# ЛАБОРАТОРНАЯ РАБОТА №8

## Задание А -> `src/lab08/models.py`.

**Требования**:

Модель **`Student`**, содержащая:

- декоратор `@dataclass`
- поля:
  - `fio`
  - `birthdate`
  - `group`
  - `gpa`
- методы:
  - `age()`
  - `to_dict()`
  - `from_dict()`
  - `__str__()`
- валидацию:
  - формата даты (`YYYY-MM-DD`)
  - диапазона среднего балла `0 ≤ gpa ≤ 5`


#### Выполнение:

```python
from dataclasses import dataclass
from datetime import datetime, date


@dataclass
class Student:
    fio: str
    birthdate: str
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("warning: birthdate format might be invalid")

        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self):
        b = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        return today.year - b.year - ((today.month, today.day) < (b.month, b.day))

    def to_dict(self):
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            fio=d["fio"],
            birthdate=d["birthdate"],
            group=d["group"],
            gpa=d["gpa"],
        )

    def __str__(self):
        return f"{self.fio} ({self.group}), gpa={self.gpa}"


if __name__ == "__main__":
    # Create
    student = Student("Zagrebin Egor Denisovich", "2008-02-10", "BIVT-25-4", 5.0)
    print(student)
    print(f"Age: {student.age()}")

    # Serialize
    student_dict = student.to_dict()
    print(f"Serialized: {student_dict}")

    # Deserialize
    restored_student = Student.from_dict(student_dict)
    print(f"Restored: {restored_student}")
```

#### Результат:

![lab08a output](../../images/lab08/8a_ouput.png)

## Задание B -> `src/lab08/serialize.py`

**Требования**:

Реализовать фунцкии для сериализации 

1. `students_to_json(students, path)`

Сохраняет список студентов в JSON.

2. `students_from_json(path) -> list[Student]`

-   читает JSON-массив
-   валидирует
-   создаёт список `Student`

#### Выполнение:

```python
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
```

#### Результат:

```python
s1 = Student("Zagrebin Egor Denisovich", "2008-02-10", "BIVT-25-4", 5.0)
s2 = Student("Perreira Alex UFCovich", "2001-01-10", "BIVT-25-1", 4.2)
s3 = Student("Volkanovski Alex MMAovich", "2012-02-12", "BIVT-25-2", 3.0)
s4 = Student("McGregorov Connor Michailovich", "2025-10-18", "BIVT-25-3", 4.6)

students = [s1, s2, s3, s4]
```
Исходный список объектов класса Student был сериализован в формате JSON и сохранён в файл `src/data/lab08/students_output.json`. 

![seriaalization result json](../../images/lab08/seri_json.png)