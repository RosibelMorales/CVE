import reflex as rx 
from typing import List

from cve.components.container import container
from cve.components.header import header
from cve.components.footer import footer

def cve() -> rx.Component:
    return container(
        header(),
        footer(),
    )