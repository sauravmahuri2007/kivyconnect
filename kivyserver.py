#!venvserver/bin/python
# -*- coding: utf-8 -*-

from base64 import b64decode
from flask import Flask
from flask import request, Response
from flask.views import MethodView
from json import dumps
from pyautogui import press, typewrite, hotkey

import time
app = Flask(__name__)

DEV_MODE = False  # text will be printed after 3 seconds


class Home(MethodView):

    def get(self):
        return Response(response=dumps('Server is up!'), status=200, mimetype='application/json')


class RemoteConnect(MethodView):

    def get(self):
        return Response(response=dumps('Allowed Methods = [POST]'), status=405, mimetype='application/json')

    def post(self):
        if request.is_json:
            try:
                data_dict = request.get_json()
                text = b64decode(data_dict.get('text'))
                if DEV_MODE:
                    time.sleep(3)
                press(text)
                return Response(response=dumps(''), status=200, mimetype='application/json')
            except Exception as err:
                print(err)
        return Response(response=dumps('Invalid Request Data or Type'), status=400, mimetype='application/json')


app.add_url_rule('/', view_func=Home.as_view('home'), methods=['GET', ])
app.add_url_rule('/rc', view_func=RemoteConnect.as_view('remote_connect'), methods=['POST', 'GET', ])


if __name__ == '__main__':
    app.run(debug=True, host='::', port=10101)
