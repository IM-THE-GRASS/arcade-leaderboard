import reflex as rx
from arcade_leaderboard.state import *
import arcade_leaderboard.components.userbutton as userbutton
from reflex_lottiefiles import LottieFiles
from reflex_motion import motion

def leaderboard_item(info, indexnum):
    return motion(
        rx.hstack(
            
            rx.center(
                rx.hstack(
                    rx.cond(
                        State.top.contains(indexnum+1),
                        rx.box(
                            rx.mobile_and_tablet(
                                LottieFiles(
                                    src=State.top_anims[indexnum+1],
                                    autoplay=True,
                                    loop=False,
                                    width="10vh",
                                    height="12.5vh"
                                ),
                            ),
                            rx.desktop_only(
                                LottieFiles(
                                    src=State.top_anims[indexnum+1],
                                    autoplay=True,
                                    loop=False,
                                    width="17vh",
                                    height="12.5vh"
                                ),
                            ),
                            margin_right="-4vw",
                            margin_left="-3vw",
                            position="relative",
                        ),
                        
                        rx.text(
                            f"{indexnum + 1}",
                            color_scheme="green",
                            size="9",
                            font_weight="bolder"
                        ),
                        
                    ),
                    # rx.cond(
                    #     ~State.top.contains(indexnum+1),
                    
                    #     rx.avatar(src=info[1]["pfp"], fallback= info[1]["username"][0:2], size="5", radius="full"),
                    rx.avatar(src=info[1]["pfp"], fallback= info[1]["username"][0:2], size="5", radius="full", margin_top = "2vh"),  
                    # ), 
                    spacing="6"
                ),
                
                
                 
                height="15vh"
            ),
            
            rx.vstack(
                rx.text(
                    
                    f"{info[1]["username"]}", 
                    font_size=["5.5vh"],
                    font_weight="600",
                    
                    color="#3DD68C",
                    padding_top="0.5vh",
                    text_wrap="nowrap"
                
                ),
                rx.cond(
                    info[1]["tickets"],
                    rx.hstack(
                        rx.desktop_only(
                            rx.text(
                                f"{info[1]['tickets']}",
                                font_size=["5vh"],
                                font_weight="600",
                                color="#3DD68C", 
                                
                                text_wrap="nowrap"
                            ),
                        ),
                        rx.mobile_and_tablet(
                            rx.text(
                                f"{info[1]['tickets']} 🎟️",
                                font_size=["5vh"],
                                font_weight="600",
                                color="#3DD68C", 
                                
                                text_wrap="nowrap"
                            ),
                        ),
                        
                        rx.box(
                            rx.desktop_only(
                                LottieFiles(
                                    src="https://lottie.host/1216c16a-a76d-4084-843c-7d6f06e931fa/FIfp90siNI.lottie",
                                    autoplay=True,
                                    loop=False,
                                    width="9vw",
                                ),
                            ),
                            position="relative",
                            right="3.4vw",
                            top="-2vh"
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
        while_hover={"scale": 1.05},
        while_tap={"scale": 0.95},
        transition={"type": "spring", "stiffness": 300, "damping": 17},
    )

def leaderboard():
    return rx.vstack(
        motion(
            rx.text(
                "Arcade leaderboard",
                font_size=["6vw", "5vw", "4vw"],
                font_weight="700",
                color="#B1F1CB",
                font_family="Slackey, sans-serif",
            ),
            padding="2vw",
            background="#113B29",
            border_radius="8px",
            width="100%",
            while_hover={"scale": 1.05},
            while_tap={"scale": 0.95},
            transition={"type": "spring", "stiffness": 400, "damping": 17},
        ),
        rx.vstack(
            rx.foreach(
                State.peopledict,
                lambda info, index: leaderboard_item(info, index),
            ),
            spacing="2vh",
            width="100%",
            overflow_y="auto",
            overflow_x="hidden",
            height="70vh",
        ),
        spacing="3vh",
        width="95vw",
        max_width="1200px",
        padding="3vw",
        background="#132D21",
        border_radius="8px",
        
    )


@rx.page(on_load=State.update_people)
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

app = rx.App(
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;1,100;1,200;1,300;1,400;1,500;1,600;1,700&family=Slackey&display=swap"
    ],
)
app.add_page(index)