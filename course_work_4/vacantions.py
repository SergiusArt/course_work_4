import requests
from bs4 import BeautifulSoup


class Vacantions:

    def __init__(self, name, url, salary, description, url_hh):
        """
        Иницаилизация атрибутов класса
        """

        self.name = name
        self.url = url
        self.salary = salary
        self.description = description
        self.url_hh = url_hh

    def format_salary(self):
        """
        Форматирование зарплаты в читабельный вид
        """

        formated_salary = ""
        if isinstance(self.salary, dict):
            salary_from = self.salary.get('from')
            salary_to = self.salary.get('to')
            salary_currency = self.salary.get('currency')
            salary_gross = None

            if salary_from and salary_to:
                formated_salary = f'от {salary_from} до {salary_to}, {salary_currency}'
            elif salary_from:
                formated_salary = f'от {salary_from}, {salary_currency}'
            elif salary_to:
                formated_salary = f'до {salary_to}, {salary_currency}'
            else:
                formated_salary = 'зарплата не указана'

        return formated_salary

    def formated_description(self):
        """
        Форматирование описания
        """

        if self.url_hh:
            response = requests.get(self.url_hh)
            data_description = response.json()
            description = data_description.get('description')

            if description:
                new_format = BeautifulSoup(description, 'html.parser')
                cleaned_text = new_format.get_text()
                return cleaned_text

        elif self.description:
            return self.description

        else:
            return "описание отсутствует"
