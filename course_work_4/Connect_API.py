from abc import ABC, abstractmethod


class ConnectAPI(ABC):
    """
    Класс работы с API.
    Модуль подключения к API с помощью ключей
    Модуль получения данных о вакансиях
    """

    @abstractmethod
    def connecting(self):
        """
        Модуль подключения к API с помощью ключей
        """
        pass

    @abstractmethod
    def get_vacations(self, find_key):
        """
        Модуль получения данных о вакансиях
        """

        pass


