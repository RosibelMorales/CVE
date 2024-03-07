import reflex as rx
from cve.components.container import container
from cve.state.query import QueryState
import pandas as pd

dataForTable=QueryState.dataForTable

def draw_table():
    return rx.data_table(
        data=dataForTable,
        pagination=True,    
        sort=True,
        search=True,
        style={"maxHeight": "500px", "overflowY": "auto", "width": "100%"}
    )

def cpe():
    
    return container(
        rx.vstack(
            rx.heading("CPE específico", color="white", size="lg"),
            rx.box(   
                rx.hstack(
                    rx.text("Tipo: ", color="white"),
                    rx.input(color="white", placeholder="ej. o", on_blur=QueryState.set_tipo)
                ),
                rx.hstack(
                    rx.text("Plataforma: ", color="white"),
                    rx.input(color="white", placeholder="ej. microsoft", on_blur=QueryState.set_plataforma)
                ),
                rx.hstack(
                    rx.text("Nombre y versión principal: ", color="white"),
                    rx.input(color="white", placeholder="ej. windows_10", on_blur=QueryState.set_nombre_version)
                ),
                rx.hstack(
                    rx.text("Versión específica: ", color="white"),
                    rx.input(color="white", placeholder="ej. 1067", on_blur=QueryState.set_version_esp)
                ),
                rx.button("Buscar", color="white", bg="blue", on_click=QueryState.get_cpe),
            ),
        ),
        draw_table(),
        style={"width": "100%", "maxWidth": "auto"},
        bg="#1E1E1E"
    )