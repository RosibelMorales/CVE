import reflex as rx

from cve.components.label import label
from cve.state.select import SelectState
from cve.components.container import container

list = ["CPE especifico", "CVE Id", "CVSS V3 Severidad", "CWE Id"]


def header() -> rx.Component:
    return container(
        rx.hstack(
            label("Seleccione una opción: "),
            rx.select(
                list,
                color="blue",
                size="lg",
                on_change=SelectState.update_select,
            ),
            rx.button("Ir", on_click=SelectState.show_fields, color_scheme="blue"),
        ),
        justifyContent="center",    
        maxWidth="auto",
    )