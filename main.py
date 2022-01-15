import json
from os.path import isfile

QUESTION_FILE_PATH = 'questions.json'
RESULT_FILE_PATH = 'result.json'


def read_json():
    """
    Считываем файл
    :return:
    """
    with open(QUESTION_FILE_PATH, encoding='utf-8') as file:
        return json.load(file)


def draw_table(questions):
    """
    Рисуем таблицу
    :return:
    """
    for category_name in questions:
        ###
        list_number_question = []
        for number_question in questions[category_name].keys():  # Перебираем номера вопросов
            if questions[category_name][number_question]['asked'] is False:
                list_number_question.append(number_question)  # Добавляем номер вопроса в список
            else:
                list_number_question.append('   ')
        ###
        # number_question = '\t'.join(
        #     [
        #         number if questions[category_name][number]['asked'] is False else ' '
        #         for number in questions[category_name]
        #     ]
        # )
        if len(category_name) < 7:
            category_name = f'{category_name}\t\t'
        print(f'{category_name}\t{" ".join(list_number_question)}')


def start(questions):

    points = 0
    correct = 0
    incorrect = 0

    count_question = sum([len(item) for item in questions.values()])  # Считаем кол-во вопросов
    while count_question > 0:  # Подсчитать колво number_question
        draw_table(questions)

        enter_user = input('Enter question ')  # Получаем ввод от пользователя: название категории и номер вопроса
        if ' ' not in enter_user:
            print('Неправильный ввод')
            continue
        category_name, number_question = enter_user.strip().split(' ')
        category_name = category_name.capitalize()

        if category_name not in questions or number_question not in questions[category_name]:
            print("Error not category or number question")
            continue

        if questions[category_name][number_question]['asked'] is True:
            print('Этот вопрос был задан ранее')
            continue

        questions[category_name][number_question]['asked'] = True  # Помечаем отвеченный вопрос для удаления из таблицы

        count_question -= 1  # Уменьшаем кол-во итераций

        if category_name in questions and number_question in questions[category_name]:  # Если название категории есть в списке категорий и номер вопроса есть в списке вопросов

            hide_word = questions[category_name][number_question]['question']  # Находим скрытое слово
            correct_word = questions[category_name][number_question]['answer']  # Находим ответ

            response = input(f'Слово {hide_word} в переводе означает ')  # Получаем от пользователя ответ
        else:
            print('Question not found')
            continue

        if response == correct_word:  # Проверяем ответ
            points += int(number_question)  # Начисляем бонусы
            correct += 1  # Начисляем кол-во правильных ответов
            print(f'Верно, +{number_question}. Ваш счет = {points}')
        else:
            points -= int(number_question)  # Начисляем бонусы
            incorrect += 1  # Начисляем кол-во не правильных ответов
            print(f'Неверно, на самом деле – {correct_word}. –{number_question}. Ваш счет = {points}')

    write_result(points, correct, incorrect)
    print(f'У нас закончились вопросы!\n'
          f'\nВаш счет: {points}\n'
          f'Верных ответов: {correct}\n'
          f'Неверных ответов: {incorrect}')


def write_result(points, correct, incorrect):
    """
    Запись результатов в файл
    :return:
    """

    data_structure = {
        'points': points,
        'correct': correct,
        'inccorect': incorrect,
    }

    if isfile(RESULT_FILE_PATH):
        with open(RESULT_FILE_PATH) as file:
            data = json.load(file)
    else:
        data = []

    data.append(data_structure)

    with open(RESULT_FILE_PATH, 'w') as file:
        json.dump(data, file)


def main():
    questions = read_json()

    start(questions)



if __name__ == '__main__':
    main()
