import reflex as rx

from AIAgentForge.pages.collections import render_creation_form
from AIAgentForge.state.collection_state import CollectionState

def render_collection_item(collection: dict) -> rx.Component:
    return rx.card(
        rx.hstack(
            rx.vstack(
                rx.heading(collection["name"], size="5"),
                rx.text(f"Created at: {collection['created_at']}"),
                align_items="start",
            ),
            rx.spacer(),
            rx.button(
                "Delete",
                on_click=lambda: CollectionState.delete_collection(collection["id"]),
                color_scheme="red",
                variant="soft", 
            ),
            align_items="center",
            width="100%",
        ),
        width="100%",
    )

def render_collections_list() -> rx.Component:
    return rx.cond(
        CollectionState.is_loading,
        rx.center(rx.spinner(size="3")),
        rx.cond(
            CollectionState.collections,
            rx.vstack(
                rx.foreach(CollectionState.collections, render_collection_item),
                spacing="4",
                width="100%",
            ),
            rx.center(
                rx.text("No collections found. Create your first collection!"),
                padding_y="4em",
            )
        )
    )

def collections_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Your Collections", size="8", margin_bottom="1em"),
            render_creation_form(),
            rx.divider(margin_y="2em"),
            render_collections_list(),
            spacing="5",
            width="100%",
            max_width="60em",
            padding_top="2em",
        ),
        size="4",
    )