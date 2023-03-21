from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import DetailView, ListView

from kpi.forms import ReportIdefo0Form, ReportDragonForm
from kpi.models import Report

from kpi import bisness_logic

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


#TODO Выкинуть нахуй отсюда
def get_row_list(data):
    row_list = []
    i = 0
    for text in data.keys():
        pole = bisness_logic.RowView(id = i, text=text)
        row_list.append(pole)
        i += 1
    return row_list


def method_dragon(request):
    """Обработчик метода дракона, который после проверки данных перенаправляет на страницу с результатом"""
    if not request.user.is_authenticated:
        return redirect("home")

    context = {}
    context["row_list"] = get_row_list(data_dragon)

    if request.POST:
        form = ReportDragonForm(request.POST)
        for f in form:
            print(f)
        if form.is_valid():
            print("VALID!")
            method = "Дракон"
            user = request.user
            data = form.cleaned_data
            #calculated_param = bisness_logic.calculate_par(data)
            report = Report(create_by=user, method=method, input_data=data)
            report.save()
            return redirect(f"/reports/{report.id}/")
        else:
            context["dragon_form"] = form
    else:
        form = ReportDragonForm()
        context['dragon_form'] = form

    return render(request, "kpi/dragon.html", context)


def method_idef0(request):
    """Обработчик метода IDEF0, который после проверки данных перенаправляет на страницу с результатом"""
    if not request.user.is_authenticated:
        return redirect("home")

    context = {}
    context["row_list"] = get_row_list(data_idefo)

    if request.POST:
        form = ReportIdefo0Form(request.POST)
        if form.is_valid():
            print("VALID!")
            method = "IDEF0"
            user = request.user
            data = form.cleaned_data
            #calculated_param = bisness_logic.calculate_par(data) #Получает список из рассчитанных значений
            report = Report(create_by=user, method=method, input_data=data)
            report.save()
            return redirect(f"/reports/{report.id}/")
        else:
            context["idef0_form"] = form
    else:
        form = ReportIdefo0Form()
        context['idef0_form'] = form

    return render(request, "kpi/idef0.html", context)


class ReportListView(LoginRequiredMixin, ListView):
    """Контроллер отображения cписка всех отчетов
    LoginRequiredMixin дл запрета доступа без авторизации"""
    #login_url = "//"
    queryset = Report.objects.all()



class ReportDetailView(LoginRequiredMixin, DetailView):
    """Контроллер отображения одного отчета
    LoginRequiredMixin дл запрета доступа без авторизации"""
    queryset = Report.objects.all()
    #login_url = "//"


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        #context['row_list'] = context["report"].calculated_data
        #TODO это оооченб полезно будет! context["report"].id
        return context

    def get_object(self):
        obj = super().get_object()
        obj.save()
        return obj
