# profile.py

def get_profile():
    return {
        "name": "Власян Давит",
        "group": "РПО-2",
        "role": "student",
        "skills": ["Git", "VS Code", "Python"]
    }


def print_profile():
    profile = get_profile()
    print(f"Студент: {profile['davit']}")
    print(f"Группа: {profile['group-2']}")
    print("Навыки:", ", ".join(profile["skills"]))
