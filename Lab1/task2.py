import csv
import os


path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
    

def create_ankets(data) -> list[tuple[str, list[int]]]:
    """Возвращает анкеты"""
    ankets = []
    for i in data:
        _, person, *answers = i
        ankets.append((person, [1 if x == "Да" else 0 for x in answers]))
    return ankets


def get_questions_and_answers(filename: str) -> (list[str], list[tuple[str, list[int]]]):
    """Получение данных из csv-таблицы с ответами"""
    with open(os.path.join(path, filename), encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        _, _, *fieldnames = next(reader)
        return fieldnames, create_ankets(list(reader))


def guessing_game(questions: list[str], tree: tuple):
    for q in questions:
        ans = input(f"{q}: ")
        int_ans = 1 if ans.lower().capitalize() in ("Да", "Yes", "Y") else 0
        tree = tree[int_ans]
        if isinstance(tree, str):
            print(tree)
            return
        

def create_tree(qnumber: int, persons: list) -> str | tuple:
    """Рекурсивная функция, создающая бинарное дерево"""
    if not persons:
        return "Извините, я вас не знаю!"
    if len(persons) == 1:
        return f"Вы - {persons[0][0]}"
    yes_persons = []
    no_persons = []
    for person in persons:
        if person[1][qnumber] == 1:
            yes_persons.append(person)
        else:
            no_persons.append(person)
    return create_tree(qnumber + 1, no_persons), create_tree(qnumber + 1, yes_persons)


if __name__ == "__main__":
    fields, persons = get_questions_and_answers("opros.csv")
    tree = create_tree(0, persons)
    guessing_game(fields, tree)