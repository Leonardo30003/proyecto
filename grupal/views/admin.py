import reflex as rx

@rx.page(
    route="/vista_admin",
    title="Admin",
)
def dashboard_page() -> rx.Component:
    sidebar_items = [
        {"label": "Usuarios", "active": True},
        {"label": "Horarios", "active": True},
        {"label": "Asignaciones", "active": True},
        {"label": "Actividades", "active": True},
    ]
    
    def sidebar_item(item):
        return rx.box(
            rx.text(item["label"], font_size="1.2em", color="#2A5D7C", padding="1em"),
            background="white" if not item["active"] else "#F8B7C1",  # Light Pink for active items
            width="100%",
            margin_bottom="1em",
            cursor="pointer",
        )
    
    content_items = [
        {"title": "ccc", "description": "ccc"},
        {"title": "ccc", "description": "ccc"},
        {"title": "ccc", "description": "ccc"},
        {"title": "ccc", "description": "ccc"},    ]
    
    def content_card(item):
        return rx.box(
            rx.text(item["title"], font_size="1.2em", color="black", text_align="center"),
            rx.text(item["description"], font_size="1em", color="black", text_align="center"),
            width="200px",
            height="200px",
            margin="1em",
            padding="1em",
            background="white",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
            aspect_ratio="1 / 1",
        )
    
    return rx.box(
        rx.box(
            *[sidebar_item(item) for item in sidebar_items],
            width="20%",
            background="#F8B7C1",  # Light Pink background for sidebar
            padding="2em",
            box_shadow="2px 0 5px rgba(0,0,0,0.1)"
        ),
        rx.box(
            *[content_card(item) for item in content_items],
            display="flex",
            justify_content="center",
            flex_wrap="wrap",
            width="80%",
            padding="2em",
            background="#F0F0F0",  # Light gray for main content background
        ),
        display="flex",
        width="100%",
        height="100vh",
        background="#F0F0F0",  # Same light gray for full background
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    rx.run(dashboard_page)
