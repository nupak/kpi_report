from django.shortcuts import render

# Create your views here.
from kpi.models import report_view_idef0, report_view_dragon


def method_calculating(request):
    print(request.path)
    context = {}
    if request.path == "/idef0/":
        context["text_for_rows"] = report_view_idef0.text_for_rows
        context["row_number_list"] = report_view_idef0.row_number_list
        context["method_name"] = report_view_idef0.type

    elif request.path == "/dragon/":
        context["text_for_rows"] = report_view_dragon.text_for_rows
        context["row_number_list"] = report_view_dragon.row_number_list
        context["method_name"] = report_view_dragon.type
    print(context)
    if request.POST:
        pass
    return render(request, "kpi/methods.html", context)
