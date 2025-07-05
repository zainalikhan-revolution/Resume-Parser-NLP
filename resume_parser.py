import spacy
import re

nlp = spacy.load("en_core_web_sm")

with open("sample_resume.txt", "r", encoding="utf-8") as file:
    resume_text = file.read()

doc = nlp(resume_text)

name = None
for ent in doc.ents:
    if ent.label_ == "PERSON":
        name = ent.text
        break

email = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", resume_text)
phone = re.findall(r"\+?\d[\d -]{8,}\d", resume_text)

skill_keywords = ['Python', 'Machine Learning', 'TensorFlow', 'NLP', 'Streamlit']
skills_found = [skill for skill in skill_keywords if skill.lower() in resume_text.lower()]

experience_lines = [line for line in resume_text.split('\n') if 'experience' in line.lower() or 'worked' in line.lower()]

print("Name:", name)
print("Email:", email)
print("Phone:", phone)
print("Skills:", skills_found)
print("Experience:", experience_lines)
