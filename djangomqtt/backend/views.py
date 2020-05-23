from django.shortcuts import render
from module import mqtt_function
# Create your views here.


def test(request):
    mqtt_function.mqtt_run()
    return render(request, 'test.html')
