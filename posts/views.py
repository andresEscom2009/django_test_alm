from django.shortcuts import render
from django.views.generic.base import View
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
class HelloWorld(View):
    def get(self, request):
        data = {
            "name": "Andres Leon Martinez",
            "years": 32,
            "codes": ["Kotlin", "Java", "Dart"]
        }
        return render(request, "hello_world.html", context=data)

