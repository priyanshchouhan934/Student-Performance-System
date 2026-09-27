def get_stats(marks):
    total = sum(marks)
    avg = total / len(marks)
    return total, avg, max(marks), min(marks)
def count_pass_fail(marks):
    passed = 0
    failed = 0
    for m in marks:
        if m >= 40:
            passed += 1
        else:
            failed += 1
    return passed, failed
def calc_score(avg, attendance, assignment, quiz, study_hours):
    study_bonus = study_hours * 5
    if study_bonus > 15:
        study_bonus = 15  # cap it so study hours cant carry the whole score
    score = avg*0.5 + attendance*0.15 + assignment*0.1 + quiz*0.1 + study_bonus
    return score
def predict_outcome(score, failed, attendance):
    if failed > 0 and score < 60:
        return "At Risk"
    if attendance < 75:
        return "Needs Improvement"
    if score >= 85:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Average"
    return "Needs Improvement"
def show_report(student):
    marks = student["marks"]
    total, avg, highest, lowest = get_stats(marks)
    passed, failed = count_pass_fail(marks)
    score = calc_score(avg, student["attendance"], student["assignment"], student["quiz"], student["study"])
    outcome = predict_outcome(score, failed, student["attendance"])
    print("\n===== PERFORMANCE REPORT =====")
    print("Name:", student["name"])
    print("Roll:", student["roll"])
    print("Marks:", marks)
    print("Total:", total)
    print("Average:", round(avg, 2))
    print("Passed:", passed, "Failed:", failed)
    print("Performance Score:", round(score, 2))
    print("Prediction:", outcome)