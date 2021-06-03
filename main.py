import fastapi
import uvicorn

from views import home


api = fastapi.FastAPI()


def configure(*routers):
    for router in list(routers):
        api.include_router(router=router)


configure(home.router)
if __name__ == '__main__':
    uvicorn.run(app=api, host='127.0.0.1', port=8080)
