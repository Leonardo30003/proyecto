import reflex as rx

@rx.page(route="/vista_docente")
def vista_docente_page() -> rx.Component:
    return rx.text("Vista del Docente", font_size="24px", color="black")
