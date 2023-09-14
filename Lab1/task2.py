import csv
import os


path = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


class Answers:
    """Класс ответов полльзователя (имя и его ответы)"""
    def __init__(self, person=None, answers=None):
        self.person = person
        self.answers = answers
    
    def __str__(self):
        return "".join(map(lambda x: "1" if x == "Да" else "0", self.answers))
    

def create_ankets(data) -> list[Answers]:
    """Возвращает анкеты"""
    ankets = []
    for i in data:
        _, person, *answers = i
        ankets.append(Answers(person=person, answers=answers))
    return ankets


def get_questions_and_answers(filename: str) -> (list[str], list[Answers]):
    """Получение данных из csv-таблицы с ответами"""
    with open(os.path.join(path, filename), encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        _, _, *fieldnames = next(reader)
        return fieldnames, create_ankets(list(reader))


def check_anket(anket: Answers, answer: str, qnumber: int) -> bool:
    return anket.answers[qnumber] == answer


def guessing_game(questions: list[str], ankets: list[Answers]):
    for x, i in enumerate(questions):
        ans = input(f"{i}: ").lower().capitalize()
        ankets = [i for i in ankets if check_anket(i, ans, x)]
        if len(ankets) == 1:
            print(f"Вы - {ankets[0].person}")
            return
        elif len(ankets) == 0:
            print("Такого человека нет!")
            return


if __name__ == "__main__":
    guessing_game(*get_questions_and_answers("opros.csv"))