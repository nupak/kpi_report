from enum import Enum

from kpi.meth_results import Idef0Result, DragonResult


class idef0:
    """Cвязь между данными поля input_data класса Report и их названия,
     для повышения понимания формул """
    count = 8
    Pur = "data0"
    Pexz= "data1"
    Pra = "data2"
    Pkp = "data3"
    CP = "data4"
    R = "data5"
    Pvux = "data6"
    Preg = "data7"

    @staticmethod
    def calculate(data):
        slognost = data[idef0.Pur] / data[idef0.Pexz]
        procesnost = data[idef0.Pra] / data[idef0.Pkp]
        control = data[idef0.CP] / data[idef0.Pkp]
        resurcoemk = data[idef0.R] / data[idef0.Pvux]
        regulir = data[idef0.Preg] / data[idef0.Pkp]

        result = {
                "Сложность": round(slognost, 2),
                "Процессность": round(procesnost, 2),
                "Контролируемость": round(control, 2),
                "Ресурсоёмкость": round(resurcoemk, 2),
                "Регулируемость": round(regulir, 2),
                }
        return result



class dragon:
    count = 9
    CP = "data0"
    Tz = "data1"
    Tp = "data2"
    Pe = "data3"
    Preg = "data4"
    Poz = "data5"
    Ppz = "data6"
    Phe = "data7"
    Pv = "data8"

    @staticmethod
    def calculate(data):
        dlitelnost = data[dragon.Tz] / data[dragon.Tp]
        regulir = data[dragon.Preg] / data[dragon.Pe]
        control = data[dragon.CP] / data[dragon.Pe]
        kahest = data[dragon.Poz] / data[dragon.Ppz]
        pribuln = data[dragon.Phe] / data[dragon.Pv]

        result = {
            "Сложность": round(dlitelnost, 2),
            "Процессность": round(regulir, 2),
            "Контролируемость": round(control, 2),
            "Ресурсоёмкость": round(kahest, 2),
            "Регулируемость": round(pribuln, 2),
        }
        return result


def calculate_par(data):
    """Рассчитывает словарь с {названием:значение, ..} рассчитанных пареметров
    по введному словарю {data0:1, ..}"""
    if len(data) == idef0.count:
        return idef0.calculate(data)
    elif len(data) == dragon.count:
        return dragon.calculate(data)


class ReportDetailWidget:
    """Класс для передачит списка объектов в шаблон"""
    def __init__(self, text, calculated_data):
        self.text = text
        self.calculated_data = calculated_data


def get_results_row_list(report):
    row_list = []
    for key, value in report.method_results.items():
        row = ReportDetailWidget(text=key, calculated_data=value)
        row_list.append(row)

    if report.method == "Дракон":
        return paste_dragon_result(row_list)
    else:
        return paste_idef0_result(row_list)


def paste_idef0_result(row_list):
    """Анализ рассчитанных параметров и подстановка выводов"""
    for i in range(len(row_list)):
        f = getattr(Idef0Result, f"get_{i}")
        text = f(row_list[i].calculated_data)
        row_list[i].result = text
    return row_list


def paste_dragon_result(row_list):
    """Анализ рассчитанных параметров и подстановка выводов"""
    for i in range(len(row_list)):
        f = getattr(DragonResult, f"get_{i}")
        text = f(row_list[i].calculated_data)
        row_list[i].result = text
    return row_list


