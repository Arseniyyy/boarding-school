from typing import Optional

import fastapi
from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from starlette.requests import Request, Receive
from fastapi.responses import StreamingResponse


directory = 'templates/appkit-landing-v1.2'
templates = Jinja2Templates(directory=directory)

router = fastapi.APIRouter()


@router.get('/', include_in_schema=False)
def root(req: Request):
    return templates.TemplateResponse(name='index.html', context={'request': req})


@router.get('/assets/plugins/bootstrap/css/bootstrap.min.css')
def bootstrap():
    file_like = open(f'{directory}/assets/plugins/bootstrap/css/bootstrap.min.css', mode='rb')
    return StreamingResponse(content=file_like, media_type='text/css')


@router.get('/assets/plugins/font-awesome/css/font-awesome.css')
def font_awesome():
    file_like = open(f'{directory}/assets/plugins/font-awesome/css/font-awesome.css', mode='rb')
    return StreamingResponse(content=file_like, media_type='text/css')


@router.get('/assets/css/styles.css')
def font_awesome():
    file_like = open(f'{directory}/assets/css/styles.css', mode='rb')
    return StreamingResponse(content=file_like, media_type='text/css')


@router.get('/assets/plugins/jquery-1.12.3.min.js')
def font_awesome():
    file_like = open(f'{directory}/assets/plugins/jquery-1.12.3.min.js', mode='rb')
    return StreamingResponse(content=file_like, media_type='text/javascript')


@router.get('/assets/js/main.js')
def font_awesome():
    file_like = open(f'{directory}/assets/js/main.js', mode='rb')
    return StreamingResponse(content=file_like, media_type='text/javascript')


@router.get('/assets/images/logo-icon.svg')
def font_awesome():
    file_like = open(f'{directory}/assets/images/logo-icon.svg', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/svg+xml')


# @router.get('/assets/images/imac.png')
# def font_awesome():
#     file_like = open(f'{directory}/assets/images/imac.png', mode='rb')
#     return StreamingResponse(content=file_like, media_type='image/png')


@router.get('/assets/images/figure-1.png')
def font_awesome():
    file_like = open(f'{directory}/assets/images/figure-1.png', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/png')


@router.get('/assets/images/figure-2.png')
def font_awesome():
    file_like = open(f'{directory}/assets/images/figure-2.png', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/png')


@router.get('/assets/images/figure-3.png')
def font_awesome():
    file_like = open(f'{directory}/assets/images/figure-3.png', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/png')


@router.get('/assets/images/Ann.jpg')
def font_awesome():
    file_like = open(f'{directory}/assets/images/Ann.jpg', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/jpg')


@router.get('/assets/images/Nikita.jpg')
def font_awesome():
    file_like = open(f'{directory}/assets/images/Nikita.jpg', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/jpg')


@router.get('/assets/images/Demid.jpg')
def font_awesome():
    file_like = open(f'{directory}/assets/images/Demid.jpg', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/jpg')


@router.get('/assets/images/Drozd.jpg')
def font_awesome():
    file_like = open(f'{directory}/assets/images/Drozd.jpg', mode='rb')
    return StreamingResponse(content=file_like, media_type='image/jpg')
