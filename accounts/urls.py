from django.urls import path
from .views import AccountView , LoginView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', AccountView.as_view()),
]
