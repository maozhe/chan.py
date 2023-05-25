from sanic import Sanic
from sanic.response import text
from sanic.response import html
from sanic.response import file
import os


class Server():

    imgPath = ""

    app = Sanic("MyHelloWorldApp")

    def __init__(self):
        self.app.static('/static', '/')

    @app.get("/")
    async def hello_world(request):
        file_path = os.path.join(os.path.sep, '000636.png')
        print(file_path)
        return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><img src="'+file_path+'"></img>')


    def runWeb(self):
        self.app.run(host="0.0.0.0", port=5000)



