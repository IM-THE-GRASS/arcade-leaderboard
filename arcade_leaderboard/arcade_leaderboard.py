import reflex as rx

def leaderboard_item(name: str, tickets: int, image_url: str) -> rx.Component:
    return rx.center(
        rx.hstack(
            rx.image(src=image_url, width="auto", height="16vh", border_radius="999px"),
            rx.vstack(
                rx.text(name, font_size=["4vw", "3vw", "2.5vw"], font_weight="600", color="#3DD68C"),
                rx.text(f"{tickets} tickets", font_size=["3vw", "2.5vw", "1.8vw"], font_weight="600", color="#3DD68C"),
                align_items="flex-start",
            ),
            spacing="2vw",
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
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            leaderboard_item("Nibbles", 47, "https://cloud-bv8ratyvx-hack-club-bot.vercel.app/4nibbler.webp"),
            spacing="2vh",
            width="100%",
            overflow_y="auto",
            max_height="70vh",
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