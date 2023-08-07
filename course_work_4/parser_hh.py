from Abstract import ConnectAPI
import requests


class ConnectHh(ConnectAPI):
    """
    Класс работы с API для сайта hh.ru
    """

    def connecting(self):
        pass

    def get_vacations(self, find_key):
        """
        Получаем список вакансий в формате json
        """

        url = f'https://api.hh.ru/vacancies?text={find_key}'
        response = requests.get(url)
        if response.status_code == 200:
            data_request = response.json()
            data_vacancies = data_request.get('items', [])
            if not data_vacancies:
                return 'Неверный запрос'
            return data_vacancies

        else:
            return response.status_code
