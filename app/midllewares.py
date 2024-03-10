from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Callable, Dict, Awaitable


class TestMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        print("Действие до обработчика")
        result = await handler(event, data)
        print("Действия после обработчика")
        return result
