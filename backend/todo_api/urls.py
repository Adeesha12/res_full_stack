from .views import TodosView
from django.urls import path

urlpatterns = [
    path('basic/',TodosView.as_view())
]
