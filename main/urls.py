from django.urls import path

from main.apps import MainConfig

from .views import SubjectListView, SubjectDetailView, MaterialDetailView, SolutionDetailView

app_name = MainConfig.name

urlpatterns = [
    path('', SubjectListView.as_view(), name='main_page'),
    path('<slug:subject>/', SubjectDetailView.as_view(), name='subject'),
    path('<slug:subject>/<slug:material>/', MaterialDetailView.as_view(), name='material'),
    path('<slug:subject>/<slug:material>/<slug:solution>/', SolutionDetailView.as_view(), name='solution'),
]
