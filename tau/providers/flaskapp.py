from .abstract import AbstractProvider

from flask import Flask


class FlaskProvider(AbstractProvider, Flask):
    def __init__(self):
        super(ClickProvider, self).__init__()
