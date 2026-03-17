import reflex as rx
from AIAgentForge.state.auth_state import AuthState

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link("AIAgentForge", href="/", font_weight="bold"),
        rx.spacer(),
        rx.cond(
            AuthState.is_authenticated,
            rx.hstack(
                rx.link("Dashboard", href="/"),
                rx.link("Collections", href="/collections"),
                rx.link("Chat", href="/chat"),
                rx.spacer(),
                rx.text(AuthState.user.email),
                rx.button("Logout", color_scheme="red", on_click=AuthState.handle_logout),
                spacing="4",
            ),
            rx.hstack(
                rx.link("Login", href="/login"),
                rx.link("Sign Up", href="/signup"),
                spacing="4",
            )
        ),
        position="sticky",
        top="0",
        padding="1em",
        width="100%",
        z_index="10",
        background_color=rx.color("gray", 2),
    )