import typing
from data_processor import (
    DataProcessor,
    NumericProcessor,
    TextProcessor,
    LogProcessor,
)


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.processed_counts: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        if proc not in self.processed_counts:
            self.processed_counts[proc] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            handled = False
            for proc in self.processors:
                if proc.validate(element):
                    proc.ingest(element)
                    if isinstance(element, list):
                        self.processed_counts[proc] += len(element)
                    else:
                        self.processed_counts[proc] += 1
                    handled = True
                    break
            if not handled:
                print(
                    f"DataStream error - Can't process element in "
                    f"stream: {element}"
                )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = ""
            if isinstance(proc, NumericProcessor):
                name = "Numeric Processor"
            elif isinstance(proc, TextProcessor):
                name = "Text Processor"
            elif isinstance(proc, LogProcessor):
                name = "Log Processor"
            total = self.processed_counts[proc]
            rem = len(proc._storage)
            print(
                f"{name}: total {total} items processed, "
                f"remaining {rem} on processor"
            )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===")
    print("Initialize Data Stream...")
    ds = DataStream()
    ds.print_processors_stats()
    print("Registering Numeric Processor")
    np = NumericProcessor()
    ds.register_processor(np)
    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {"log_level": "INFO", "log_message": "User wil is connected"},
        ],
        42,
        ["Hi", "five"],
    ]
    print(
        "Send first batch of data on stream: ['Hello world', "
        "[3.14, -1, 2.71], [{'log_level': 'WARNING', "
        "'log_message': 'Telnet access! Use ssh instead'}, "
        "{'log_level': 'INFO', 'log_message': 'User wil is connected'}], "
        "42, ['Hi', 'five']]"
    )
    ds.process_stream(batch)
    ds.print_processors_stats()
    print("Registering other data processors")
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(tp)
    ds.register_processor(lp)
    print("Send the same batch again")
    ds.process_stream(batch)
    ds.print_processors_stats()
    print(
        "Consume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )
    for _ in range(3):
        np.output()
    for _ in range(2):
        tp.output()
    for _ in range(1):
        lp.output()
    ds.print_processors_stats()
