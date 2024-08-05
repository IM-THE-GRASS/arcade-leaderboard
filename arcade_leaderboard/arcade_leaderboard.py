import reflex as rx
from arcade_leaderboard.state import *
import arcade_leaderboard.components.userbutton as userbutton
def leaderboard_item(info):
    return rx.center(
        rx.hstack(
            rx.center(
                rx.avatar(src=info[1]["pfp"], fallback= info[1]["username"][0:2], size="4", radius="full"),    
                height="15vh",
                padding_left="10vw"
            ),
            
            rx.vstack(
                rx.text(f"{info[1]["username"]}", font_size=["2.5vw"], font_weight="600", color="#3DD68C", padding_top="0.5vh"),
                rx.cond(
                    info[1]["tickets"],
                    rx.text(f"{info[1]['tickets']} 🎟️", font_size=["2vw"], font_weight="600", color="#3DD68C"),
                ),
                
                spacing='1',
                align_items="flex-start",
                text_wrap="wrap",
            ),
            spacing="2vw",
        ),
        justify="start",
        padding="2vw",
        background="#113B29",
        border_radius="8px",
        width="100%",
        height="15vh",
        padding_right="78vw"
    )

def leaderboard():
    return rx.vstack(
        rx.box(
            rx.text("Arcade leaderboard", font_size=["6vw", "5vw", "4vw"], font_weight="700", color="#B1F1CB"),
            padding="2vw",
            background="#113B29",
            border_radius="8px",
            width="100%",
        ),
        rx.vstack(
            rx.foreach(
                State.people,
                lambda info: leaderboard_item(info),
            ),
            rx.foreach(
                State.people,
                lambda info: leaderboard_item(info),
            ),
            rx.foreach(
                State.people,
                lambda info: leaderboard_item(info),
            ),
            spacing="2vh",
            width="100%",
            overflow_y="auto",
            height="70vh",
        ),
        spacing="3vh",
        width="95vw",
        max_width="1200px",
        padding="3vw",
        background="#132D21",
        border_radius="8px",
    )

def index():
    return rx.center(
        rx.box(
            leaderboard(),
            userbutton.button(),
            width="95vw",
            max_width="1200px",
            position="relative",
            
        ),
        width="100%",
        height="100vh",
        background="#0C231A",
        overflow="hidden",
        padding_top = "12vh"
    )

app = rx.App()
app.add_page(index)