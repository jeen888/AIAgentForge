import reflex as rx
from AIAgentForge.state.dashboard_state import DashboardState

def dashboard_page() -> rx.Component:
    """
    대시보드의 메인페이지 UI를 정의하는 컴포넌트 함수.
    """
    return rx.container(
        rx.heading("사용자 대시보드", size="8"),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("이름"),
                    rx.table.column_header_cell("나이"),
                    rx.table.column_header_cell("역할"),
                )
            ),
            # 테이블 본문을 추가하고 상태와 연결.
            rx.table.body(
                rx.foreach(
                    DashboardState.users,
                    lambda user: rx.table.row(
                        rx.table.cell(user["name"]),
                        rx.table.cell(user["age"]),
                        # rx.table.cell(str(user["age"])),
                        rx.table.cell(user["role"]),
                    )
                )
            ),
            rx.divider(),
            rx.hstack(
                rx.input(placeholder="이름", name="name"),
                rx.input(placeholder="나이", name="age", type="number"),
                rx.input(placeholder="역할", name="role"),
                rx.button("사용자 추가"),
                justify="center",
            ),
            spacing="5",
            align="center",
            padding_y="2em"
        )
    )