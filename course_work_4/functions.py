import json

from parser_hh import ConnectHh
from parser_sj import ConnectSuperJob
from vacantions import Vacantions
from typing import List


def vacantions_hh(find_key):
    """
    Объект с вакансиями hh.ru
    """

    vacantions = ConnectHh()
    vacantions_data = vacantions.get_vacations(find_key)

    vacantions_list = []

    for vacantion in vacantions_data:
        title = vacantion.get('name')
        url = vacantion.get('alternate_url')
        salary = vacantion.get('salary')
        description = vacantion.get('description')
        url_hh = vacantion.get('url')
        job = Vacantions(title, url, salary, description, url_hh)

        vacantions_list.append(job)

    return vacantions_list


def vacantions_sj(find_key):
    """
    Объект с вакансиями superjob.ru
    """

    vacantions = ConnectSuperJob()
    vacantions_data = vacantions.get_vacations(find_key)

    vacantions_list = []

    for vacantion in vacantions_data['objects']:
        title = vacantion['profession']
        url = vacantion['link']
        salary = {
            'from': vacantion['payment_from'],
            'to': vacantion['payment_to'],
            'currency': vacantion['currency'],
            'gross': None
        }
        if 'client' in vacantion and 'description' in vacantion['client']:
            description = vacantion['client']['description']
        else:
            description = ""
        api_url = None

        job = Vacantions(title, url, salary, description, api_url)
        vacantions_list.append(job)

    return vacantions_list


def min_salary(vacantions: list, salary: int):
    """
    Вывод вакансий с минимальной указанной зарплатой
    """

    vacantions_list = []
    for vacantion in vacantions:
        salary_to, salary_from = vacantion.get_salary_info()
        if salary_from is not None and salary_from != '':
            salary_from = int(salary_from)
        salary_from = salary_from or 0

        if salary_from >= salary:
            vacantions_list.append(vacantion)

    return vacantions_list


def add_vacancies_to_json_file(file_name: str, vacancies_list: List) -> None:
    """
    Функция для добавления списка вакансий в JSON
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        data = [job.to_dict() for job in vacancies_list]
        json.dump(data, file, ensure_ascii=False, indent=2)
