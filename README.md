# 🚀 Smart Career Guide – AI Career Mentor

Smart Career Guide is an AI-powered web app that generates a **personalized career plan** based on a user's:
- Education
- Current Skills
- Interests

It provides:
1. Best Career Path  
2. Skill Gap Analysis  
3. 6-Month Learning Roadmap  
4. Resume Improvement Tips  

Built for hackathons and MVP demos using **Flask + Google Gemini API** with a clean, modern UI.

---

## 🧠 How It Works

1. User enters:
   - Name  
   - Education  
   - Skills  
   - Interests  
2. Data is sent to Flask backend.
3. A prompt is generated and sent to **Google Gemini (GenAI)**.
4. AI returns a structured career plan.
5. Result is displayed on a beautiful report page with:
   - Copy button  
   - Print option  

---

## 🛠 Tech Stack

- Frontend:  
  - HTML  
  - CSS (Glassmorphism UI)  
- Backend:  
  - Python  
  - Flask  
- AI Engine:  
  - Google Gemini (`google-genai`)
- Deployment Ready:  
  - Works on localhost & cloud platforms

---

## 📂 Project Structure

```
Smart-Career-Guide/
│
├── app.py
├── requirements.txt
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
```

 
## ▶️ How to Run Locally

1. Clone the repository:
```bash
git clone https://github.com/your-username/smart-career-guide.git
cd smart-career-guide
```

2.Install dependencies:
```
pip install -r requirements.txt
```
Run the app:
```
python app.py
```

Open in browser:
```
http://127.0.0.1:5000
```
---
✨ Features

AI-generated career guidance

Clean modern UI

Copy & Print career report

Fast response using Gemini Flash model

Hackathon-ready MVP

Easy to extend:

Resume checker

Skill tracker

Student dashboard

Login system

---
🏆 Use Cases

Hackathons

College projects

Career counseling tools

EdTech MVP demos

Portfolio project

---
💡 Future Improvements

Resume upload & analysis

User accounts & history

Career dashboards

Skill progress tracking

Multi-language support

Made with ❤️ using Flask + Google AI

---
## 👨‍💻 Author

**Jitendra Gaherwar**  
B.Tech (Information Technology)  
Data & AI Developer  

Focused on building practical, real-world AI tools for learning, productivity, and career growth.  
Passionate about transforming ideas into usable products using Python, ML, and modern AI APIs.
