from django.shortcuts import render
from django.http import JsonResponse
from .models import TestDB


def get_elements(request):
    elements = TestDB.objects.all()
    data = [{"name": element.test_name, "email": element.test_email}
            for element in elements]
    return JsonResponse(data, safe=False)
