import reflex as rx
from AIAgentForge.state.collection_state import CollectionState

def render_creation_form() -> rx.Component:
    return rx.form(
        rx.hstack(
            rx.input(
                placeholder="Collection Name", 
                value=CollectionState.new_collection_name,
                on_change=CollectionState.set_new_collection_name,
                flex_grow=1,
            ),
            rx.button(
                "Create Collection", 
                type="submit", 
                is_loading=CollectionState.is_loading,
            ),
            spacing="4",
        ),
        on_submit=CollectionState.create_collection,
        width="100%",
    )