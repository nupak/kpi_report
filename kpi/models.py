from django.contrib.auth.models import User
from django.db import models



class Report(models.Model):
    """Класс сохранения данных"""

    id = models.BigIntegerField(primary_key=True, blank=False, unique=True)
    data = models.DateField() #TODO is today.now
    create_by = User() #TODO oneto onefiled
    type = models.CharField(max_length=255)
    input_data = models.JSONField() #TODO Параметры введеные данные в формате словаря

data_dragon = {
    "Количество собственников": "",
    "Время выполнения бизнес-процесса (обработки одной заявки)": "",
    "Рабочее время": "",
    "Число экземпляров (действий) бизнес-процесса ": "",
    "Количество регламентной нормативной документации": "",
    "Количество обработанных заявок": "",
    "Количество поданных заявок": "",
    "Чистая прибыль": "",
    "Выручка": "",
}
data_idefo = {
    "Количество уровней бизнес-процессов": "",
    "Количество экземпляров бизнес-процессов": "",
    "Количество классов бизнес-процессов": "",
    "Число собственников бизнес-процессов": "",
    "Количество разрывов процессов в экземплярах бизнес-процессов": "",
    "Количество использованных ресурсов в бизнес-процессе": "",
    "Количество «выходов» в экземплярах бизнес-процессов": "",
    "Количество регламентирующей нормативной документации": "",
}


def get_numbers_list(n):
    return
class ReportView:
    def __init__(self, type):
        self.type = type
        if type == "IDEF0":
            self.data = data_idefo
            self.text_for_rows = list(data_idefo.keys())
        elif type == "Дракон":
            self.data = data_dragon
            self.text_for_rows = list(data_dragon.keys())
        self.row_number_list = [i for i in range(len(self.text_for_rows))] #Для вывода цифр на html

report_view_idef0 = ReportView("IDEF0")
report_view_dragon = ReportView("Дракон")