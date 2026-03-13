try:
    from AIAgentForge.state.base import BaseState
except ImportError:
    from base import BaseState

class DashboardState(BaseState):
    """
    대시보드 페이지의 상태를 관리하는 클래스.
    대시보드에서 필요한 모든 상태 변수와 이벤트 핸들러 정의.
    """
    # 사용자 목록을 저장할 기본 변수(Base Var).
    # 초기 데이터로 두 명의 사용자를 하드 코딩.
    users: list[dict] = [
        {"name": "존 도", "age": 30, "role": "개발자"},
        {"name": "제인 도", "age": 28, "role": "디자이너"},
    ]

    def add_user(self, form_data: dict):
        if not form_data.get("name") or not form_data.get("age") or not form_data.get("role"):
            return rx.window_alert("모든 필드를 입력해주세요.")

        self.users.append({
            "name": form_data["name"],
            "age": form_data["age"],
            "role": form_data["role"],
        })
    pass