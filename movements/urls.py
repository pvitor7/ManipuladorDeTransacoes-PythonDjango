from django.urls import path
from .views import MovementsView

urlpatterns = [
    path('movements/', MovementsView.as_view()),
]
