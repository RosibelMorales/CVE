"""The authentication state."""
import reflex as rx
from sqlmodel import select

from .base import State, User


class AuthState(State):

    username: str
    password: str
    confirm_password: str

    def signup(self):
        with rx.session() as session:
            if self.password != self.confirm_password:
                return rx.window_alert("Passwords do not match.")
            if session.exec(select(User).where(User.username == self.username)).first():
                return rx.window_alert("Username already exists.")
            self.user = User(username=self.username, password=self.password)
            session.add(self.user)
            session.expire_on_commit = False
            session.commit()
            return rx.redirect("/")
    
    def login(self):
        if not self.username or not self.password:
            # Verificar si los campos de usuario o contraseña están vacíos
            return rx.window_alert("El nombre de usuario y contraseña son requeridos.")

        with rx.session() as session:
            user = session.exec(
                select(User).where(User.username == self.username)
            ).first()

            if user and user.password == self.password:
                self.user = user
                return rx.redirect("/")
            else:
                return rx.window_alert("Invalid username or password.")

