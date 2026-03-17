import reflex as rx
from AIAgentForge.state.auth_state import AuthState

def signup_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Create Account", size="8"),
            
            # 1. rx.form으로 감싸고 내부에 vstack을 배치합니다.
            rx.form(
                rx.vstack(
                    rx.input(
                        placeholder="Email", 
                        type="email", 
                        name="email", 
                        required=True, 
                        width="300px"
                    ),
                    rx.input(
                        placeholder="Password", 
                        type="password", 
                        name="password", 
                        required=True, 
                        width="300px"
                    ),
                    rx.input(
                        placeholder="Confirm Password", 
                        type="password", 
                        name="password_confirm", # handle_signup에서 사용하는 이름과 일치해야 함
                        required=True, 
                        width="300px"
                    ),
                    rx.button(
                        "Sign Up", 
                        type="submit", 
                        color_scheme="green", 
                        width="300px", 
                        is_loading=AuthState.is_loading
                    ),
                    spacing="4",
                ),
                on_submit=AuthState.handle_signup, # 여기서 handle_signup 호출
            ),
            
            # 2. 에러 메시지 처리
            rx.cond(
                AuthState.error_message != "",
                rx.callout(
                    AuthState.error_message,
                    icon="triangle_exclamation",
                    color_scheme="red",
                    width="100%",
                )
            ),
            
            # 3. 로그인 페이지 이동 링크
            rx.text(
                "Already have an account? ",
                rx.link("Login", href="/login"),
                size="2",
            ),
            
            spacing="5",
            align="center",
            width="350px",
            padding="2em",
            border="1px solid #eaeaea",
            border_radius="10px",
        ),
        width="100%",
        height="100vh",
    )

# import reflex as rx

# from AIAgentForge.state.auth_state import AuthState

# def signup_page() -> rx.Component:
#     return rx.center(
#         rx.vstack(
#             rx.heading("Sign Up", size="8"),
#             rx.form(
#                 rx.input(placeholder="Email", type="email", name="email", required=True, width="300px"),
#                 rx.input(placeholder="Password", type="password", name="password", required=True, width="300px"),
#                 rx.input(placeholder="Confirm Password", type="password", name="password_confirm", required=True, width="300px"),
#                 rx.button("Sign Up", type="submit", color_scheme="blue", width="300px",
#                           is_loading=AuthState.is_loading),
#                 spacing="4",
#             ),
#             on_submit=AuthState.handle_signup,
#         ),
#         # 에러 메시지가 있을 때만
#         rx.cond(
#             AuthState.error_message != "",
#             rx.callout(
#                 AuthState.error_message,
#                 icon="alert_triangle",
#                 color_scheme="red",
#                 width="100%",
#                 margin_top="1em",
#             )
#         ),
#         rx.text("Already have an account?",
#             rx.link("Login", href="/login", color="blue.500"),
#             " 하세요.",
#             margin_top="1em",
#         ),
#         spacing="5",
#         align="center",
#         width="25em",
#     )