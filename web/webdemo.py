from sanic import Sanic
from sanic.response import text

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def hello_world(request):
    return text("Hello, world.222")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
