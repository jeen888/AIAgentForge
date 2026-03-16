import reflex as rx
from AIAgentForge.state.chat_state import ChatState
from AIAgentForge.components.chat_bubble import chat_bubble

def action_bar() -> rx.Component:
    return rx.center(
        rx.vstack(
            rx.form(
                rx.hstack(
                    rx.input(
                        placeholder="질문을 입력하세요...",
                        value=ChatState.question,
                        on_change=ChatState.set_question,
                        flex_grow="1",
                        width="100%",
                        height="10em",
                        multiple=True,  # 여러 줄 입력 허용
                        align_items="flex-start",  # 입력 필드 상단 정렬
                    ),
                    rx.button("전송", type="submit", color_scheme="blue"),
                ), 
                on_submit=ChatState.answer,
                reset_on_submit=True,  # 폼 제출 후 입력 필드 초기화
                width="100%",
            ),
            position="sticky",
            bottom="0",
            background_color=rx.color("gray", 2),
            width=800,
        )
    )

def chat_page() -> rx.Component:
    return rx.vstack(
        rx.box(
            # rx.foreach를 사용하여 chat_history리스트 순회
            # 각 메시지에 대해 chat_bubble 컴포넌트 렌더링
            rx.foreach(ChatState.chat_history, chat_bubble),
            width="100%",
            padding_x="2em",
            padding_top="2em"
        ),
        rx.spacer(),
        action_bar(),
        align="center",
        width="100%",
        height="100vh", # 전체 화면 높이로 설정하여 하단에 고정된 액션 바와 스크롤 가능한 채팅 영역 확보
    )