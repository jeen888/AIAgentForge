import reflex as rx
import os
from gotrue.types import User
from supabase import create_client, Client
from typing import ClassVar

class BaseState(rx.State):
    """
    모든 상태 클래스의 기반이 되는 기본 상태.
    앱 전역에서 사용될 상태 변수나 이벤트 핸들러 정의.
    """
    is_authenticated: bool = False
    user: User | None = None
    access_token: str = rx.Cookie("")
    refresh_token: str = rx.Cookie("")

    # Supabase 클라이언트 인스턴스를 클래스 변수로 정의
    supabase_client: ClassVar[Client] = create_client(
        os.getenv("SUPABASE_URL", "http://localhost:8000"),
        os.getenv("SUPABASE_ANON_KEY", "sb_publishable_ACJWlzQHlZjBrEguHvfOxg_3BJgxAaH")
    )