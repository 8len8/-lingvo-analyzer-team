from modules.question_bank import get_random_questions, shuffle_options, generate_test_variant
from modules.test_ui import *

def main():
    show_welcome()
    
    mode = choose_mode()
    
    variant = generate_test_variant()
    print(f"\n Ваш вариант теста: {variant}")
    
    raw_questions = get_random_questions(5)
    
    questions = [shuffle_options(q) for q in raw_questions]
    
    correct_count = 0
    mistakes = []
    
    for i, q in enumerate(questions, 1):
        user_answer, is_correct = ask_question(q, i, len(questions), mode)
        
        if is_correct:
            correct_count += 1
            print(" Правильно!")
        else:
            mistakes.append({
                "question": q["question"],
                "user_answer": q["options"][user_answer],
                "correct_answer": q["options"][q["correct"]]
            })
            print(" Неправильно!")
    
    show_result(correct_count, len(questions), mistakes, mode, variant)
    show_goodbye()

if __name__ == "__main__":
    main() 
