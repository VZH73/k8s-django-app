from django.http import HttpResponse
from django.urls import path


def home(_request):
    return HttpResponse('Hello from Django on Kubernetes')


urlpatterns = [
    path('', home),
]
