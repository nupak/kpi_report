from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, ListView

from kpi.forms import ReportIdefo0Form, ReportDragonForm
from kpi.models import Report

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
class RowView:
    def __init__(self,id,text):
        self.id = id
        self.text = text
        self.input = ""


def put_input_data(method, cleaned_data):
    return cleaned_data


def get_row_list(data):
    row_list = []
    i = 0
    for text in data.keys():
        pole = RowView(id=i, text=text)
        row_list.append(pole)
        i += 1
    return row_list

def method_dragon(request):

    if not request.user.is_authenticated:
        return redirect("home")

    context = {}
    context["row_list"] = get_row_list(data_dragon)

    if request.POST:
        form = ReportDragonForm(request.POST)
        if form.is_valid():
            method = "Дракон"
            data = put_input_data(method=method, cleaned_data=form.cleaned_data)
            user = request.user
            report = Report(create_by=user, method=method, input_data=data)
            report.save()
            return redirect("report")
        else:
            context["dragon_form"] = form
    else:
        form = ReportDragonForm()
        context['dragon_form'] = form

    return render(request, "kpi/dragon.html", context)


def method_idef0(request):

    if not request.user.is_authenticated:
        return redirect("home")

    context = {}
    context["row_list"] = get_row_list(data_idefo)

    if request.POST:
        form = ReportIdefo0Form(request.POST)
        if form.is_valid():
            print("VALID!")
            method = "IDEF0"
            data = put_input_data(method=method, cleaned_data=form.cleaned_data)
            user = request.user

            report = Report(create_by=user, method=method, input_data=data)
            report.save()
        else:
            context["idef0_form"] = form
    else:
        form = ReportIdefo0Form()
        print(form)
        context['idef0_form'] = form

    return render(request, "kpi/idef0.html", context)

class ReportListView(ListView):
    queryset = Report.objects.all()

class ReportDetailView(DetailView):

    queryset = Report.objects.all()

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj