"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from grupal.component.navbar import navbar
from grupal.component.header import header
from grupal.component.footer import pie_de_pagina

from rxconfig import config

class State(rx.State):
    """The app state."""

    ...

def index() -> rx.Component:
    # Welcome Page (Index)
    trabajos = [
        {
            'titulo': 'Reserva de aulas',
            'descripcion': 'Proyecto de gestion de aulas y espacios fisicos de la UIDE',
            'imagen_url': 'iconos/youtube.png',
        },
        {
            'titulo': 'Sistema GPR',
            'descripcion': 'Proyecto de gestion de notas de docentes de la UIDE',
            'imagen_url': 'iconos/youtube.png',
        },
        {
            'titulo': 'Sistema Practicas',
            'descripcion': 'Proyecto de gestion de practicas laborales de la UIDE',
            'imagen_url': 'iconos/youtube.png',
        },
        {
            'titulo': 'Sistema Practicas II',
            'descripcion': 'Proyecto de gestion de practicas laborales de la UIDE',
            'imagen_url': 'iconos/youtube.png',
        },
    ]

    

    return rx.container(
        rx.color_mode.button(position="top-right"),
         rx.vstack(
            navbar(),
            header(),
            pie_de_pagina(),
        ),
        rx.logo(),
    )


app = rx.App()
app.add_page(index)
