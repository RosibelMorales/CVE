import reflex as rx 
from cve.state.query import QueryState

dataForTable=QueryState.dataForTable

def draw_table():
    return rx.data_table(
        data=dataForTable,
        pagination=True,    
        sort=True,
        search=True,
        style={"maxHeight": "500px", "overflowY": "auto", "width": "100%"}
    )

def cveid():
    return rx.container(
        rx.vstack(
            rx.heading("CVE por ID", color="white", size="lg"),
            rx.box(   
                rx.hstack(
                    rx.text("ID de CVE: ", color="white"),
                    rx.input(color="white", placeholder="ej. CVE-2019-1010218", on_blur=QueryState.set_id_cve)
                ),
                rx.button("Buscar", color="white", bg="blue", on_click=QueryState.get_by_id),
                rx.button("Limpiar tabla", color="white", bg="red", on_click=QueryState.clear),
            ),
        ),
        draw_table(),
        style={"width": "100%", "maxWidth": "auto"},  # Ajusta el ancho máximo del contenedor principal según tus necesidades
        bg="#1E1E1E"
    )
    
