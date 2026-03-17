import reflex as rx

from AIAgentForge.pages.collections_page import collections_page

try:
    from AIAgentForge.pages.dashboard import dashboard_page
except ImportError:
    from pages.dashboard import dashboard_page

from AIAgentForge.pages.chat import chat_page
from AIAgentForge.pages.login import login_page
from AIAgentForge.pages.signup import signup_page
from AIAgentForge.state.auth_state import AuthState

# 앱 인스턴스 생성, 테마, 스타일시트 등 앱 전반의 설정을 여기서 할 수 있음.
app=rx.App()

# 보호된 라우트에 on_load 이벤트 핸들러를 추가하여 인증 상태를 확인하고, 인증되지 않은 사용자를 로그인 페이지로 리디렉션합니다.
app.add_page(dashboard_page, route="/", on_load=AuthState.check_auth)
app.add_page(chat_page, route="/chat", on_load=AuthState.check_auth)
app.add_page(collections_page, route="/collections", on_load=AuthState.check_auth)

# 공개 라우트
app.add_page(login_page, route="/login")
app.add_page(signup_page, route="/signup")

# 페이지 컴포넌트를 URL 경로에 추가(라우팅)합니다.
# 여기서는 루트 URL("/")에 대시보드 페이지를 연결합니다.
# app.add_page(dashboard_page, path="/")
# app.add_page(dashboard_page, route="/")

# 새로운 채팅 페이지를 '/chat' 경로에 추가합니다.
# app.add_page(chat_page, route="/chat")

# 인증 관련 페이지를 추가합니다
# app.add_page(login_page, route="/login")
# app.add_page(signup_page, route="/signup")


# """Welcome to Reflex! This file outlines the steps to create a basic app."""

# import reflex as rx

# from rxconfig import config


# class State(rx.State):
#     """The app state."""


# def index() -> rx.Component:
#     # Welcome Page (Index)
#     return rx.container(
#         rx.color_mode.button(position="top-right"),
#         rx.vstack(
#             rx.heading("Welcome to Reflex!", size="9"),
#             rx.text(
#                 "Get started by editing ",
#                 rx.code(f"{config.app_name}/{config.app_name}.py"),
#                 size="5",
#             ),
#             rx.link(
#                 rx.button("Check out our docs!"),
#                 href="https://reflex.dev/docs/getting-started/introduction/",
#                 is_external=True,
#             ),
#             spacing="5",
#             justify="center",
#             min_height="85vh",
#         ),
#     )


# app = rx.App()
# app.add_page(index)
