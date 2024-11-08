from typing import Any

import pytest
from pytest_mock import MockerFixture

from src.print_mixin import PrintMixin


def test_print_mixin_initialization(product3: Any) -> None:
    instance, mock_print = product3
    mock_print.assert_called_once()  # Проверяем, что print был вызван один раз
    # Проверяем, что вывод содержит нужные элементы
    assert "Создан объект:" in mock_print.call_args[0][0]
    assert "Xiaomi Redmi Note 11" in mock_print.call_args[0][0]
    assert "31000.0" in mock_print.call_args[0][0]
    assert "14" in mock_print.call_args[0][0]


def test_print_mixin_with_multiple_args(product3: Any) -> None:
    instance, mock_print = product3
    mock_print.assert_called_once()  # Проверяем, что print был вызван один раз
    # Проверяем, что вывод содержит нужные элементы
    assert "Создан объект:" in mock_print.call_args[0][0]
    assert "Xiaomi Redmi Note 11" in mock_print.call_args[0][0]
    assert "31000.0" in mock_print.call_args[0][0]
    assert "14" in mock_print.call_args[0][0]


def test_print_mixin_with_no_args(mocker: MockerFixture) -> None:
    mock_print = mocker.patch("builtins.print")

    class EmptyProduct(PrintMixin):
        def __init__(self) -> None:
            super().__init__()

    # Создаем объект без аргументов
    EmptyProduct()
    mock_print.assert_called_once()  # Проверяем, что print был вызван один раз
    assert mock_print.call_args[0][0] == "Создан объект: EmptyProduct()"


if __name__ == "__main__":
    pytest.main()
