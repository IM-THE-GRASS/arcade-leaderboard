import reflex as rx
import pymongo
import os
import dotenv
dotenv.load_dotenv()

print(os.environ.get("mongoDB"))
dbclient = pymongo.MongoClient(os.environ.get("mongoDB"))
db= dbclient["arcade-leaderboard"]

class State(rx.State):
    people:dict
    def get_people():
        people = db["people"]
        result = []
        for x in people.find():
            x.pop('_id')
            result.append(x)
        return result
    people:list[dict[str, str]] = get_people()
    print(type(people))
    print(hash("testpassword"))
    print(hash("testpassword"))
    print(hash("testpassword"))
        
        
    print(dbclient.list_database_names())

def leaderboard_item(name: str, tickets: str, image_url: str, info:list[dict[str, str]] = []) -> rx.Component:
    return rx.center(
        rx.cond(
            info,
            rx.hstack(
                rx.image(src=image_url, width="auto", height="16vh", border_radius="999px"),
                rx.vstack(
                    rx.text(name, font_size=["4vw", "3vw", "2.5vw"], font_weight="600", color="#3DD68C"),
                    rx.text(f"{info[0]} tickets", font_size=["3vw", "2.5vw", "1.8vw"], font_weight="600", color="#3DD68C"),
                    align_items="flex-start",
                ),
                spacing="2vw",
            ),
            rx.hstack(
                rx.image(src=image_url, width="auto", height="16vh", border_radius="999px"),
                rx.vstack(
                    rx.text(name, font_size=["4vw", "3vw", "2.5vw"], font_weight="600", color="#3DD68C"),
                    rx.text(f"{tickets} tickets", font_size=["3vw", "2.5vw", "1.8vw"], font_weight="600", color="#3DD68C"),
                    align_items="flex-start",
                ),
                spacing="2vw",
            ),
        ),
        
        justify="start",
        padding="2vw",
        background="#113B29",
        border_radius="8px",
        width="100%",
        height="15vh",
    )

def leaderboard() -> rx.Component:
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
                lambda info: leaderboard_item("Nibbles", "47", "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp", info=info),
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

def index() -> rx.Component:
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