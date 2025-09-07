
## lambda function
divide = lambda x, y: x / y if y != 0 else "Error: Division by zero"


## use of lambda functions

def first():
    
    avg = lambda seq: sum(seq) / len(seq) if seq else 0
    total = lambda seq: sum(seq) if seq else 0
    top = lambda seq: max(seq) if seq else None

    students = [
        {"name": "Alice", "age": 22, "grades": [85, 90, 88, 91, 87]},
        {"name": "Bob", "age": 23, "grades": [78, 82, 80, 79, 81]},
        {"name": "Charlie", "age": 21, "grades": [92, 95, 94, 96, 93]},
        {"name": "Diana", "age": 22, "grades": [88, 84, 90, 89, 92]},
        {"name": "Ethan", "age": 24, "grades": [75, 77, 73, 80, 78]},
        {"name": "Fiona", "age": 20, "grades": [91, 89, 93, 90, 94]}
    ]

    for student in students:
        operation = input(f"{student['name']}: enter operation (average/total/top): ").strip().lower()
        grades = student["grades"]
        if operation in ("average", "avg"):
            print(avg(grades))            
        elif operation == "total":
            print(total(grades))
        elif operation == "top":
            print(top(grades))


#### Lambda ninja master

def second():
    # avg = lambda seq: sum(seq) / len(seq) if seq else 0
    # total = lambda seq: sum(seq) if seq else 0
    # top = lambda seq: max(seq) if seq else None

    # operations = {
    #     "average": avg,
    #     "total": total,
    #     "top": top
    # }


    students = [
        {"name": "Alice", "age": 22, "grades": [85, 90, 88, 91, 87]},
        {"name": "Bob", "age": 23, "grades": [78, 82, 80, 79, 81]},
        {"name": "Charlie", "age": 21, "grades": [92, 95, 94, 96, 93]},
        {"name": "Diana", "age": 22, "grades": [88, 84, 90, 89, 92]},
        {"name": "Ethan", "age": 24, "grades": [75, 77, 73, 80, 78]},
        {"name": "Fiona", "age": 20, "grades": [91, 89, 93, 90, 94]}
    ]

    operations = {
        "average": lambda seq: sum(seq) / len(seq) if seq else 0,
        #"total": lambda seq: sum(seq) if seq else 0,
        "total": sum,
        #"top": lambda seq: max(seq) if seq else None
        "top": max
    }

    for student in students:
        operation = input(f"{student['name']}: enter operation (average/total/top): ").strip().lower()
        print(operations[operation](student["grades"]))

#first()
second()