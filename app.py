from flask import Flask, render_template, request
import google.genai as genai

client = genai.Client(api_key="AIzaSyArqG_0ipAUsA4TqM1Vejachgf3saZYMDI")
# import google.generativeai as genai
# genai.configure(api_key="AIzaSyArqG_0ipAUsA4TqM1Vejachgf3saZYMDI")

# for m in genai.list_models():
#     if "generateContent" in m.supported_generation_methods:
#         print(m.name)


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route('/analyze', methods=['POST'])
def analyze():
    name = request.form.get('name')
    education = request.form.get('education')
    skills = request.form.get('skills')
    interest = request.form.get('interest')

    prompt = f"""
You are a professional career mentor.

Student Name: {name}
Education: {education}
Current Skills: {skills}
Interests: {interest}

Give output in clear sections:
1. Best Career Path
2. Skill Gap
3. 6-Month Learning Roadmap (Month-wise)
4. Resume Improvement Tips


IMPORTANT:
- Do NOT use markdown symbols like ##, **, |, --- or tables.
- Write in simple plain text with headings and bullet points.
- Make it clean and readable for normal users.
"""

    response = client.models.generate_content(
        model="models/gemini-2.5-flash-lite",
        contents=prompt
    )

    result = response.text
     
    
    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
