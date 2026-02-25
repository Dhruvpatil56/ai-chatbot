import os
import sqlite3
import json
from flask import Flask, render_template, request, jsonify, session
from groq import Groq
from dotenv import load_dotenv
import uuid

load_dotenv()

app = Flask(__name__)
app.secret_key = "chatbot-secret-key"

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = {
    "role": "system",
    "content": "You are a helpful AI assistant. You are smart, concise, and friendly."
}

# ── DB path — points to volume mount for Docker ─────────────
DB_PATH = "/app/data/chat_history.db"

# ── Database setup ──────────────────────────────────────────
def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            session_id TEXT NOT NULL,
            role TEXT NOT NULL,
            content TEXT NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def get_history(session_id):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content FROM conversations WHERE session_id = ? ORDER BY id ASC",
        (session_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    history = [system_prompt]
    for role, content in rows:
        history.append({"role": role, "content": content})
    return history

def save_message(session_id, role, content):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO conversations (session_id, role, content) VALUES (?, ?, ?)",
        (session_id, role, content)
    )
    conn.commit()
    conn.close()

# ── Routes ───────────────────────────────────────────────────
@app.route("/")
def index():
    if "session_id" not in session:
        session["session_id"] = str(uuid.uuid4())
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    session_id = session.get("session_id", str(uuid.uuid4()))

    save_message(session_id, "user", user_message)
    history = get_history(session_id)

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=history,
        temperature=0.7,
        max_tokens=1024
    )

    assistant_message = response.choices[0].message.content
    save_message(session_id, "assistant", assistant_message)

    return jsonify({"reply": assistant_message})

@app.route("/history", methods=["GET"])
def history():
    session_id = session.get("session_id")
    if not session_id:
        return jsonify([])

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT role, content, timestamp FROM conversations WHERE session_id = ? ORDER BY id ASC",
        (session_id,)
    )
    rows = cursor.fetchall()
    conn.close()

    return jsonify([{"role": r, "content": c, "timestamp": t} for r, c, t in rows])

@app.route("/clear", methods=["POST"])
def clear():
    session_id = session.get("session_id")
    if session_id:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM conversations WHERE session_id = ?", (session_id,))
        conn.commit()
        conn.close()
        session["session_id"] = str(uuid.uuid4())
    return jsonify({"status": "cleared"})

# ── Init and run ─────────────────────────────────────────────
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=False)
