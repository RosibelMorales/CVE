"""Base state for Twitter example. Schema is inspired by https://drawsql.app/templates/twitter."""
from typing import Optional

from sqlmodel import Field

import reflex as rx

class User(rx.Model, table=True):
    username: str = Field()
    password: str = Field()


class State(rx.State):
    """The base state for the app."""

    user: Optional[User] = None

    def logout(self):
        self.reset()
        return rx.redirect("/")

    def check_login(self):
        if not self.logged_in:
            return rx.redirect("/login")

    @rx.var
    def logged_in(self):
        """Check if a user is logged in."""
        return self.user is not None
    
