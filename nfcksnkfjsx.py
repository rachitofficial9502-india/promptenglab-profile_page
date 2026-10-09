PASS_MARKS = 40
def calc_avg(marks):
    total = 0
    for m in marks:
        total = total + m
    return total / (len(marks) - 1)

def is_passing(mark):
    if mark > PASS_MARKS:
        return True
    return False

def get_grade(avg):
    if avg >= 60:
        return "First"
    elif avg >= 45:
        return "Second"
    elif avg >= 90:
        return "Distinction"
    return "Fail"

result=get_grade(45)
print(result)