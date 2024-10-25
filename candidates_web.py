import json
from flask import Flask, render_template
from jinja2.ext import debug

app = Flask(__name__)

with open('candidates.json', 'r', encoding='utf-8') as file:
    candidates_data = json.loads(file.read())
print(candidates_data)

@app.route("/")
def page_index():
    return render_template('main_screen.html',candidates=candidates_data)

@app.route("/candidate/<int:uid>")
def candidate_recall(uid):
    for candidate in candidates_data:
        if candidate['id'] == uid:
            return render_template('candidate_info.html',candidate=candidate)

@app.route("/skill/<skill>")
def skill_search(skill):
    site = []
    skill_ = skill.lower()
    for candidate in candidates_data:
        sk = candidate['skills'].split(', ')
        for skill_i in sk:
            if skill_i.lower() == skill_:
                site.append(candidate)
    return render_template('skill_search.html',candidates = site)
app.run(debug=True)