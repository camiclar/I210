#15.2
# A teacher has a list of final scores for her class
# Write a program using a list comprehension to figure out what percentage passed her course
# A passing grade for this core course is 70% or more

# write a list comprehension that sets scores as either "pass" or "fail"
# e.g. output: ['pass', 'pass', 'fail', ...]
def pass_or_fail(grades):
    results = ["pass" if grade >= 70.0 else "fail" for grade in grades]
    return results

def get_percent_passed(results):
    num_passed = 0
    for student in results:
        if student == "pass":
            num_passed += 1
    percent_passed = (num_passed / len(results)) * 100
    return percent_passed

# use this information to figure out what percentage of students passed the course
# e.g. output: Percent passed: 82.6%

if __name__ == "__main__":
    grades = [90.2, 100, 48.5, 89.8, 73, 78.2, 67, 99, 85.4, 97.1, 93.3, 75.5, 96.9, 100, 55, 88.1, 97.6, 94, 100, 69, 73.3, 78.4, 81.1]
    results = pass_or_fail(grades)
    print(f"Percent passed: {get_percent_passed(results):.1f}%")
