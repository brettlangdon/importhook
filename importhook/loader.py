from importlib.abc import Loader
import sys

from .logger import logger
from .registry import registry
from .utils import get_module_name


class HookLoader(Loader):
    """
    Custom `importlib.abc.Loader` which ensures we call any registered hooks when a module is loaded.
    """
    __slots__ = ['loader']

    def __init__(self, loader):
        self.loader = loader

    def exec_module(self, module, *args, **kwargs):
        logger.debug(f'{self.__class__.__name__}.exec_module(module={module}, *args={args}, **kwargs={kwargs})')
        name = get_module_name(module)

        mod = self.loader.exec_module(module, *args, **kwargs)
        if mod is not None:
            module = mod

        # If we have a hook in the registry, then call it now
        if name in registry:
            mod = registry[name](module)
            if mod is not None:
                module = mod

        # If we have a global hook in the registry, then call it now
        if None in registry:
            mod = registry[None](module)
            if mod is not None:
                module = mod

        sys.modules[name] = module
