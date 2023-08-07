from parser_hh import ConnectHh
from parser_sj import ConnectSuperJob
from vacantions import Vacantions


# def hh_vacantions(find_key):
#     """
#     Формируем список вакансий - объектов
#     """

vacantions = ConnectHh()
find_key = "продавец"
vacantions_data = vacantions.get_vacations(find_key)

vacantions_list = []

for vacantion in vacantions_data:
    title = vacantion.get('name')
    url = vacantion.get('alternate_url')
    salary = vacantion.get('salary')
    description = vacantion.get('description')
    url_hh = vacantion.get('url')
    job = Vacantions(title, url, salary, description, url_hh)
    formated_salary = job.format_salary()
    farmated_description = job.formated_description()

    print(f'{job.name}, {job.url}, {formated_salary}, {farmated_description}, {job.url_hh}')

