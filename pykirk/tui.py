import configparser
import os
import pathlib

from textual.app import App, ComposeResult, RenderResult
from textual.containers import Horizontal, Vertical, VerticalScroll
from textual.widget import Widget
from textual.widgets import Footer, Header, Placeholder, Static, DirectoryTree


class DateWidget(Widget):
    def __init__(self, base_path: str):
        super().__init__()
        self.base_path = pathlib.Path(os.path.expanduser(base_path))

        self.base_path.mkdir(exist_ok=True)

    def compose(self) -> ComposeResult:
        yield DirectoryTree(self.base_path)


class PreviewWidget(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder("PreviewWidget")


class EntryWidget(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder("EntryWidget")


class PyKirk(App):
    """Captain's Log..."""

    CSS_PATH = "pykirk.tcss"

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("n", "new", "New"),
        ("e", "edit", "Edit"),
        ("d", "delete", "Delete"),
    ]

    def init_config(self):
        self.config = configparser.ConfigParser()
        config_file_path = pathlib.Path(os.path.expanduser("~/.pykirk/config.ini"))

        config_file_path.parent.mkdir(exist_ok=True)

        if config_file_path.exists():
            self.config.read_file(config_file_path.open())

        self.log.info("In on_mount!")

    def on_mount(self):
        self.init_config()

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        self.init_config()

        yield Header()
        with Vertical():
            with Horizontal():
                yield DateWidget(
                    self.config.get("journal", "path", fallback="~/.pykirk/journal/")
                )
                yield EntryWidget()
        yield Footer()


def run():
    app = PyKirk()
    app.run()


if __name__ == "__main__":
    run()
