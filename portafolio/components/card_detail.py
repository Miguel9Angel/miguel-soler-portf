import reflex as rx
from portafolio.data import Extra  
from portafolio.styles.styles import IMAGE_HEIGHT, Size   

def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.inset(
            rx.image(
                src=extra.image,
                height=IMAGE_HEIGHT,
                width="100%",
                object_fit="cover"
            ),
            pb=Size.DEFAULT.value
        ),
        rx.text.strong(extra.title),
        rx.text(
            extra.description,
            size=Size.SMALL.value,
            color_scheme="gray"
        ),
        width="100%",
        cursor="pointer",
        _hover={"transform": "scale(1.02)"},
        transition="transform 0.2s ease-in-out",
        on_click=rx.redirect(extra.url, external=True)
    )