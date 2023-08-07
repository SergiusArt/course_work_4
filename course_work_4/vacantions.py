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

    def valid_data(self):
        """
        Метод для валидации данных. Проверяет инициализирован ли класс
        """

        if not self.name or self.url or self.salary is None or not self.description:
            return False
        else:
            return True

    def get_salary_info(self):
        """
        Возвращает значения ключей зп от и до
        """

        if isinstance(self.salary, dict):
            salary_to = self.salary.get('to')
            salary_from = self.salary.get('from')
            return salary_to, salary_from

        else:
            return None, None

    def __le__(self, other):
        if isinstance(other, Vacantions):
            self_to_salary, self_from_salary = self.get_salary_info()
            other_to_salary, other_from_salary = other.get_salary_info()

            # преобразование строк в числа
            if self_from_salary is not None and self_from_salary != "":
                self_from_salary = int(self_from_salary)
            if self_to_salary is not None and self_to_salary != "":
                self_to_salary = int(self_to_salary)
            if other_from_salary is not None and other_from_salary != "":
                other_from_salary = int(other_from_salary)
            if other_to_salary is not None and other_to_salary != "":
                other_to_salary = int(other_to_salary)

            # если зарплата не указана
            if self_from_salary is None and self_to_salary is None:
                return True
            elif other_from_salary is None and other_to_salary is None:
                return False

            # отсутствует значение 'from', то оно равно 0
            self_from_salary = self_from_salary or 0
            other_from_salary = other_from_salary or 0

            # если поля 'from' и 'to' пустые
            if self_from_salary == 0 and self_to_salary == 0 and other_from_salary == 0 and other_to_salary == 0:
                return True

            # равенство зарплат
            if self_from_salary == other_from_salary and self_to_salary == other_to_salary:
                return "Зарплаты одинаковые"

            # сравнение зарплат
            if self_from_salary < other_from_salary:
                return True
            elif self_from_salary > other_from_salary:
                return False

            # если 'from' одинаковые - сравнение по значению 'to'
            if self_to_salary is None:
                return False
            elif other_to_salary is None:
                return True
            else:
                return self_to_salary <= other_to_salary

    def __lt__(self, other) -> bool:
        """
        Метод для сравнения вакансий по зарплате (меньше)
        """
        result = self.__le__(other)
        if result == "Зарплаты одинаковые":
            return False
        return result

    def __gt__(self, other) -> bool:
        """
        Метод для сравнения вакансий по зарплате (больше)
        """
        result = self.__le__(other)
        if result == "Зарплаты одинаковые":
            return False
        return not result

    def __ge__(self, other) -> bool:
        """
        Метод для сравнения вакансий по зарплате (больше или равно)
        """
        result = self.__le__(other)
        return result or (result == "Зарплаты одинаковые")

    def to_dict(self):
        """
        Преобразование объекта в словарь
        """

        dict_data = {
            "name": self.name,
            "url": self.url,
            "salary": self.salary,
            "description": self.formated_description(),
        }

        return dict_data
