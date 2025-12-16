from src.lab09.group import Group
from src.lab08.models import Student

group = Group("src/data/lab09/students.csv")
group.update("Perreira Alex UFCovich", gpa=2.0)
for s in group.list():
    print(s)
