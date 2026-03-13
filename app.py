import os
import smtplib
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SENDER_EMAIL = os.getenv("SENDER_EMAIL", "your_email@gmail.com")
SENDER_PASSWORD = os.getenv("SENDER_PASSWORD", "your_app_password")
RECIPIENT_EMAIL = os.getenv("RECIPIENT_EMAIL", "niravpanchal9980@gmail.com")
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

KNOWLEDGE_BASE = {
    "name": "Nirav Panchal",
    "email": "niravpanchal9980@gmail.com",
    "github": "https://github.com/niravpanchal11",
    "linkedin": "https://www.linkedin.com/in/niravpanchal11/",
    "twitter": "https://twitter.com/niravpanchal_11/",
    "youtube": "https://www.youtube.com/@niravpanchal11",
    "leetcode": "https://leetcode.com/u/niravpanchal/",
    "geeksforgeeks": "https://auth.geeksforgeeks.org/user/niravpanchal11/",
    "codeforces": "https://codeforces.com/profile/Nirav_11",
    "hackerrank": "https://www.hackerrank.com/profile/niravpanchal11",
    "codechef": "https://www.codechef.com/users/nirav_11",
    "hackerearth": "https://www.hackerearth.com/@niravpanchal9980",
    "description": "Backend Developer | DevOps Engineer | Data Engineer | AI/ML Engineer",
    "competitive_programming": "300+ DSA and competitive programming problems solved",
    "expertise": ["Backend Development", "DevOps Engineering", "Data Engineering", "AI/ML Engineering"],
    "skills": {
        "languages": ["Python", "Java", "C++", "JavaScript", "TypeScript", "SQL", "Bash"],
        "backend": ["Django", "Flask", "FastAPI", "Spring Boot", "Node.js", "RESTful APIs", "GraphQL", "Microservices"],
        "devops": ["AWS", "Azure", "Docker", "Kubernetes", "Jenkins", "GitLab CI/CD", "Terraform", "Ansible", "CloudFormation"],
        "data_engineering": ["Apache Spark", "Apache Kafka", "Airflow", "ETL Pipelines", "Data Warehousing", "BigQuery", "Snowflake"],
        "ai_ml": ["TensorFlow", "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Machine Learning", "Deep Learning", "NLP", "Computer Vision"],
        "databases": ["PostgreSQL", "MySQL", "MongoDB", "Redis", "DynamoDB", "Cassandra", "Elasticsearch"],
        "tools": ["Git", "Linux", "Nginx", "RabbitMQ", "Grafana", "Prometheus", "ELK Stack"],
        "competitive": ["LeetCode", "CodeChef", "HackerRank", "HackerEarth", "GeeksForGeeks", "CodeForces"]
    },
    "social": ["LinkedIn", "Twitter", "YouTube", "LeetCode", "GeeksforGeeks", "CodeForces", "HackerRank", "CodeChef", "HackerEarth"]
}

class Message(BaseModel):
    message: str

class EmailRequest(BaseModel):
    name: str
    email: EmailStr
    subject: str
    message: str

def get_response(user_message: str) -> str:
    message = user_message.lower().strip()
    
    if any(word in message for word in ["hello", "hi", "hey", "greetings", "what's up"]):
        return f"Hello! 👋 I'm Nirav Panchal's AI assistant. I can help you learn about his skills, experience, and projects. What would you like to know?"
    
    if any(word in message for word in ["name", "who are you", "who is this"]):
        return f"This is {KNOWLEDGE_BASE['name']}'s portfolio! He's a Full Stack Software Engineer. What would you like to know about him?"
    
    if any(word in message for word in ["about", "tell me", "describe", "introduction"]):
        return f"{KNOWLEDGE_BASE['name']} is a {KNOWLEDGE_BASE['description']}. He specializes in Backend Development, DevOps Engineering, Data Engineering, and AI/ML Engineering. Feel free to ask about his skills, projects, or how to contact him!"
    
    if any(word in message for word in ["contact", "email", "reach", "get in touch"]):
        return f"You can reach Nirav at: 📧 {KNOWLEDGE_BASE['email']}\n\nOr connect with him on:\n• LinkedIn: linkedin.com/in/niravpanchal11\n• GitHub: github.com/niravpanchal11\n• Twitter: @niravpanchal_11"
    
    if any(word in message for word in ["skill", "expertise", "what do you know", "proficient", "specialization"]):
        skills_response = "Nirav specializes in:\n\n"
        skills_response += f"🎯 Core Expertise: {', '.join(KNOWLEDGE_BASE['expertise'])}\n\n"
        skills_response += f"💻 Languages: {', '.join(KNOWLEDGE_BASE['skills']['languages'])}\n\n"
        skills_response += f"⚙️ Backend: {', '.join(KNOWLEDGE_BASE['skills']['backend'])}\n\n"
        skills_response += f"☁️ DevOps: {', '.join(KNOWLEDGE_BASE['skills']['devops'])}\n\n"
        skills_response += f"📊 Data Engineering: {', '.join(KNOWLEDGE_BASE['skills']['data_engineering'])}\n\n"
        skills_response += f"🤖 AI/ML: {', '.join(KNOWLEDGE_BASE['skills']['ai_ml'])}\n\n"
        skills_response += f"🗄️ Databases: {', '.join(KNOWLEDGE_BASE['skills']['databases'])}"
        return skills_response
    
    if any(word in message for word in ["python", "java", "c++", "javascript", "typescript"]):
        if "python" in message:
            return "Nirav is highly proficient in Python! He uses it for backend development (Django, Flask, FastAPI), data engineering (Pandas, Spark), and AI/ML (TensorFlow, PyTorch, Scikit-learn). 🐍"
        elif "java" in message:
            return "Nirav has strong Java skills! He's experienced with Spring Boot for building robust backend applications and microservices. ☕"
        elif "c++" in message or "c++" in message:
            return "C++ is one of Nirav's core languages! He uses it for competitive programming, system-level development, and performance-critical applications. 🚀"
        elif "javascript" in message or "typescript" in message:
            return "Nirav is skilled in JavaScript and TypeScript! He uses them for backend development with Node.js and building scalable APIs. 💻"
    
    if any(word in message for word in ["devops", "docker", "kubernetes", "aws", "azure", "ci/cd", "jenkins", "terraform"]):
        return "Nirav is a skilled DevOps Engineer! He works with:\n\n☁️ Cloud: AWS, Azure\n🐳 Containers: Docker, Kubernetes\n🔧 CI/CD: Jenkins, GitLab CI/CD\n📦 IaC: Terraform, Ansible, CloudFormation\n📊 Monitoring: Grafana, Prometheus, ELK Stack"
    
    if any(word in message for word in ["data engineering", "data engineer", "etl", "spark", "kafka", "airflow", "pipeline"]):
        return "Nirav is an experienced Data Engineer! He specializes in:\n\n📊 Big Data: Apache Spark, Apache Kafka\n🔄 ETL Pipelines & Data Orchestration: Airflow\n🏢 Data Warehousing: BigQuery, Snowflake\n🗄️ Databases: PostgreSQL, MongoDB, Redis, Cassandra\n⚡ Real-time Data Processing"
    
    if any(word in message for word in ["ai", "ml", "machine learning", "deep learning", "tensorflow", "pytorch", "nlp", "computer vision"]):
        return "Nirav is an AI/ML Engineer with expertise in:\n\n🤖 Frameworks: TensorFlow, PyTorch, Scikit-learn\n📊 Data Science: Pandas, NumPy, Matplotlib\n🧠 Specializations: Machine Learning, Deep Learning, NLP, Computer Vision\n🔬 Model Development, Training & Deployment"
    
    if any(word in message for word in ["react", "angular", "flask", "django", "spring"]):
        if "flask" in message:
            return "Nirav uses Flask for building lightweight and flexible web applications and RESTful APIs in Python! 🍶"
        elif "django" in message:
            return "Nirav leverages Django for rapid backend development with batteries-included features and robust ORM! 🎯"
        elif "spring" in message or "springboot" in message:
            return "Nirav uses Spring Boot for Java backend development - building scalable microservices and enterprise applications! 🌱"
    
    if any(word in message for word in ["linkedin", "github", "twitter", "youtube", "social"]):
        return f"You can find Nirav on:\n\n🔗 LinkedIn: {KNOWLEDGE_BASE['linkedin']}\n🐙 GitHub: {KNOWLEDGE_BASE['github']}\n🐦 Twitter: {KNOWLEDGE_BASE['twitter']}\n📺 YouTube: {KNOWLEDGE_BASE['youtube']}"
    
    if any(word in message for word in ["leetcode", "competitive", "coding", "dsa", "algorithm", "problem solving", "codeforces", "hackerrank", "codechef", "geeksforgeeks"]):
        return f"Nirav has solved 300+ DSA and competitive programming problems! 🏆\n\nFind him on:\n• LeetCode: {KNOWLEDGE_BASE['leetcode']}\n• GeeksForGeeks: {KNOWLEDGE_BASE['geeksforgeeks']}\n• CodeForces: {KNOWLEDGE_BASE['codeforces']}\n• HackerRank: {KNOWLEDGE_BASE['hackerrank']}\n• CodeChef: {KNOWLEDGE_BASE['codechef']}\n• HackerEarth: {KNOWLEDGE_BASE['hackerearth']}"
    
    if any(word in message for word in ["project", "portfolio", "what have you built", "what has he built"]):
        return "Nirav has worked on various projects involving web development, backend systems, and competitive programming challenges. Visit the Projects page to see more details! 🚀"
    
    if any(word in message for word in ["experience", "work", "career"]):
        return "Nirav is a Backend Developer, DevOps Engineer, Data Engineer, and AI/ML Engineer with experience in building scalable applications, data pipelines, and ML models. Check out the Experience page for more details! 💼"
    
    if any(word in message for word in ["help", "what can you do", "options", "commands"]):
        return "I can help you with:\n\n• Nirav's expertise in Backend, DevOps, Data Engineering & AI/ML\n• His technical skills and tools\n• Competitive programming achievements (300+ problems)\n• Contact information and social profiles\n• Projects and experience\n\nJust ask me anything about Nirav Panchal! 😊"
    
    return "That's interesting! 🤔 I'm here to help you learn about Nirav Panchal. Feel free to ask about skills, experience, projects, or how to contact me. You can also ask for help to see all the things I can assist with!"

@app.post("/chat")
async def chat(message: Message):
    user_message = message.message
    response = get_response(user_message)
    return {"response": response}

@app.post("/send-email")
async def send_email(request: EmailRequest):
    print(f"\n{'='*50}")
    print(f"📧 Received email request from: {request.name} ({request.email})")
    print(f"Subject: {request.subject}")
    print(f"{'='*50}\n")
    
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = f"Portfolio Contact: {request.subject}"
        
        print(f"Sending email from {SENDER_EMAIL} to {RECIPIENT_EMAIL}")
        
        body = f"""
        <html>
            <body style="font-family: Arial, sans-serif; background-color: #f5f5f5; padding: 20px;">
                <div style="background-color: white; padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1);">
                    <h2 style="color: #8B5A3C; border-bottom: 3px solid #8B5A3C; padding-bottom: 10px;">New Message from Portfolio</h2>
                    
                    <div style="margin: 20px 0;">
                        <p><strong style="color: #333;">From:</strong> {request.name}</p>
                        <p><strong style="color: #333;">Email:</strong> {request.email}</p>
                        <p><strong style="color: #333;">Subject:</strong> {request.subject}</p>
                    </div>
                    
                    <div style="background-color: #f9f9f9; padding: 15px; border-left: 4px solid #8B5A3C; margin: 20px 0;">
                        <h3 style="color: #8B5A3C; margin-top: 0;">Message:</h3>
                        <p style="white-space: pre-wrap; color: #555;">{request.message}</p>
                    </div>
                    
                    <p style="color: #999; font-size: 0.9em; margin-top: 30px; border-top: 1px solid #eee; padding-top: 15px;">
                        This email was sent from your portfolio contact form.
                    </p>
                </div>
            </body>
        </html>
        """
        
        msg.attach(MIMEText(body, 'html'))
        
        print(f"Connecting to SMTP server: {SMTP_SERVER}:{SMTP_PORT}")
        
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            print("SMTP connection established, logging in...")
            server.login(SENDER_EMAIL, SENDER_PASSWORD)
            print("Login successful, sending email...")
            server.send_message(msg)
            print("✅ Email sent successfully!")
        
        return {
            "success": True,
            "message": "Email sent successfully!",
            "status": 200
        }
    
    except Exception as e:
        print(f"❌ Error sending email: {str(e)}")
        return {
            "success": False,
            "message": f"Failed to send email: {str(e)}",
            "status": 500
        }

@app.get("/")
async def root():
    return {"message": "Nirav Panchal's Portfolio API is running!", "endpoints": ["/chat", "/send-email"]}

@app.get("/health")
async def health_check():
    return {"status": "ok", "chatbot": "running", "email_service": "running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    print("\n" + "="*60)
    print("🚀 Starting Portfolio Backend Services...")
    print("="*60)
    print(f"💬 Chatbot: POST /chat")
    print(f"📧 Email Service: POST /send-email")
    print(f"📧 Sender Email: {SENDER_EMAIL}")
    print(f"📬 Recipient Email: {RECIPIENT_EMAIL}")
    print(f"🌐 Server: http://127.0.0.1:{port}")
    print("="*60 + "\n")
    uvicorn.run(app, host="0.0.0.0", port=port)
