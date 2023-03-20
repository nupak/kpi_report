from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import ReportListView, ReportDetailView

urlpatterns = [
    path('idefzero/',views.method_idef0, name="idefzero"),
    path('dragon/', views.method_dragon, name="dragon"),
    path('reports/', ReportListView.as_view(),name="reports"),
    path('reports/<int:pk>/', ReportDetailView.as_view(), name='report-detail'),
]


