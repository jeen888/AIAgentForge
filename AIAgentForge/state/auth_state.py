import reflex as rx
from gotrue.types import User
from base import BaseState

class AuthState(BaseState):
    """
    인증 상태를 관리하는 클래스.
    로그인, 로그아웃, 사용자 정보 저장 등 인증과 관련된 모든 상태 변수와 이벤트 핸들러 정의.
    """
    is_authenticated: bool = False
    user: User | None = None   
    error_message: str = ""
    is_loading: bool = False

    # JWT 토큰을 저장할 변수 추가
    access_token: str = rx.Cookie("")
    refresh_token: str = rx.Cookie("")