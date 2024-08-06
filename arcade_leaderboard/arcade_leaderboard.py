import reflex as rx
from arcade_leaderboard.state import *
import arcade_leaderboard.components.userbutton as userbutton
from reflex_lottiefiles import LottieFiles


def leaderboard_item(info, index):
    return rx.box(
        rx.hstack(
            
            rx.center(
                rx.hstack(
                    rx.cond(
                        index != 0,
                        rx.text(
                            f"{index + 1}",
                            color_scheme="green",
                            size="9",
                            font_weight="bolder"
                        ),
                        rx.box(
                            LottieFiles(
                                src="https://lottie.host/b3f43394-a351-4755-9c03-5c61100951e4/kHb0G7NsSI.lottie",
                                autoplay=True,
                                loop=False,
                                width="15vw",
                                height="5vw"
                            ),
                            right="-100"
                            position="relative",
                        )
                    ),
                    
                    
                    rx.avatar(src=info[1]["pfp"], fallback= info[1]["username"][0:2], size="5", radius="full"),   
                    spacing="6"
                ),
                
                
                 
                height="15vh"
            ),
            
            rx.vstack(
                rx.text(
                    
                    f"{info[1]["username"]}", 
                    font_size=["2.5vw"],
                    font_weight="600",
                    
                    color="#3DD68C",
                    padding_top="0.5vh",
                    text_wrap="nowrap"
                
                ),
                rx.cond(
                    info[1]["tickets"],
                    rx.hstack(
                        rx.text(
                            f"{info[1]['tickets']} 🎟️",
                            font_size=["2vw"],
                            font_weight="600",
                            color="#3DD68C", 
                            
                            text_wrap="nowrap"
                        ),
                        rx.box(
                            rx.desktop_only(
                                LottieFiles(
                                    src="https://lottie.host/1216c16a-a76d-4084-843c-7d6f06e931fa/FIfp90siNI.lottie",
                                    autoplay=True,
                                    loop=False,
                                    width="11vw",
                                ),
                            ),
                            
                            position="relative",
                            right="7.5vw",
                            top="-4.4vh"
                        )
                        
                    )
                    
                ),
                
                spacing='1',
                align_items="flex-start",
            ),
            spacing="2vw",
        ),
        padding_bottom="3vh",
        padding_left="2vw",
        background="#113B29",
        border_radius="8px",
        width="100%",
        height="15vh",
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
                State.peopledict,
                lambda info, index: leaderboard_item(info, index),
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
        on_mount=State.update_people
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