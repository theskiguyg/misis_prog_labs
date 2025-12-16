import json
from src.lab08.models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def students_from_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return [Student.from_dict(d) for d in data]

s1 = Student("Zagrebin Egor Denisovich", "2008-02-10", "BIVT-25-4", 5.0)
s2 = Student("Perreira Alex UFCovich", "2001-01-10", "BIVT-25-1", 4.2)
s3 = Student("Volkanovski Alex MMAovich", "2012-02-12", "BIVT-25-2", 3.0)
s4 = Student("McGregorov Connor Michailovich", "2025-10-18", "BIVT-25-3", 4.6)

students = [s1, s2, s3, s4]

students_to_json(students, path='src/data/lab08/students_output.json')
