import reflex as rx
import pymongo
import os
import dotenv
dotenv.load_dotenv()

print(os.environ.get("mongoDB"))
dbclient = pymongo.MongoClient(os.environ.get("mongoDB"))
db= dbclient["arcade-leaderboard"]

class State(rx.State):
    def prints(to_print, thing2=None):
        print("1", to_print)
        print("2", thing2)
    
    
    def get_people():
        people = db["people"]
        result = {}
        for x in people.find():
            x.pop('_id')
            keys = list(x.keys())
            x = x[keys[0]]
            print(type(x))
            print( "x", x)
            result[keys[0]] = x
        return result
    people:dict[str, dict[str, str]] = get_people()
def leaderboard_item(info):
    return rx.center(
        rx.hstack(
            rx.cond(
                info[1]["pfp"],
                rx.avatar(src=info[1]["pfp"], fallback= info[1]["username"][0:2], size="3", radius="full"),
                #rx.image(src=info[1]["pfp"], width="auto", height="16vh", border_radius="999px"),
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
            rx.center(
                rx.icon(
                    tag="user_round_cog",
                    color="#B1F1CB",
                    size=70,
                ),
                width="6vw",
                height="6vw",
                padding="1vw",
                background="#174933",
                border_radius="50%",
                overflow="hidden",
                position="absolute",
                right="-4vw",
                top="7vh",
                display="flex",
                justify_content="center",
                align_items="center",
            ),
            width="95vw",
            max_width="1200px",
            position="relative",
        ),
        width="100%",
        height="100vh",
        background="#0C231A",
        overflow="hidden"
    )

app = rx.App()
app.add_page(index)