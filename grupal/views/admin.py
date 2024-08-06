import reflex as rx

@rx.page(route="/vista_admin")
def vista_admin_page() -> rx.Component:
    return rx.text("Vista del Admin", font_size="24px", color="black")
