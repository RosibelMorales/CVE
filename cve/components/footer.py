import reflex as rx 

def footer() -> rx.Component:
    return rx.container(
        rx.container(height="55px"),
        rx.text(
            f"© Este producto utiliza datos de la API de NVD, pero no está respaldado ni certificado por NVD",
            fontSize="8px",
            color="white",
            letterSpacing="2px",
        ),
        maxWidth="auto",
        center_content=True,   
    )