from django.urls import path,include
from BookTicket.views import dashboard

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
]