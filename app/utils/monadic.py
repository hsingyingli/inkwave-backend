from collections import namedtuple
from typing import Awaitable, Callable, Union
from functools import wraps

from annotated_types import T

Success = namedtuple(
    "Success",
    ["is_succeeded", "is_failed", "result", "errors"],
    defaults=[True, False, None, None],
)

Fail = namedtuple(
    "Fail",
    ["is_succeeded", "is_failed", "result", "errors"],
    defaults=[False, True, None, None],
)


def async_monadic(func: Callable[..., Awaitable[T]]) -> Callable[..., Awaitable[Union[Success, Fail]]]:
    @wraps(func)
    async def wrap(*args, **kwargs) -> Union[Success, Fail]:
        try:
            result = await func(*args, **kwargs)
            if type(result) == Success or type(result) == Fail:
                return result
            return Success(result=result)
        except Exception as e:
            return Fail(errors=e)

    return wrap


def monadic(func: Callable) -> Callable[..., Union[Success, Fail]]:
    @wraps(func)
    def wrap(*args, **kwargs) -> Union[Success, Fail]:
        try:
            result = func(*args, **kwargs)
            if type(result) == Success or type(result) == Fail:
                return result
            return Success(result=result)
        except Exception as e:
            return Fail(errors=e)

    return wrap
