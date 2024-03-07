import reflex as rx

from cve.components.container import container


def auth_layout(*args) -> rx.Component:
    return container(
        *args,
        width="400px",
        height="75vh",
        bg="#1E1E1E",
        borderRadius="15px",
        boxShadow = "41px -41px 82px #2d374b, -41px 41px 82px #2d374b",
    )
