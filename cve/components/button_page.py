import reflex as rx

def button_page(title: str, url: str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.vstack(
                    rx.text(title),
                    color="white",
                    fontSize="15px",
                    weight="bold",
                    spacing="0.5em",
                    padding_y="0.5em",
                    padding_right="0.5em"                
                ),
                width="100%"
            ),
            width="200px",
            height="45px",
            color_scheme="blue",
        ),
        on_click=rx.redirect(url),
        is_external=True,
        width="100%"
    )