from functions import vacantions_hh, vacantions_sj, min_salary, add_vacancies_to_json_file
import sys

PATH = 'data_vacantions.json'

user_site = input('Выберите сайт:\n1)hh.ru\n2)superjob.ru\n')

if user_site == "1":
    user_find_key = input('Введите запрос по ключевому слову: \n')
    list_vacantions = vacantions_hh(user_find_key)
elif user_site == "2":
    user_find_key = input('Введите запрос по ключевому слову: \n')
    list_vacantions = vacantions_sj(user_find_key)
else:
    print('Не верные данные')
    sys.exit()

user_sorted = input('Сортировать данные:\n1)По возрастанию\n2)По убыванию\n3)Показать зп не менее указанной суммы\n')

if user_sorted == "1":
    list_vacantions.sort()
    for item in list_vacantions:
        formated_salary = item.format_salary()
        formated_description = item.formated_description()
        print(f'{item.name}, {item.url}, {formated_salary}, {formated_description}, {item.url_hh}')
        add_vacancies_to_json_file(PATH, list_vacantions)

elif user_sorted == "2":
    list_vacantions.sort(reverse=True)
    for item in list_vacantions:
        formated_salary = item.format_salary()
        formated_description = item.formated_description()
        print(f'{item.name}, {item.url}, {formated_salary}, {formated_description}, {item.url_hh}')
        add_vacancies_to_json_file(PATH, list_vacantions)

elif user_sorted == "3":
    user_min_salary = int(input('Введите минимальную сумму зарплаты: '))
    desire = min_salary(list_vacantions, user_min_salary)
    if not desire:
        print("Таких вакансий нет")
        add_vacancies_to_json_file(PATH, list_vacantions)
    else:
        for item in desire:
            formated_salary = item.format_salary()
            formated_description = item.formated_description()
            print(f'{item.name}, {item.url}, {formated_salary}, {formated_description}, {item.url_hh}')
            add_vacancies_to_json_file(PATH, list_vacantions)

else:
    print("Не верный пункт")
