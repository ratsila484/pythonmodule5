#!/usr/env/bin/python3

import abc
from typing import Any


def check_is_int(data: Any) -> bool:
    try:
        int(data)
        return True
    except ValueError:
        return False


def check_is_float(data: Any) -> bool:
    try:
        float(data)
        return True
    except ValueError:
        return False


def check_is_list(data: Any) -> bool:
    try:
        len(data)
        return True
    except Exception:
        return False


class NotValidateData(Exception):
    def __init__(self, *args):
        super().__init__(*args)


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self.data: str = ""
        self.use_validate: bool = False
    
    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        self.use_validate = True
        is_valid: bool = False
        if check_is_list(data):
            for number in data:
                try:
                    number = str(number)
                    int(number)
                    float(number)
                    is_valid = True
                except ValueError:
                    is_valid = False
        else:
            data = str(data)
            if check_is_int(data) or check_is_float(data):
                is_valid = True
            else:
                is_valid = False
        return is_valid


    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass
    
    def output(self, data: Any) -> tuple[int, str]:
        if (check_is_list(data)):
            print(f"Extracting {len(data)} values")
            for i in range(data):
                print(f"Numeric value {i}: {data[i]}")
        else:
            print(f"Extracting {data}")
            print(f"Numeric value: {data}")


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()
    
    def validate(self, data):
        return super().validate(data)

    def ingest(self, data):
        if not self.use_validate:
            raise NotValidateData("Improper numeric data")
        else:
            self.data = data


if __name__ == "__main__":
    print("===  Code Nexus - Data Processor ===\n")
    try:
        print("Testing Numeric Processor...")
        num1 = NumericProcessor()
        num2 = NumericProcessor()
        print(f"Trying to validate input '42': {num1.validate(42)}")
        print(f"Trying to validate input 'Hello': {num1.validate('Hello')}")
        print(f"Test invalid ingestion of string 'foo' without prior validation:")
        num2.ingest('foo')
        num3 = NumericProcessor()
        data = [1,2,3,4,5]
        num3.validate(data)
        num3.ingest(data)
        num3.output(data)
    except Exception as ex:
        print(f"Got exception: {ex}")
