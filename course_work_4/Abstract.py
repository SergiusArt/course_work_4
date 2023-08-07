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


class JobSaver(ABC):
    """
    Ищет вакансию, добавляет или удаляет
    """

    @abstractmethod
    def find_vacation(self, key):
        pass

    @abstractmethod
    def add_vacation(self, job):
        pass

    @abstractmethod
    def del_vacation(self, job):
        pass
