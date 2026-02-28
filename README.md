🚀 AI Chatbot Platform

A lightweight AI-powered chatbot platform built with Python, Flask, SQLite, Docker, and Kubernetes-ready manifests.

This project started as a CLI chatbot and evolved into a containerized web application with persistent storage and deployment-ready infrastructure — designed with a server administration and DevOps mindset.

The application currently integrates with the Groq API, and can be easily adapted to use OpenAI if required.

🧠 Features

CLI-based chatbot core

Flask web UI

Persistent chat history (SQLite)

Environment-based secret management

Groq API integration

Dockerized deployment

Docker Compose support

Kubernetes manifests (Deployment, Service, PVC, Secret template)

Clean project structure

Git-ready (no secrets committed)

📁 Project Structure
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
⚙️ Prerequisites

Ubuntu/Linux server

Python 3.10+

pip

Docker (optional)

Kubernetes (optional)

Groq API key (default)

OpenAI API key (optional alternative)

🔐 Environment Configuration

Create a .env file in the project root:

GROQ_API_KEY=your_groq_api_key_here

If switching to OpenAI, update your application logic and use:

OPENAI_API_KEY=your_openai_api_key_here

Make sure .env is listed in .gitignore.

🖥️ Running Locally (Without Docker)
1️⃣ Install Dependencies
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip python3-venv sqlite3 -y
2️⃣ Clone Repository
git clone https://github.com/Dhruvpatil56/ai-chatbot.git
cd ai-chatbot
3️⃣ Create Virtual Environment
python3 -m venv venv
source venv/bin/activate
4️⃣ Install Requirements
pip install -r requirements.txt
5️⃣ Run Application
python3 app.py

Application will be available at:

http://<server-ip>:5000
🐳 Running with Docker
1️⃣ Build Image
docker build -t ai-chatbot .
2️⃣ Run Container
docker run -d \
  -p 5000:5000 \
  --env-file .env \
  --name ai-chatbot \
  ai-chatbot

Access:

http://<server-ip>:5000
🐳 Docker Compose (Optional)

If using docker-compose.yml:

docker compose up -d --build
☸️ Kubernetes Deployment (Optional)

Inside k8s/ directory:

1️⃣ Create Secret
kubectl create secret generic ai-chatbot-secret \
  --from-literal=GROQ_API_KEY=your_groq_api_key

(Modify if using OpenAI instead.)

2️⃣ Apply Manifests
kubectl apply -f k8s/

Verify:

kubectl get pods
kubectl get svc
🗄️ Database

SQLite used for persistent chat history

chat_history.db stores conversation records

Designed for lightweight internal usage

Can be replaced with PostgreSQL in production environments

🔒 Security Considerations

API keys stored in environment variables

No secrets committed to repository

Stateless container design

DB persistence handled separately

Designed for least-privilege execution

Secrets templated in Kubernetes manifests

📦 DevOps Practices Applied

Environment isolation via virtualenv

Dependency locking (requirements.txt)

Docker containerization

Kubernetes deployment manifests

Separation of runtime data

Clean Git history

No hardcoded secrets

Infrastructure-aware project structure

🎯 Project Evolution

This project began as a simple CLI chatbot using Groq API and progressively evolved into a production-style AI web tool, focusing on:

Stability

Secure configuration

Maintainability

Deployment flexibility

Infrastructure awareness

👨‍💻 Author

Dhruv Patil
DevOps & Cloud Enthusiast
