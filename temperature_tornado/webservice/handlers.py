import tornado.web
import json


class FahrenheitHandler(tornado.web.RequestHandler):
    """Handler to convert Farenheit to others."""

    def get(self, temperature):
        temperature = float(temperature)
        kel = float(((temperature - 32.0) * (5.0 / 9.0)) + 273.15)
        cel = float((temperature - 32.0) * (5.0 / 9.0))
        ran = float(temperature + 459.67)

        self.write(json.dumps({"kelvin": kel, "celsius": cel, "rankine": ran}))


class KelvinHandler(tornado.web.RequestHandler):
    """Handler to convert Kalvin to others."""

    def get(self, temperature):
        temperature = float(temperature)
        far = float(((9.0 / 5.0) * (temperature - 273.15)) + 32.0)
        cel = float(temperature - 273.15)
        ran = float(temperature * 1.8)

        self.write(json.dumps({"fahrenheit": far, "celsius": cel, "rankine": ran}))


class CelsiusHandler(tornado.web.RequestHandler):
    """Handler to convert Celcius to others."""

    def get(self, temperature):
        temperature = float(temperature)
        far = float((temperature * (9.0 / 5.0)) + 32)
        kel = float(temperature + 273.15)
        ran = float((temperature * 1.8) + 491.67)

        self.write(json.dumps({"fahrenheit": far, "kelvin": kel, "rankine": ran}))


class RankineHandler(tornado.web.RequestHandler):
    """Handler to convert Rankine to others."""

    def get(self, temperature):
        temperature = float(temperature)
        far = float(temperature - 459.67)
        cel = float((temperature / 1.8) - 273.15)
        kel = float(temperature / 1.8)

        self.write(json.dumps({"fahrenheit": far, "celsius": cel, "kelvin": kel}))


