import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Knowledge base (could be stored in database instead)

job_positions = [
    {
        "title": "Entry-Level Python Engineer",
        "needed_skills": ["Python course work", "Software Engineering course work"],
        "desire_skills": ["Agile course"],
        "qualifications": "Bachelor in CS"
    },
    {
        "title": "Python Engineer",
        "needed_skills": ["3 years Python development", "1 year data development", "Experience in Agile projects"],
        "desire_skills": ["Used Git"],
        "qualifications": "Bachelor in CS" 
    },
    {
        "title": "Project Manager",
        "needed_skills": ["3 years managing software projects", "2 years in Agile projects"],
        "desire_skills": [],
        "qualifications": "PMI Lean Project Managment Certification"
    },
    {
        "title": "Senior Knowledge Engineer",
        "needed_skills": ["3 years using Python to develop Expert Systems", "2 years data architecture amd development"],
        "desire_skills": [],
        "qualifications": "Masters in CS"
    }
]

@app.route('/evaluate', methods = ['POST'])

def evaluate_applicant():
    data = request.get_json()
    
    if not data:
        return jsonify({"status": "Error", "reason": "Invalid JSON format"}), 400
    
    applicant_skills = data.get("skills", [])
    applicant_qualifications = data.get("qualifications", "")
    
    if not isinstance(applicant_skills, list) or not isinstance(applicant_qualifications, str):
        return jsonify({"status": "Error", "reason": "Invalid JSON format"}), 400
    
    qualified_jobs = []
    
    for job in job_positions:
        if all(skill in applicant_skills for skill in job["needed_skills"]) and job["qualifications"] == applicant_qualifications:
            qualified_jobs.append(job["title"])
            
    if qualified_jobs:
        return jsonify({"status": "Accepted", "positions": qualified_jobs})
    else:
        return jsonify({"status": "Rejected", "reason": "Applicant does not meet required qualifications or skills."})
    

if __name__ == '__main__':
    app.run(debug = True)