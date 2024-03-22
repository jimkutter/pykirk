from textual.app import App, ComposeResult
from textual.containers import VerticalScroll, Horizontal, Vertical
from textual.widgets import Header, Footer, Static, Placeholder

class DateList(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder("DateList")

class CalendarWidget(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder("CalendarWidget")

class EntryView(Static):
    def compose(self) -> ComposeResult:
        yield Placeholder("DayView")

class PyKirk(App):
    """Captain's Log..."""

    CSS_PATH = "pykirk.tcss"

    BINDINGS = [
        ("q", "quit", "Quit"),
        ("n", "new", "New"),
        ("e", "edit", "Edit"),
        ("d", "delete", "Delete"),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        with Vertical():
            with Horizontal():
                yield DateList()
                yield CalendarWidget()
            with VerticalScroll():
                yield EntryView()            
        yield Footer()


def run():
    app = PyKirk()
    app.run()

if __name__ == "__main__":
    run()
