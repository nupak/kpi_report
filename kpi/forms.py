from django import forms

from kpi.models import Report


class ReportIdefo0Form(forms.Form):
    data0 = forms.IntegerField(required=True)
    data1 = forms.IntegerField(required=True)
    data2 = forms.IntegerField(required=True)
    data3 = forms.IntegerField(required=True)
    data4 = forms.IntegerField(required=True)
    data5 = forms.IntegerField(required=True)
    data6 = forms.IntegerField(required=True)
    data7 = forms.IntegerField(required=True)

class ReportDragonForm(forms.Form):
    data0 = forms.IntegerField(required=True)
    data1 = forms.IntegerField(required=True)
    data2 = forms.IntegerField(required=True)
    data3 = forms.IntegerField(required=True)
    data4 = forms.IntegerField(required=True)
    data5 = forms.IntegerField(required=True)
    data6 = forms.IntegerField(required=True)
    data7 = forms.IntegerField(required=True)
    data8 = forms.IntegerField(required=True)
