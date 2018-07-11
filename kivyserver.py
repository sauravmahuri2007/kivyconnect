#!venvserver/bin/python
# -*- coding: utf-8 -*-

from flask import Flask
from flask import request
from pyautogui import press, typewrite, hotkey

import time
app = Flask(__name__)


@app.route('/<text>')
def remote_input(text):
    time.sleep(2)
    press(text)
    return ''


if __name__ == '__main__':
    app.run(debug=True, host='::', port=10101)
