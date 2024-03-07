"""The home page. This file includes examples abstracting complex UI into smaller components."""
import reflex as rx
from cve.state.base import State
from cve.components.button_page import button_page
from cve.components.footer import footer
from ..components import container


def home():
    return container(
        rx.center(
            rx.vstack(
                rx.container(
                    rx.image(
                    src="/icono.png",
                    width="500px", 
                    height="auto",
                    border_radius="15px 15px",
                    border="5px",
                    ),
                    width="250px",
                    center_content=True
                ),
                rx.container(height="55px"),
                rx.hstack(
                    button_page("CVE", "/cve"),
                    button_page("CVE Historial", "/change"),
                    button_page("Acerca de...", "/about"),
                    width="100%",
                    spacing="1em"                
                ),
                rx.container(height="100px"),
                footer(),
                center_content=True,
                justifyContent="center",
            )
        )
    )
