import reflex as rx
from arcade_leaderboard.state import *
from reflex_motion import motion
def dialog_content():
    return rx.dialog.content(
        rx.dialog.title(
            "Add a user to the leaderboard"
        ),
        rx.flex(
            rx.text(
                "Username",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
                color_scheme="green"
            ),
            motion(
                rx.input(
                    value = State.reg_username,
                    placeholder="Enter your username",
                    on_change=State.set_reg_username,
                    color_scheme="green"
                ),
                while_hover={"scale": 1.05},
                while_tap={"scale": 0.95},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            rx.text(
                "Shop URL",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
                color_scheme="green"
            ),
            motion(
                rx.input(
                    value=State.reg_url,
                    on_change=State.set_reg_url,
                    placeholder="Enter your shop URL you get when you do /shop in the arcade slack",
                    color_scheme="green"
                ),
                while_hover={"scale": 1.05},
                while_tap={"scale": 0.95},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            rx.text(
                "Link to profile picture (OPTIONAL)",
                as_="div",
                size="2",
                margin_bottom="4px",
                weight="bold",
                color_scheme="green"
            ),
            motion(
                rx.input(
                    value=State.reg_pfp,
                    on_change=State.set_reg_pfp,
                    placeholder="Enter a link to your pfp. (For example:https://placehold.co/60x60)",
                    color_scheme="green"
                ),
                while_hover={"scale": 1.05},
                while_tap={"scale": 0.95},
                transition={"type": "spring", "stiffness": 400, "damping": 17},
            ),
            rx.text(
                State.reg_error,
                size="2",
                weight="medium",
                color_scheme="red"
            ),
            rx.dialog.close(
                motion(
                    rx.button(
                        "Confirm",
                        color_scheme="green",
                        disabled = State.register_button_disabled,
                        on_click=State.register,
                        width="100%"
                        
                    ),
                    
                    while_hover={"scale": 1.02},
                    while_tap={"scale": 0.95},
                    transition={"type": "spring", "stiffness": 400, "damping": 17},
                ),
                
            ),
            direction="column",
            spacing="3",
        )
    )


def button():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.center(
                motion(
                    rx.box(
                        rx.icon(
                            tag="user-plus",
                            color="#B1F1CB",
                            size=70,
                        ),
                        bg="#174933",
                        border_radius="999999px",
                        padding="1vw"
                        
                    ),
                    
                    while_hover={"scale": 1.2},
                    while_tap={"scale": 0.9},
                    transition={"type": "spring", "stiffness": 400, "damping": 17},
                ),
                
                border_radius="999999px",
                width="6vw",
                height="6vw",
                padding="1vw",
                position="absolute",
                right="-4vw",
                top="7vh",
            ),
            
        ),
        rx.dialog.content(
            dialog_content()
        )
        
    
    )