import json
def parse_resume_to_json(resume_content):
    resume_lines = resume_content.strip().split("\n")
    resume_json = {
        "name": resume_lines[0],
        "address": resume_lines[1],
        "contact": resume_lines[2],
        "objective": resume_lines[4],
        "experience": [],
        "education": resume_lines[14],
        "skills": resume_lines[16].split(": ")[1].split(", ")
    }
    
    experience = []
    current_experience = {}
    for line in resume_lines[6:13]:
        if line.startswith("-"):
            current_experience.setdefault("responsibilities", []).append(line.lstrip("- ").strip())
        else:
            if current_experience:
                experience.append(current_experience)
            current_experience = {"title": line}
    experience.append(current_experience)
    
    resume_json["experience"] = experience
    return json.dumps(resume_json, indent=4)

# Parsing the resume
parsed_resume = parse_resume_to_json(resume_content)
print(parsed_resume)
