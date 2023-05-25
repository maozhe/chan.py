from sanic import Sanic
from sanic.response import text
from sanic.response import html
from sanic.response import file
from sanic import response

import os


imgPath = ""

app = Sanic("web")


app.static('/static', '/')

@app.route('/img')
async def hello_world(request):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    file_path = current_directory + '\\000636.png'
    print(file_path)
    return html('<!DOCTYPE html><html lang="en"><meta charset="UTF-8"><img src="/image.png"></img>')



@app.route('/image.png')
async def serve_image(request):
    current_directory = os.path.dirname(os.path.realpath(__file__))
    image_path = current_directory + '\\result\\img.png'
    return await response.file(image_path)

def runWeb():
    app.run(host="0.0.0.0", port=5000)



