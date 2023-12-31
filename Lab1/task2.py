import csv #для чтения гугл-дока
import os #для корректного нахождения пути до файла

path = os.path.realpath(os.path.dirname(__file__)) #real_path заменяет символическую ссылку на каноничную

def create_ankets(data) -> dict[str, list[int]]:
    """Возвращает анкеты"""
    ankets = {}
    for i in data: #пробегаемся по строкам data
        _, person, *answers = i #помещаем в переменные fio и ответы человека из i
        '''добавляем в список ankets fio человека и его ответы в формате 1/0'''
        ankets[person] = [1 if x == "Да" else 0 for x in answers]
    return ankets


def get_questions_and_answers(filename: str) -> (list[str], list[dict[str, list[int]]]):
    """Получение данных из csv-таблицы с ответами"""
    with open(os.path.join(path, filename), encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=",")
        _, _, *fieldnames = next(reader) #сохраняем первую строчку (вопросы)
        '''#возвращаем fieldnames (вопросы) и вызываем функцию create_ankets 
    для создания анкет из списка, сформированного на основе файла csv'''
        return fieldnames, create_ankets(list(reader))

def create_tree(qnumber: int, persons: dict) -> str | tuple:
    """Рекурсивная функция, создающая бинарное дерево"""
    if not persons: #==если пусто
        return "Извините, я вас не знаю!" + '\n'*2 + 'game over.'
    if len(persons) == 1:
        return f"Вы - {list(persons.keys())[0]}" + '\n'*2 + 'game over.'
    yes_persons = {}
    no_persons = {}
    for person, answers in persons.items(): #поочередно берем Person и помещаем его в один из словарей в зависимости от ответа на текущий вопрос
        if answers[qnumber] == 1:
            yes_persons[person] = answers
        else:
            no_persons[person] = answers
    return create_tree(qnumber + 1, no_persons), create_tree(qnumber + 1, yes_persons)

def guessing_game(questions: list[str], tree: tuple):
    for q in questions: #пробегаемся по вопросам
        ans = input(f"{q}: ") #выводим текущий вопрос в консоль(?) для пользователя и получаем ответ
        '''с помощью тернарного оператора преобразуем ответ в 1 - да либо 0 - нет'''
        int_ans = 1 if ans.lower().capitalize() in ("Да", "Yes", "Y") else 0
        tree = tree[int_ans]
        if isinstance(tree, str): #относится ли tree к классу str
            print(tree) #если да, то игра заканчивается, если нет, то игра продолжается (и эта строчка не отрабатывает)
            return
        

if __name__ == "__main__":
    print('the game starts...' + '\n')
    fields, persons = get_questions_and_answers("opros.csv")
    tree = create_tree(0, persons)
    guessing_game(fields, tree)