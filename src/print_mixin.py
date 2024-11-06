from typing import Any


class PrintMixin:
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        class_name = self.__class__.__name__
        params = ", ".join(repr(arg) for arg in args)  # Используем repr для корректного отображения
        print(f"Создан объект: {class_name}({params})")
