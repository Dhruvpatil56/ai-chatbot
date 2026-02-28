# 🚀 AI Chatbot Platform

A lightweight AI-powered chatbot built using **Python, Flask, SQLite, Docker, and Kubernetes-ready manifests**.

Originally developed as a CLI chatbot, this project evolved into a containerized web application with persistent storage and deployment-ready infrastructure — built with a **server administration and DevOps mindset**.

The application integrates with the **Groq API** by default and can be easily adapted to use **OpenAI API**.

---

## 🧠 Core Features

- CLI chatbot engine  
- Flask-based web interface  
- Persistent chat storage (SQLite)  
- Secure environment-based secret management  
- Groq API integration (OpenAI optional)  
- Docker containerization  
- Docker Compose support  
- Kubernetes manifests (Deployment, Service, PVC, Secret template)  
- Clean, production-aware project structure  

---

## 📁 Project Structure

```
ai-chatbot/
├── Dockerfile
├── docker-compose.yml
├── app.py
├── chatbot.py
├── requirements.txt
├── chat_history.db
├── data/
├── templates/
│   └── index.html
├── k8s/
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── pvc.yaml
│   └── secret.example.yaml
└── README.md
```

---

## ⚙️ Prerequisites

- Ubuntu / Linux server  
- Python 3.10+  
- pip  
- Docker (optional)  
- Kubernetes (optional)  
- Groq API key (default)  

---

## 🔐 Environment Configuration

Create a `.env` file in the project root:

```
GROQ_API_KEY=your_groq_api_key_here
```

If switching to OpenAI:

```
OPENAI_API_KEY=your_openai_api_key_here
```

Ensure `.env` is added to `.gitignore`.

---

# 🖥️ Local Setup (Without Docker)

### 1️⃣ System Setup

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv sqlite3 -y
```

### 2️⃣ Clone Repository

```bash
git clone https://github.com/Dhruvpatil56/ai-chatbot.git
cd ai-chatbot
```

### 3️⃣ Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run Application

```bash
python3 app.py
```

Access in browser:

```
http://<server-ip>:5000
```

---

# 🐳 Docker Deployment

### Build Image

```bash
docker build -t ai-chatbot .
```

### Run Container

```bash
docker run -d \
  -p 5000:5000 \
  --env-file .env \
  --name ai-chatbot \
  ai-chatbot
```

Access:

```
http://<server-ip>:5000
```

---

# 🐳 Docker Compose (Optional)

```bash
docker compose up -d --build
```

---

# ☸️ Kubernetes Deployment (Optional)

### Create Secret

```bash
kubectl create secret generic ai-chatbot-secret \
  --from-literal=GROQ_API_KEY=your_groq_api_key
```

### Deploy

```bash
kubectl apply -f k8s/
```

### Verify

```bash
kubectl get pods
kubectl get svc
```

---

## 🗄️ Database

- SQLite used for chat persistence  
- `chat_history.db` stores conversation history  
- Designed for lightweight/internal usage  
- Can be replaced with PostgreSQL for production scaling  

---

## 🔒 Security Considerations

- API keys stored in environment variables  
- No secrets committed to repository  
- Stateless container design  
- Runtime data separated from source code  
- Kubernetes secrets templated securely  

---

## 📦 DevOps Practices Applied

- Virtual environment isolation  
- Dependency locking via `requirements.txt`  
- Docker containerization  
- Kubernetes deployment manifests  
- Clean Git history  
- No hardcoded credentials  
- Infrastructure-aware architecture  

---

## 🎯 Project Evolution

CLI Chatbot  
→ Flask Web UI  
→ SQLite Persistence  
→ Dockerized Deployment  
→ Kubernetes-Ready Manifests  

Built to simulate a lightweight, production-style AI service with operational awareness.

---

## 👨‍💻 Author

**Dhruv Patil**  
DevOps & Cloud Enthusiast
