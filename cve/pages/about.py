import reflex as rx
from cve.components.container import container
from cve.components.footer import footer

def about():
    return container(
        rx.box(
            rx.heading("Acerca de este software", color="white"),
            rx.text("Desarrollar e implementar una herramienta SIEM que involucrará la integración y configuración de tecnologías avanzadas de recopilación", color="white", m=2),
            rx.text("y análisis de registros de eventos, permitiendo una visión holística de la postura de seguridad.", color="white", m=2),
            rx.divider(variant="dashed", border_color="white"),
            rx.text("Síguenos en nuestras redes sociales:", color="white", m=2),
            rx.link("GitHub", href="https://github.com/RosibelMorales", target="_blank", color="white", m=2),
            rx.link("Facebook", href="https://www.facebook.com/profile.php?id=100057139582326&locale=es_LA", target="_blank", color="white", m=2),
        ),
        footer(),
    )

