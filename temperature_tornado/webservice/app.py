import tornado.ioloop

from handlers import KelvinHandler, FahrenheitHandler, RankineHandler, CelsiusHandler


def make_app():
    return tornado.web.Application([
        (r"/convert/kelvin/(-?\d*\.?\d+?)/", KelvinHandler),
        (r"/convert/fahrenheit/(-?\d*\.?\d+?)/", FahrenheitHandler),
        (r"/convert/rankine/(-?\d*\.?\d+?)/", RankineHandler),
        (r"/convert/celsius/(-?\d*\.?\d+?)/", CelsiusHandler)
    ])

if __name__ == '__main__':
    print ('Running server on localhost...')
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
