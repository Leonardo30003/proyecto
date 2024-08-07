import reflex as rx

# Definición de las funciones para manejar los clics
def registrar_entrada():
    return rx.toast.success("Registro de entrada exitoso")

def registrar_salida():
    return rx.toast.success("Registro de salida exitoso")

@rx.page(route="/vista_docente")
def vista_docente_page() -> rx.Component:
    return rx.container(
        rx.text("Vista del Docente", font_size="24px", color="black", margin_bottom="20px"),
        
        # Foto de perfil
        rx.image(
            src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR1VrYUGacRSnrwIe29Dtps4kO4WxwajfgenQ&s",
            alt="Foto de perfil",
            width="150px",
            height="150px",
            border_radius="50%",
            margin_bottom="20px"
        ),

        # Nombres y apellidos
        rx.text("Nombres y Apellidos: Juan Pérez", font_size="18px", color="black", margin_bottom="10px"),
        
        # Horario
        rx.text("Horario: Lunes a Viernes, 8:00 AM - 4:00 PM", font_size="18px", color="black", margin_bottom="10px"),
        
        # Facultad
        rx.text("Facultad: Facultad de Ingeniería", font_size="18px", color="black", margin_bottom="10px"),
        
        # Materias impartidas
        rx.text("Materias Impartidas: Programación, Bases de Datos, Redes", font_size="18px", color="black", margin_bottom="20px"),
        
        # Botón para registrar entrada
        rx.button(
            "Registrar Entrada",
            on_click=rx.toast.success("Registro de entrada exitoso"),
            margin_right="10px",
            padding="10px",
            font_size="16px"
        ),
        
        # Botón para registrar salida
        rx.button(
            "Registrar Salida",
            on_click=rx.toast.success("Registro de salida exitoso"),
            padding="10px",
            font_size="16px"
        ),
        
        align_items="center",
        justify_content="center",
        padding="20px",
        border="1px solid #E0E0E0",
        border_radius="10px",
        box_shadow="0px 0px 10px rgba(0, 0, 0, 0.1)",
        background="#FFFFFF",
        height="100vh",  # Ajusta la altura para ocupar toda la ventana
        display="flex",
        flex_direction="column"
    )
