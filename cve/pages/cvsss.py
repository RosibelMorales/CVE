import reflex as rx 
from cve.components.container import container
from cve.state.query import QueryState
from fastapi.exceptions import HTTPException
from typing import List
import pandas as pd
import csv

dataForTable=QueryState.dataForTable

def draw_table():
    return rx.data_table(
        data=dataForTable,
        pagination=True,    
        sort=True,
        search=True,
        style={"maxHeight": "500px", "overflowY": "auto", "width": "100%"}
    )

def cvsss():
    return rx.container(
        rx.vstack(
            rx.heading("CVSSV3 Severity", color="white", size="lg"),
            rx.box(   
                rx.hstack(
                    rx.text("Clasificación de gravedad: ", color="white"),
                    rx.input(color="white", placeholder="LOW/MEDIUM/HIGH/CRITICAL", on_blur=QueryState.set_clasificacion)
                ),
                rx.button("Buscar", color="white", bg="blue", on_click=QueryState.get_classification),
                rx.button("Limpiar tabla", color="white", bg="red", on_click=QueryState.clear),
            ),
        ),
        draw_table(),
        style={"width": "100%", "maxWidth": "auto"},  # Ajusta el ancho máximo del contenedor principal según tus necesidades
        bg="#1E1E1E"
    )