import reflex as rx
from cve.layouts import auth_layout
from cve.state.auth import AuthState
from cve.components.container import container


def login():
    return container(
        auth_layout(
            rx.vstack(
                rx.container(
                rx.text(
                "Iniciar sesión",
                fontSize="28px",
                color="white",
                fontWeight="bold",
                letterScpacing="2px"
                ),
                width="250px",
                center_content=True,
                ), 
                rx.container(
                    rx.image(
                    src="/icono.png",
                    width="100px", 
                    height="auto",
                    border_radius="15px 15px",
                    border="5px",
                    ),
                    width="250px",
                    center_content=True
                ), 
                rx.container(
                    rx.vstack(
                        rx.hstack(
                            rx.icon(
                                tag="email",
                                color="white",
                                fontSize="11px",
                            ),
                            rx.input(type="email", placeholder="Nombre de usuario", on_blur=AuthState.set_username, mb=4, color="white"),
                        ),
                        rx.hstack(
                            rx.icon(
                                tag="lock",
                                color="white",
                                fontSize="11px",
                            ),
                            rx.input(
                                type_="password",
                                placeholder="Contraseña",
                                on_blur=AuthState.set_password,
                                mb=3,
                                color="white",
                            ),
                        ),
                        rx.button(
                            "Iniciar sesión",
                            on_click=AuthState.login,
                            bg="blue",
                            color="white",
                            fontSize="11px",
                            weight="bold",
                        ),
                        
                        alignItems="center",
                        p=10,
                    )
                ),
                rx.text(
                    "Crear cuenta ",
                    rx.link("Clic aquí.", href="/signup", color="blue.500"),
                    color="gray.600",
                ),
            )
        ),
    )
