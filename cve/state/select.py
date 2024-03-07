import reflex as rx

from cve.state.base import State

class SelectState(State):
    option: str = "No selection yet."
    
    def update_select(self, value):
        self.option = value
    
    def show_fields(self) -> rx.Component:
        match self.option:
            case "CPE especifico":
                return rx.redirect("/cpe")
            case "CVE Id":
                return rx.redirect("/cveid")
            case "CVSS V3 Severidad":
                return rx.redirect("/cvsss")
            case "CWE Id":
                return rx.redirect("/cwe")
            case _:
                return rx.window_alert("No hay selección específica")