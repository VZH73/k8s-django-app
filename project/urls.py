from expenses.views import home, health
from django.urls import path


urlpatterns = [
    path('', home, name='home'),
    path('health/', health, name='health'),
]
]
