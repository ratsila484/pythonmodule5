#!/usr/bin/python3

from abc import ABC, abstractmethod
from typing import Any


class DataProcessor():
    def __init__(self) -> None:
        self.data: str = ""
    
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    @abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        pass


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.data: int | float | list[int | float] = 0
        self.is_validate: bool = False

    def validate(self, data: Any) -> bool:
        isNumeric: bool = False
        if data:
            try:
                int(data)
                float(data)
                isNumeric = True
            except ValueError:
                isNumeric = False
        elif len(data) >= 1:
            for number in data:
                if number.isdigit() or float(number):
                    isNumeric += True
                else:
                    isNumeric += False
        return isNumeric

    def ingest(self, data: Any) -> None:
        if not self.is_validate:
            if 
            raise 


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass
    
    def ingest(self, data: Any) -> None:
        pass


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        pass
    
    def ingest(self, data: Any) -> None:
        pass


if __name__ == "__main__":
    num = NumericProcessor()
    print(num.validate("42.6fdsdf"))
    num.ingest(42)