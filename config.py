import os

class Config(object):
    SECRET_KY = os.environ.get() or "Secret_String"