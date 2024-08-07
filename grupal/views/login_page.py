import reflex as rx
from enum import Enum

# Define your color palette and text color as seen in your colors.py file.
class Color(Enum):
    PRIMARY = "#D9D9D9"
    SECONDARY = "#FFB6C1"
    BACKGROUND = "#FFFFFF"
    CONTENT = "#FFFFFF"
    TEXT = "#444444"

class TextColor(Enum):
    HEADER = "#4A4A4A"
    BODY = "#6D6D6D"
    BUTTON_TEXT = "#FFFFFF"

class PageState(rx.State):
    cedula: str = ""
    username: str = ""
    password: str = ""
    error_message: str = ""

    def handle_submit_docente(self, form_data: dict):
        # Aquí puedes añadir la lógica de autenticación para el docente
        return rx.redirect("/vista_docente")

    def handle_submit_admin(self, form_data: dict):
        # Aquí puedes añadir la lógica de autenticación para el admin
        return rx.redirect("/vista_admin")

    def clear_error(self, _=None):
        self.error_message = ""

@rx.page(route="/login")
def login_page() -> rx.Component:
    return rx.box(
        rx.center(
            rx.box(
                rx.vstack(
                    rx.text("Sistema de Registro", font_size="3xl", font_weight="bold", color=TextColor.HEADER.value, margin_bottom="10px"),
                    rx.text("Bienvenido al sistema de asistencia de la UIDE", font_size="md", color=TextColor.BODY.value, margin_bottom="20px"),
                    rx.tabs.root(
                        rx.tabs.list(
                            rx.tabs.trigger("Docente", value="login_docente", padding="10px 20px", font_size="md", 
                                            background=Color.BACKGROUND.value, color=TextColor.HEADER.value, 
                                            border_radius="8px 8px 0 0", _selected={"background": Color.PRIMARY.value}),
                            rx.tabs.trigger("Admin", value="login_admin", padding="10px 20px", font_size="md", 
                                            background=Color.BACKGROUND.value, color=TextColor.HEADER.value, 
                                            border_radius="8px 8px 0 0", _selected={"background": Color.PRIMARY.value}),
                        ),
                        rx.tabs.content(
                            rx.box(
                                rx.form(
                                    rx.vstack(
                                        form_fields("Numero de Cedula", "Enter your ID", "text", "cedula"),
                                        rx.button("Sign In", type="submit", background=Color.SECONDARY.value, color=TextColor.BUTTON_TEXT.value,
                                                  _hover={"background": Color.PRIMARY.value}, padding="12px", border_radius="5px"),
                                        rx.cond(
                                            PageState.error_message != "",
                                            rx.text(PageState.error_message, color="red", font_size="14px"),
                                        ),
                                        spacing="15px",
                                    ),
                                    on_submit=PageState.handle_submit_docente,
                                ),
                                padding="30px",
                                background=Color.CONTENT.value,
                                border_radius="12px",
                                box_shadow="rgba(0, 0, 0, 0.1) 0px 4px 8px",
                                margin_top="10px",
                            ),
                            value="login_docente"
                        ),
                        rx.tabs.content(
                            rx.box(
                                rx.form(
                                    rx.vstack(
                                        form_fields("Email", "Enter your email", "text", "username"),
                                        form_fields("Password", "Enter your password", "password", "password"),
                                        rx.button("Sign In", type="submit", background=Color.SECONDARY.value, color=TextColor.BUTTON_TEXT.value,
                                                  _hover={"background": Color.PRIMARY.value}, padding="12px", border_radius="5px"),
                                        rx.cond(
                                            PageState.error_message != "",
                                            rx.text(PageState.error_message, color="red", font_size="14px"),
                                        ),
                                        spacing="15px",
                                    ),
                                    on_submit=PageState.handle_submit_admin,
                                ),
                                padding="30px",
                                background=Color.CONTENT.value,
                                border_radius="12px",
                                box_shadow="rgba(0, 0, 0, 0.1) 0px 4px 8px",
                                margin_top="10px",
                            ),
                            value="login_admin"
                        ),
                    ),
                    background=Color.BACKGROUND.value,
                    padding="40px",
                    border_radius="15px",
                    box_shadow="rgba(0,0,0,0.1) 0px 8px 16px",
                    width="400px",
                    margin="auto",
                ),
                background=Color.BACKGROUND.value,
                height="100vh",
                display="flex",
                justify_content="center",
                align_items="center",
            )
        ),
        background=Color.BACKGROUND.value,
        width="100vw",
        height="100vh",
    )

def form_fields(label: str, placeholder: str, type: str, name: str) -> rx.Component:
    return rx.form.field(
        rx.form.label(label, font_size="lg", font_weight="medium", color=TextColor.HEADER.value),
        rx.input(
            placeholder=placeholder,
            type=type,
            name=name,
            padding="10px",
            border_radius="5px",
            border="1px solid #E0E0E0",
            width="100%",
            background=Color.CONTENT.value,
            color=TextColor.BODY.value,
        ),
        align_items="flex-start",
        width="100%",
        margin_bottom="10px",
    )
 