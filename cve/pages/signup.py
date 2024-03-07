"""Sign up page. Uses auth_layout to render UI shared with the login page."""
import reflex as rx
from cve.layouts import auth_layout
from cve.state.auth import AuthState
from cve.components.container import container


def signup():
    return container(
        auth_layout(
            rx.container(
                rx.text(
                "Registrarse",
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
                        rx.input(placeholder="Nombre de usuario", on_blur=AuthState.set_username, mb=4, color="white"),
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
                            mb=4,
                            color="white"
                        ),
                    ),
                    rx.hstack(
                        rx.icon(
                            tag="lock",
                            color="white",
                            fontSize="11px",
                        ),
                        rx.input(
                            type_="password",
                            placeholder="Confirme su contraseña",
                            on_blur=AuthState.set_confirm_password,
                            mb=4,
                            color="white"
                        ),
                    ),
                    rx.button(
                        "Registrarse",
                        on_click=AuthState.signup,
                        bg="blue",
                        color="white",
                    ),
                    justifyContent="center",
                    align_items="center",
                    p=4,
                )
            ),
            rx.text(
                "Ya tienes cuenta? ",
                rx.link("Inicia sesión aquí.", href="/login", color="blue.500"),
                color="gray.600",
            ),
        ),
    )
