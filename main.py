import fastapi
import uvicorn

from views import home


api = fastapi.FastAPI()


def configure(*routers):
    for router in list(routers):
        api.include_router(router=router)


configure(home.router)
