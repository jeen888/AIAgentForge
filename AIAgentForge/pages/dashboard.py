import reflex as rx
from AIAgentForge.state.dashboard_state import DashboardState

def dashboard_page() -> rx.Component:
    return rx.container(
        rx.vstack(
            # 1. 제목
            rx.heading("사용자 대시보드", size="8", margin_bottom="1em"),

            # 총 사용자 수 표시
            # rx.text(f"총 사용자 수: {len(DashboardState.users)}", size="md", color="gray.500", margin_bottom="1em"),
            rx.text(f"총 사용자 수: {DashboardState.total_users} 명", size="6"),

            # 2. 테이블 (데이터 표시 영역)
            rx.table.root(
                rx.table.header(
                    rx.table.row(
                        rx.table.column_header_cell("이름"),
                        rx.table.column_header_cell("나이"),
                        rx.table.column_header_cell("역할"),
                    )
                ),
                rx.table.body(
                    rx.foreach(
                        DashboardState.users,
                        lambda user: rx.table.row(
                            rx.table.cell(user["name"]),
                            rx.table.cell(user["age"]),
                            rx.table.cell(user["role"]),
                        )
                    )
                ),
                width="100%",
                variant="surface", # 사진처럼 깔끔한 테두리 효과
            ),

            rx.divider(), # 테이블과 폼 사이에 구분선 추가

            # recharts 막대 그래프 추가 (예시 데이터 사용
            rx.recharts.bar_chart(
                rx.recharts.bar(
                    data_key="age", stroke="#8884d8", fill="#8884d8"
                ),
                rx.recharts.x_axis(data_key="name"),
                rx.recharts.y_axis(),
                data=DashboardState.users,
                width="100%",
                height=300
            ),

            # 3. 입력 폼 (데이터 입력 영역)
            # 테이블 바로 아래에 위치하도록 vstack의 자식으로 배치합니다.
            rx.form(
                rx.hstack(
                    rx.input(placeholder="이름", name="name", required=True, flex="1"),
                    rx.input(placeholder="나이", name="age", type="number", required=True, flex="1"),
                    rx.input(placeholder="역할", name="role", required=True, flex="1"),
                    rx.button("사용자 추가", type="submit", color_scheme="blue"),
                    rx.button("리셋", type="button", color_scheme="red"),
                    width="100%",
                    spacing="3",
                    margin_top="1em",
                ),
                on_submit=DashboardState.add_user,
                reset_on_submit=True,
                width="100%",
            ),

            spacing="5",
            align="center",
            width="100%",
            max_width="600px", # 너무 퍼지지 않게 적절한 너비 설정
        ),
        padding_top="5em",
    )
    # return rx.container(
    #     rx.heading("사용자 대시보드", size="8"),
    #     rx.table.root(
    #         rx.table.header(
    #             rx.table.row(
    #                 rx.table.column_header_cell("이름"),
    #                 rx.table.column_header_cell("나이"),
    #                 rx.table.column_header_cell("역할"),
    #             )
    #         ),
    #         # 테이블 본문을 추가하고 상태와 연결.
    #         rx.table.body(
    #             rx.foreach(
    #                 DashboardState.users,
    #                 lambda user: rx.table.row(
    #                     rx.table.cell(user["name"]),
    #                     rx.table.cell(user["age"]),
    #                     # rx.table.cell(str(user["age"])),
    #                     rx.table.cell(user["role"]),
    #                 )
    #             )
    #         ),
    #         rx.divider(),
    #         rx.form(
    #             rx.hstack(
    #                 rx.input(placeholder="이름", name="name", required=True),
    #                 rx.input(placeholder="나이", name="age", type="number", required=True),
    #                 rx.input(placeholder="역할", name="role", required=True),
    #                 rx.button("사용자 추가", type="submit"),
    #                 justify="center"
    #             ),
    #             on_submit=DashboardState.add_user,
    #             reset_on_submit=True
    #         ),
    #         spacing="5",
    #         align="center",
    #         padding_y="2em"
    #     )
    # )