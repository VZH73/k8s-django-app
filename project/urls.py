from expenses.views import home, health, metrics
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('health/', health, name='health'),
    path('metrics/', metrics, name='metrics'),
]

