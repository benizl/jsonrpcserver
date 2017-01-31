from aiohttp import web
from jsonrpcserver.aio import methods

app = web.Application()

@methods.add
async def ping():
    return 'pong'

async def handle(request):
    request = await request.text()
    response = await methods.dispatch(request)
    return web.json_response(response)

app.router.add_post('/', handle)

if __name__ == '__main__':
    web.run_app(app, port=5000)
