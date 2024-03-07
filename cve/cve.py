import reflex as rx

from .pages import home, login, signup, cve, cpe, cveid, cvsss, cwe, about
from .state.base import State

app = rx.App(state=State)
app.add_page(login)
app.add_page(signup)
app.add_page(home, route="/", on_load=State.check_login())
app.add_page(cpe)
app.add_page(cve)
app.add_page(cveid)
app.add_page(cvsss)
app.add_page(cwe)
app.add_page(about)
app.compile()
