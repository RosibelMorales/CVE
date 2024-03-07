import reflex as rx 

def label(body: str) -> rx.Component:
    return rx.text(
        body,
        fontSize="13px",
        color="white",
    )