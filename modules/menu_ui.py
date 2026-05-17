import datetime

def print_header() -> None:
    print("="*40)
    print("  Лингвистический анализатор v1.0")
    print(f"  Запуск: {datetime.datetime.now().strftime('%H:%M:%S')}")
    print("="*40)

def get_user_input() -> str:
    return input("\n Введите текст для анализа: ").strip()

def format_results(freq: dict, sentences: int) -> None:
    print("\n  РЕЗУЛЬТАТЫ:")
    print(f" • Предложений: {sentences}")
    print(" • Топ-5 слов:")
    for word, count in list(freq.items())[:5]:
        print(f"    {word}: {count}")
