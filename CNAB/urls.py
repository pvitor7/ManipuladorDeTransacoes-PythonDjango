"""CNAB URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (SpectacularAPIView, SpectacularSwaggerSplitView, SpectacularRedocView)

####################################################################################################

from drf_spectacular.utils import extend_schema, OpenApiParameter
from drf_spectacular.types import OpenApiTypes
from rest_framework.views import APIView
from Transactions.serializers import TransactionSerializer
from Transactions.models import Transaction
...



class TransacoesView(APIView):
    
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    @extend_schema(
        operation_id = 'transaction_post', #(1)
        parameters=[ #(2)
          TransactionSerializer,
          OpenApiParameter("pk", OpenApiTypes.UUID, OpenApiParameter.PATH),
          OpenApiParameter("queryparam1", OpenApiTypes.UUID, OpenApiParameter.QUERY),
        ],
        request=TransactionSerializer, #(3)
        responses={201: TransactionSerializer}, #(4)
        description = 'Rota para upload de transações', #(5)
        summary = 'Upload de transações', #(6)
        deprecated = True, #(7)
        tags = ['Upload de transações'], #(8)
        exclude = True, #(9)
    )
    
    def check_permissions(self, request):
        return super().check_permissions(request)
        
####################################################################################################

urlpatterns = [
    path('teste/', TransacoesView.as_view()),
]


urlpatterns = [
    path('admin/', admin.site.urls),
    path('teste/', TransacoesView.as_view()),
    path('api/', include('movements.urls')),
    path('api/', include('Store.urls')),
    path('api/', include('Transactions.urls')),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger-doc/', SpectacularSwaggerSplitView.as_view(url_name='schema')),
]