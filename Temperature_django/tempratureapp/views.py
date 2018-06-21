# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

import json

from django.http import HttpResponse

# Create your views here.


def kelvin(request,temperature):
    temperature = float(temperature)
    far = float(((9.0 / 5.0) * (temperature - 273.15)) + 32.0)
    cel = float(temperature - 273.15)
    ran = float(temperature * 1.8)

    return HttpResponse(json.dumps({"fahrenheit": far, "celsius": cel, "rankine": ran}))

def fahrenheit(request,temperature):
    temperature = float(temperature)
    kel = float(((temperature - 32.0) * (5.0 / 9.0)) + 273.15)
    cel = float((temperature - 32.0) * (5.0 / 9.0))
    ran = float(temperature + 459.67)

    return HttpResponse(json.dumps({"kelvin": kel, "celsius": cel, "rankine": ran}))


def rankine(request,temperature):
    temperature = float(temperature)
    far = float(temperature - 459.67)
    cel = float((temperature / 1.8) - 273.15)
    kel = float(temperature / 1.8)

    return HttpResponse(json.dumps({"fahrenheit": far, "celsius": cel, "kelvin": kel}))


def celsius(request,temperature):
    temperature = float(temperature)
    far = float((temperature * (9.0 / 5.0)) + 32)
    kel = float(temperature + 273.15)
    ran = float((temperature * 1.8) + 491.67)

    return HttpResponse(json.dumps({"fahrenheit": far, "kelvin": kel, "rankine": ran}))
