import reflex as rx
from arcade_leaderboard.state import *
def dialog_content():
    return rx.dialog.content(
        rx.dialog.title(
            "Register"
        ),
        rx.flex(
            rx.text(
                "Username",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
            rx.input(
                value = State.reg_username,
                placeholder="Enter your username",
                on_change=State.set_reg_username
            ),
            rx.text(
                "Password",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
            
            rx.input(
                value=State.reg_password,
                placeholder="Enter your password",
                type="password",
                on_change=State.set_reg_password
            ),
            rx.text(
                "Shop URL",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
            ),
            
            rx.input(
                value=State.reg_url,
                on_change=State.set_reg_url,
                placeholder="Enter your shop URL you get when you do /shop in the arcade slack",
            ),
            rx.text(
                State.reg_error,
                size="2",
                weight="medium",
                color_scheme="red"
            ),
            rx.dialog.close(
                rx.button(
                    "Confirm",
                    color_scheme="green",
                    disabled = State.register_button_disabled,
                    on_click=State.register
                )
            ),
            direction="column",
            spacing="3",
        )
    )


def button():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.center(
                rx.icon(
                    tag="user_round_cog",
                    color="#B1F1CB",
                    size=70,
                ),
                border_radius="999999px",
                width="6vw",
                height="6vw",
                padding="1vw",
                background="#174933",
                position="absolute",
                right="-4vw",
                top="7vh",
            ),
            
        ),
        rx.dialog.content(
            dialog_content()
        )
        
    
    )