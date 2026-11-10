import typing
from data_processor import NumericProcessor, TextProcessor, LogProcessor
from data_stream import DataStream


@typing.runtime_checkable
class ExportPlugin(typing.Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        pass


class PipelineDataStream(DataStream):
    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self.processors:
            collected = []
            for _ in range(nb):
                if proc._storage:
                    collected.append(proc.output())
                else:
                    break
            if collected:
                plugin.process_output(collected)


class CSVExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("CSV Output:")
        vals = [v for _, v in data]
        print(",".join(vals))


class JSONExportPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:
        print("JSON Output:")
        items = [f'"item_{r}": "{v}"' for r, v in data]
        print("{" + ", ".join(items) + "}")


if __name__ == "__main__":
    print("=== Code Nexus - Data Pipeline ===")
    print("Initialize Data Stream...")
    ds = PipelineDataStream()
    ds.print_processors_stats()
    print("Registering Processors")
    np = NumericProcessor()
    tp = TextProcessor()
    lp = LogProcessor()
    ds.register_processor(np)
    ds.register_processor(tp)
    ds.register_processor(lp)
    batch1 = [
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
    ds.process_stream(batch1)
    ds.print_processors_stats()
    print("Send 3 processed data from each processor to a CSV plugin:")
    csv_plugin = CSVExportPlugin()
    ds.output_pipeline(3, csv_plugin)
    ds.print_processors_stats()
    batch2 = [
        21,
        ["I love AI", "LLMs are wonderful", "Stay healthy"],
        [
            {"log_level": "ERROR", "log_message": "500 server crash"},
            {
                "log_level": "NOTICE",
                "log_message": "Certificate expires in 10 days",
            },
        ],
        "World hello",
    ]
    print(
        "Send another batch of data: [21, ['I love AI', "
        "'LLMs are wonderful', 'Stay healthy'], [{'log_level': 'ERROR', "
        "'log_message': '500 server crash'}, {'log_level': 'NOTICE', "
        "'log_message': 'Certificate expires in 10 days'}], "
        "'World hello']"
    )
    ds.process_stream(batch2)
    ds.print_processors_stats()
    print("Send 5 processed data from each processor to a JSON plugin:")
    json_plugin = JSONExportPlugin()
    ds.output_pipeline(5, json_plugin)
    ds.print_processors_stats()
