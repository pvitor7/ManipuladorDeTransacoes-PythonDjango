from django.urls import path
from .views import StoresView

urlpatterns = [
    path('stores/', StoresView.as_view()),
]
