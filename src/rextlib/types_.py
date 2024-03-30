__all__ = ("CoroutineFunction",)

from typing import TypeAlias
from collections.abc import Callable, Coroutine


CoroutineFunction: TypeAlias = Callable[..., Coroutine]
