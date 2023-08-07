from Abstract import ConnectAPI
import os
import requests


class ConnectSuperJob(ConnectAPI):
    """
    Класс работы с API для сайта superjob.ru
    """

    def __init__(self):
        self.KEY_SJ = os.getenv('SJ_KEY')
        self.url = 'https://api.superjob.ru/2.0/vacancies/'

    def connecting(self):
        """
        Получение данных с сайта в формате json
        """

        headers = {"X-Api-App-Id": self.KEY_SJ}
        response = requests.get(self.url, headers=headers)
        return response.json()

    def get_vacations(self, find_key):
        """
        Получение вакансий из общего файла с данными в формате json
        """

        data_vacations = self.connecting()
        vacansions_list = []

        for vacansion in data_vacations['objects']:
            profession = vacansion.get('profession', '').lower()
            if find_key.lower() in profession:
                vacansions_list.append(vacansion)

        if not vacansions_list:
            return 'данные не найдены'

        return {'objects': vacansions_list}
