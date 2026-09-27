def get_unique(marks):
    seen = []
    for m in marks:
        if m not in seen:
            seen.append(m)
    return seen
def kth_smallest(marks, k):
    # bubble sort, dont need anything fancy for 4 subjects
    data = marks[:]
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    return data[k-1]
def show_analysis(student):
    marks = student["marks"]
    high = 0
    for m in marks:
        if m >= 75:
            high += 1
    print("\n===== ARRAY / LIST ANALYSIS =====")
    print("Reverse:", marks[::-1])
    print("Unique:", get_unique(marks))
    print("Marks >= 75:", high)
    print("3rd smallest:", kth_smallest(marks, 3))