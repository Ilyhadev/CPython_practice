# Импортируем pi из m1
from .m1 import pi
from .m2 import __i

# Определяем, что будет доступно при import *
__all__ = ['pi', '__i']
