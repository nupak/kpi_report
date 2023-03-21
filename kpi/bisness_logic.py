from enum import Enum

class idefo(Enum):
    """Cвязь между данными поля input_data класса Report и их названия,
     для повышения понимания формул """
    count = 8 #Количество параметров для рассчет  IDEF0
    Pur = "data0"
    Pexz= "data1"
    Pra = "data2"
    Pkp = "data3"
    CP = "data4"
    R = "data5"
    Pvux = "data6"
    Preg = "data7"


class dragon(Enum):
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


normail_idef0_coeff = {
    "Сложность": 0.66,
    "Процессность": 1,
    "Контролируемость":1,
    "Ресурсоёмкость":1,
    "Регулируемость":1
}


class RowView:
    def __init__(self, id, text):
        self.text = text
        self.id = id

def calc_idef0(data):
    slognost = data[idefo.Pur] / data[idefo.Pexz]
    procesnost = data[idefo.Pra] / data[idefo.Pkp]
    control = data[idefo.CP] / data[idefo.Pkp]
    resurcoemk = data[idefo.R] / data[idefo.Pvux]
    regulir = data[idefo.Preg] / data[idefo.Pkp]
    return [slognost, procesnost, control, resurcoemk, regulir]


def calc_dragon(data):
    dlitelnost = data[dragon.Tz] / data[dragon.Tp]
    regulir = data[dragon.Preg] / data[dragon.Pe]
    control = data[dragon.CP] / data[dragon.Pe]
    kahest = data[dragon.Poz] / data[dragon.Ppz]
    pribuln = data[dragon.Phe] / data[dragon.Pv]
    return [dlitelnost, regulir, control, kahest, pribuln]


def calculate_par(data):
    if len(data) == idefo.count:
        return calc_idef0(data)
    elif len(data) == dragon.count:
        return calc_dragon(data)
