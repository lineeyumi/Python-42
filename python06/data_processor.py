import abc
from typing import Any, Union, List, Dict


class DataProcessor(abc.ABC):
    def __init__(self) -> None:
        self._storage: List[tuple[int, str]] = []
        self._counter: int = 0

    @abc.abstractmethod
    def validate(self, data: Any) -> bool:
        pass

    @abc.abstractmethod
    def ingest(self, data: Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        if not self._storage:
            raise IndexError("No data")
        return self._storage.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        if isinstance(data, list):
            return (
                all(isinstance(x, (int, float)) for x in data)
                and len(data) > 0
            )
        return False

    def ingest(
        self, data: Union[int, float, List[Union[int, float]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, str(item)))
                self._counter += 1
        else:
            self._storage.append((self._counter, str(data)))
            self._counter += 1


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        if isinstance(data, list):
            return all(isinstance(x, str) for x in data) and len(data) > 0
        return False

    def ingest(self, data: Union[str, List[str]]) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for item in data:
                self._storage.append((self._counter, item))
                self._counter += 1
        else:
            self._storage.append((self._counter, data))
            self._counter += 1


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        if isinstance(data, dict):
            return (
                all(
                    isinstance(k, str) and isinstance(v, str)
                    for k, v in data.items()
                )
                and "log_level" in data
                and "log_message" in data
            )
        if isinstance(data, list):
            return (
                all(
                    isinstance(x, dict)
                    and "log_level" in x
                    and "log_message" in x
                    for x in data
                )
                and len(data) > 0
            )
        return False

    def ingest(
        self, data: Union[Dict[str, str], List[Dict[str, str]]]
    ) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for item in data:
                val = f"{item['log_level']}: {item['log_message']}"
                self._storage.append((self._counter, val))
                self._counter += 1
        else:
            val = f"{data['log_level']}: {data['log_message']}"
            self._storage.append((self._counter, val))
            self._counter += 1


if __name__ == "__main__":
    print("=== Code Nexus - Data Processor ===")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    print("Testing Numeric Processor...")
    print(f"Trying to validate input '42': {np.validate(42)}")
    print(f"Trying to validate input 'Hello': {np.validate('Hello')}")
    print("Test invalid ingestion of string 'foo' without prior validation:")
    try:
        np.ingest("foo")  # type: ignore
    except ValueError as e:
        print(f"Got exception: {e}")
    print("Processing data:")
    np.ingest([1, 2, 3, 4, 5])
    print("Extracting 3 values...")
    for i in range(3):
        r, v = np.output()
        print(f"Numeric value {r}: {v}")
    print("Testing Text Processor...")
    print(f"Trying to validate input '42': {tp.validate(42)}")
    print("Processing data: ['Hello', 'Nexus', 'World']")
    tp.ingest(["Hello", "Nexus", "World"])
    print("Extracting 1 value...")
    r, v = tp.output()
    print(f"Text value {r}: {v}")
    print("Testing Log Processor...")
    print(f"Trying to validate input 'Hello': {lp.validate('Hello')}")
    logs = [
        {"log_level": "NOTICE", "log_message": "Connection to server"},
        {"log_level": "ERROR", "log_message": "Unauthorized access!!"},
    ]
    print(f"Processing data: {logs}")
    lp.ingest(logs)
    print("Extracting 2 values...")
    for i in range(2):
        r, v = lp.output()
        print(f"Log entry {r}: {v}")
