"""dating_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from django.urls import path
from .views import index, registration, LoginClient, logout_client, ListClientsApiView, other_client_page, DetailClientApiView


urlpatterns = [
    path('api/v1/clients_list', ListClientsApiView.as_view(), name='clients_list_api'),
    path('api/v1/client_detail/<int:id>', DetailClientApiView.as_view(), name='client_detail_api'),
    path('index/', index, name='index'),
    path('clients/create/', registration, name='registration'),
    path('login/', LoginClient.as_view(), name='login'),
    path('logout/', logout_client, name='logout'),
    path('clients/<int:id>/other_clients/<int:other_client_id>', other_client_page,
         name='other_client_detail')
]
