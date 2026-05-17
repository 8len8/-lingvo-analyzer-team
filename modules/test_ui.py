def show_welcome():
    print("\n=== ГЕНЕРАТОР ТЕСТОВ ===")
    print("Добро пожаловать!")

def choose_mode():
    print("\n1. Обучение (с подсказкой)")
    print("2. Экзамен (без подсказок)")
    choice = input("Выберите режим (1(обуч) или 2(экз)): ")
    return "learning" if choice == "1" else "exam"

def ask_question(question_dict, num, total, mode):
    print(f"\nВопрос {num} из {total}:")
    print(question_dict["question"])
    for i, opt in enumerate(question_dict["options"]):
        print(f"{i+1}. {opt}")
    if mode == "learning":
        print(f" Подсказка: правильный вариант {question_dict['correct'] + 1}")
    while True:
        try:
            answer = int(input("Ваш ответ (номер): ")) - 1
            if 0 <= answer < len(question_dict["options"]):
                return answer, answer == question_dict["correct"]
            print(f"Введите число от 1 до {len(question_dict['options'])}")
        except ValueError:
            print("Введите число!")

def show_result(correct, total, mistakes, mode, variant):
    print("\n" + "="*40)
    print("РЕЗУЛЬТАТЫ ТЕСТА")
    print(f"Вариант: {variant}")
    print(f"Режим: {'Обучение' if mode == 'learning' else 'Экзамен'}")
    print(f"Правильных ответов: {correct} из {total}")
    percent = (correct / total) * 100
    print(f"Процент: {percent:.1f}%")
    if percent >= 90:
        grade = "5 (Отлично)"
    elif percent >= 70:
        grade = "4 (Хорошо)"
    elif percent >= 50:
        grade = "3 (Удовлетворительно)"
    else:
        grade = "2 (Неудовлетворительно)"
    print(f"Оценка: {grade}")
    if mistakes:
        print("\n--- ОШИБКИ ---")
        for m in mistakes:
            print(f"Вопрос: {m['question']}")
            print(f" Ваш ответ: {m['user_answer']}")
            print(f" Правильный: {m['correct_answer']}\n")

def show_goodbye():
    print("\nСпасибо за прохождение теста! До свидания!")
