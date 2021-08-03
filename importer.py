from __future__ import annotations

import importlib.util
import inspect
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from types import ModuleType


# https://docs.python.org/3/library/importlib.html#importing-a-source-file-directly
def import_module(module_name: str, file_path: str) -> ModuleType:
    spec = importlib.util.spec_from_file_location(module_name, location=file_path)
    if spec is None:
        raise ValueError(
            f"Failed to get spec for module {module_name} at path {file_path}"
        )
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    if spec.loader is None:
        raise ValueError(
            f"Spec has no loader for module {module_name} at path {file_path}"
        )
    spec.loader.exec_module(module)  # type: ignore # ???
    return module


def xxx(module: ModuleType) -> None:
    ret = {}
    for name, value in inspect.getmembers(module):
        if inspect.isclass(value):
            ret[name] = {
                "doc": value.__doc__,
                "name": value.__name__,
                "qualname": value.__qualname__,
                "module": value.__module__,
            }
            # TODO: methods
        elif inspect.ismethod(value):
            ret[name] = {
                "doc": value.__doc__,
                "name": value.__name__,
                "qualname": value.__qualname__,
                "module": value.__module__,
            }
        elif inspect.isfunction(value):
            ret[name] = {
                "doc": value.__doc__,
                "name": value.__name__,
                "qualname": value.__qualname__,
                "module": value.__module__,
                "defaults": value.__defaults__,
                "kwdefaults": value.__kwdefaults__,
                "annotations": value.__annotations__,
            }
