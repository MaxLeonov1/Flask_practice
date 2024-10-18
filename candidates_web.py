import json
from flask import Flask
from jinja2.ext import debug

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates_data = json.loads(file.read())
print(candidates_data)

@app.route("/")
def page_index():
    site_str = ''
    for candidate in candidates_data:
        site_str = site_str + f"<pre>\nИмя: {candidate['name']}\nПозиция кандидата: {candidate['position']}\nНавыки: {candidate['skills']}"
    #print(site_str)
    return site_str

@app.route("/candidate/<int:uid>")
def candidate_recall(uid):
    for candidate in candidates_data:
        if candidate['id'] == uid:
            return f"<img src={candidate['picture']}><pre>\nИмя: {candidate['name']}\nПозиция кандидата: {candidate['position']}\nНавыки: {candidate['skills']}"

@app.route("/skill/<skill>")
def skill_search(skill):
    site_str = ''
    skill_ = skill.lower()
    for candidate in candidates_data:
        sk = candidate['skills'].split(', ')
        for skill_i in sk:
            if skill_i.lower() == skill_:
                site_str = site_str + f"<pre>\nИмя: {candidate['name']}\nПозиция кандидата: {candidate['position']}\nНавыки: {candidate['skills']}"
    return site_str
app.run(debug=True)