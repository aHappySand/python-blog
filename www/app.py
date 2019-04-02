# -*- coding: utf-8 -*-
# __author__ = 'zjj'
# date：2019/3/27 20:42

import logging;logging.basicConfig(level=logging.INFO)

import os, json, time
from datetime import datetime

from aiohttp import web

import aiomysql

async def index(request):
    return web.Response(body=b'<h1>awesome</h1>')



app = web.Application()
app.add_routes([web.get('/', index)])

web.run_app(app, host='127.0.0.1', port=8000)