students = []
def find_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s
    return None