from typing import List, Tuple


def show_history() -> None:
    print("\n== Brief history of Python ==")


def get_names_score() -> Tuple[List[str], List[float]]:
    while True:
        try:
            count = int(input("Number of students: "))
            if count <= 0:
                print("Please enter a number greater than zero")
                continue
            break
        except ValueError:
            print("Invalid input")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores:")

    for i in range(count):
        name = input(f'Student {i + 1} name: ').strip()
        if not name:
            name = f'Student {i + 1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f'Enter the score for {name}: '))
                if 0 <= score <= 100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")
            except ValueError:
                print("Invalid input")

    return names_of_students, scores  # Fixed indentation


def calculate_average(scores: List[float]) -> float:  
    return sum(scores) / len(scores) if scores else 0.0


def assign_grades(scores: List[float]) -> List[str]:
    grades = []
    for score in scores:
        if score >= 90:
            grades.append("A")
        elif score >= 80:
            grades.append("B")
        elif score >= 70:
            grades.append("C")
        elif score >= 60:
            grades.append("D")
        else:
            grades.append("F")
    return grades


def display_results(names: List[str], scores: List[float], grades: List[str], average: float) -> None:
    print("\n== Results ==")
    for name, score, grade in zip(names, scores, grades):
        print(f"{name}: Score = {score:.2f}, Grade = {grade}")
    print(f"\nClass Average: {average:.2f}")


def main() -> None:
    show_history()
    names, scores = get_names_score()
    average = calculate_average(scores)
    grades = assign_grades(scores)
    display_results(names, scores, grades, average)


if __name__ == "__main__":
    main()