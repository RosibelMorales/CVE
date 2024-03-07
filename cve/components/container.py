import reflex as rx


def container(*children, **props) -> rx.Component:
    props = (
        dict(
            center_content=True,
            justifyContent="center",
            maxWidth="auto",
            height="100vh",
            bg="#1E1E1E"
        )
        | props
    )
    return rx.container(*children, **props)