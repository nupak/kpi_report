class DragonResult:

    text = {
        "Длительность":
            {
            "good" : "Значение kдл≤0,3 означает, что бизнес-процесс недлительный и время, затраченное на его выполнение является минимальным, тем самым показывая эффективное выполнение процесса.  ",
            "bad" : "Если допустимое значение 0,3 превышается, то длительность считается плохой, т.к. время проведения бизнес-процесса увеличивается, это может оказывать влияние на эффективность других процессов.  "
            },
        "Регулируемость":
            {
            "good" : "Высокий уровень регулируемости бизнес-процесса",
            "bad" : "Уровень регулируемости бизнес-процесса снижается в случае, когда значение данного коэффициента kрег<1. "
            },
        "Контролируемость":
            {
            "good" : "Бизнес-процесс является контролируемым.",
            "bad" : "Параметр kотв<0,3 бизнес-процесс характеризуется пониженной степенью контролируемости."
            },
        "Качество":
            {
            "good" : "При значении kкч⩾0,7, считается, что бизнес-процесс качественный",
            "bad" : "Значение меньше 0,7 – параметр считается проблемным, так как результат бизнес-процесса не выполняется."
            },
        "Прибыльность":
            {
            "good" : "В случае значения kпр>0 бизнес-процесс характеризуется как прибыльный. ",
            "bad" : "Бизнес-процесс является убыточным"
            },
    }
    words = list(text.keys())

    @staticmethod
    def get_0(value):
        print("вал", value)
        if value <=0.3:
            return DragonResult.text[DragonResult.words[0]]['good']
        else:
            return DragonResult.text[DragonResult.words[0]]['bad']


    @staticmethod
    def get_1(value):
        if value >= 1:
            return DragonResult.text[DragonResult.words[1]]['good']
        else:
            return DragonResult.text[DragonResult.words[1]]['bad']

    @staticmethod
    def get_2(value):
        if value >= 0.3:
            return DragonResult.text[DragonResult.words[2]]['good']
        else:
            return DragonResult.text[DragonResult.words[2]]['bad']

    @staticmethod
    def get_3(value):
        if value >= 0.7:
            return DragonResult.text[DragonResult.words[3]]['good']
        else:
            return DragonResult.text[DragonResult.words[3]]['bad']

    @staticmethod
    def get_4(value):
        if value > 0:
            return DragonResult.text[DragonResult.words[4]]['good']
        else:
            return DragonResult.text[DragonResult.words[4]]['bad']



class Idef0Result:

    text = {
        "Сложность":
            {
            "good" : "Бизнес-процесс характеризуется как сложный",
            "bad" : "Бизнес-процесс считается не сложным"
            },
        "Процессность":
            {
            "good" : "Бизнес-процесс характеризуется как процессный",
            "bad" : "Характеризует модель бизнес-процессов как не процессную, а проблемную, т. к. число «разрывов» в классах бизнес-процесса превысило допустимый уровень нормы"
            },
        "Контролируемость":
            {
            "good" : "Бизнес-процесс является контролируемым.",
            "bad" : "Бизнес-процесс характеризуется пониженной степенью контролируемости."
            },
        "Ресурсоёмкость":
            {
            "good" : "Меньшее значение данного коэффициента (низкий уровень ресурсоемкости) характеризует повышение эффективности использования ресурсов в бизнес-процессе",
            "bad" : "Низкая эффективность использования ресурсов в бизнес-процессе"
            },
        "Регулируемость":
            {
            "good" : "Высокий уровень регулируемости бизнес-процесса",
            "bad" : "Низкий уровень регулируемости бизнес-процесса"
            },
    }
    words = list(text.keys())

    @staticmethod
    def get_0(value):
        if value <= 0.66:
            return Idef0Result.text[Idef0Result.words[0]]['good']
        else:
            return Idef0Result.text[Idef0Result.words[0]]['bad']


    @staticmethod
    def get_1(value):
        if value < 1:
            return Idef0Result.text[Idef0Result.words[1]]['good']
        else:
            return Idef0Result.text[Idef0Result.words[1]]['bad']

    @staticmethod
    def get_2(value):
        if value == 1:
            return Idef0Result.text[Idef0Result.words[2]]['good']
        else:
            return Idef0Result.text[Idef0Result.words[2]]['bad']

    @staticmethod
    def get_3(value):
        if value < 1:
            return Idef0Result.text[Idef0Result.words[3]]['good']
        else:
            return Idef0Result.text[Idef0Result.words[3]]['bad']

    @staticmethod
    def get_4(value):
        if value >= 1:
            return Idef0Result.text[Idef0Result.words[4]]['good']
        else:
            return Idef0Result.text[Idef0Result.words[4]]['bad']