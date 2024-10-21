__title__ = "durakonline.py"
__author__ = "Zakovskiy"
__license__ = "MIT"
__copyright__ = "Copyright 2021-2022 Zakovskiy"
__version__ = "3.4.1"

from .durakonline import Client
from .authorization import Authorization
from .game import Game
from .friend import Friend
from .socket_listener import SocketListener

from .utils import objects

from requests import get
from json import loads