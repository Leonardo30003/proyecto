import reflex as rx
import asyncio

def notificacion_componente(message: str, icon_notify: str, color: str) -> rx.Component:
    return rx.callout(
        message,
        icon=icon_notify,
        style = estilo_notificacion,
        color_scheme = color,
    )

estilo_notificacion ={
    'position': "fixed",
    'top': "10px",
    'right': "10px",
    'margin': "10px 10px",
}