import reflex as rx 

def cpe_esp() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.text("Tipo: ", color="white"),
            rx.input(color="white")
        ),
        rx.hstack(
            rx.text("Plataforma: ", color="white"),
            rx.input(color="white")
        ),
        rx.hstack(
            rx.text("Nombre y versión principal: ", color="white"),
            rx.input(color="white")
        ),
        rx.hstack(
            rx.text("Versión específica: ", color="white"),
            rx.input(color="white")
        ),
        justifyContent="center",
    )
    