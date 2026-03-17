import reflex as rx
from AIAgentForge.state.auth_state import AuthState

def login_page() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.heading("Login", size="8"),
            
            # 1. rx.form 내부는 반드시 하나의 레이아웃(vstack 등)으로 감싸야 합니다.
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
                    rx.button(
                        "Login", 
                        type="submit", 
                        color_scheme="blue", 
                        width="300px", 
                        is_loading=AuthState.is_loading
                    ),
                    spacing="4", # 요소 사이 간격
                ),
                on_submit=AuthState.handle_login,
            ),
            
            # 2. 에러 메시지 처리
            rx.cond(
                AuthState.error_message != "",
                rx.callout(
                    AuthState.error_message,
                    icon="info", # Radix Themes에 맞는 아이콘으로 변경
                    color_scheme="red",
                    width="100%",
                )
            ),
            
            # 3. 하단 링크
            rx.text(
                "Don't have an account? ",
                rx.link("Sign Up", href="/signup"),
                " 하세요.",
                size="2",
            ),
            
            spacing="5",
            align="center",
            width="350px", # 전체 컨텐츠 너비 고정
            padding="2em",
            border="1px solid #eaeaea", # 외곽선 추가 (선택 사항)
            border_radius="10px",
        ),
        width="100%",
        height="100vh", # 화면 중앙 정렬을 위해 높이 설정
    )