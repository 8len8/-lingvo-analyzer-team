import random
from datetime import datetime
QUESTIONS = [
    {
        "question": "Сколько дней в году?",
        "options": ["365", "366", "364"],
        "correct": 0  
    },
    {
        "question": "Какой цвет у неба в ясный день?",
        "options": ["Зелёный", "Красный", "Голубой"],
        "correct": 2
    },
    {
        "question": "Кто написал 'Войну и мир'?",
        "options": ["Достоевский", "Толстой", "Чехов"],
        "correct": 1
    },
    {
        "question": "Столица Франции?",
        "options": ["Берлин", "Лондон", "Париж"],
        "correct": 2
    },
    {
        "question": "2 + 2 * 2 = ?",
        "options": ["6", "8", "4"],
        "correct": 0
    },
    {
        "question": "Какой газ мы вдыхаем?",
        "options": ["Кислород", "Углекислый газ", "Азот"],
        "correct": 0
    },
    {
        "question": "Сколько континентов на Земле?",
        "options": ["5", "6", "7"],
        "correct": 1
    },
    {
        "question": "Кто написал 'Евгения Онегина'?",
        "options": ["Лермонтов", "Пушкин", "Гоголь"],
        "correct": 1
    },
    {
        "question": "Самый большой океан?",
        "options": ["Индийский", "Атлантический", "Тихий"],
        "correct": 2
    },
    {
        "question": "Сколько цветов в радуге?",
        "options": ["5", "6", "7"],
        "correct": 2
    },
    {
        "question": "Кто такой Архимед?",
        "options": ["Философ", "Математик", "Художник"],
        "correct": 1
    },
    {
        "question": "Столица России?",
        "options": ["СПб", "Москва", "Казань"],
        "correct": 1
    },
    {
        "question": "Сколько дней в неделе?",
        "options": ["5", "6", "7"],
        "correct": 2
    },
    {
        "question": "Какой орган отвечает за зрение?",
        "options": ["Ухо", "Нос", "Глаз"],
        "correct": 2
    },
    {
        "question": "Кто открыл Америку?",
        "options": ["Васко да Гама", "Колумб", "Магеллан"],
        "correct": 1
    },
    {
        "question": "Сколько месяцев в году?",
        "options": ["10", "11", "12"],
        "correct": 2
    },
    {
        "question": "Столица Германии?",
        "options": ["Мюнхен", "Берлин", "Гамбург"],
        "correct": 1
    },
    {
        "question": "Кто написал 'Ревизора'?",
        "options": ["Гоголь", "Чехов", "Тургенев"],
        "correct": 0
    },
    {
        "question": "Самый маленький материк?",
        "options": ["Австралия", "Евразия", "Антарктида"],
        "correct": 0
    },
    {
        "question": "Сколько секунд в минуте?",
        "options": ["50", "60", "70"],
        "correct": 1
    }
]

def get_random_questions(n: int = 10) -> list:
    return random.sample(QUESTIONS, min(n, len(QUESTIONS)))

def shuffle_options(question: dict) -> dict:
    import random
    options = question["options"].copy()
    random.shuffle(options)

    correct_answer = question["options"][question["correct"]]
    new_correct_index = options.index(correct_answer)
    return {
        "question": question["question"],
        "options": options,
        "correct": new_correct_index
    }

def generate_test_variant() -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    rand_part = random.randint(1000, 9999)
    return f"TEST_{timestamp}_{rand_part}"