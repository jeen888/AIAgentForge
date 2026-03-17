import reflex as rx
from gotrue.types import User
from .base import BaseState
# from AIAgentForge.state.base import BaseState

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

    async def handle_login(self, form_data: dict):
        """
        로그인 폼 제출 시 호출되는 이벤트 핸들러.
        form_data: 로그인 폼에서 입력된 데이터 (예: 이메일, 비밀번호)
        """
        self.is_loading = True
        self.error_message = ""
        yield

        try:
            # supabaase_client는 BaseState에 정의된 전역 client instance라고 가정
            response = await self.supabase_client.auth.sign_in_with_password({
                "email": form_data["email"],
                "password": form_data["password"],
            })
            if response.session:
                self.access_token = response.session.access_token
                self.refresh_token = response.session.refresh_token
                self.is_authenticated = True
                self.user = response.user
            else:
                self.error_message = "Login failed: " + (response.error.message if response.error else "Unknown error")
        except Exception as e:
            self.error_message = "Login error: " + str(e)
        finally:
            self.is_loading = False
            yield # 에러 발생시 상태 업데이트를 위해 yield 추가

    async def handle_signup(self, form_data: dict):
        """
        회원가입 폼 제출 시 호출되는 이벤트 핸들러.
        form_data: 회원가입 폼에서 입력된 데이터 (예: 이메일, 비밀번호, 비밀번호 확인)
        """
        self.is_loading = True
        self.error_message = ""
        yield

        if form_data["password"] != form_data["password_confirm"]:
            self.error_message = "Passwords do not match."
            self.is_loading = False
            yield
            return

        try:
            response = await self.supabase_client.auth.sign_up({
                "email": form_data["email"],
                "password": form_data["password"],
            })
            if response.user:
                if response.session:
                    self.access_token = response.session.access_token
                    self.refresh_token = response.session.refresh_token
                    self.is_authenticated = True
                    self.user = response.user
                    self.is_loading = False
                    yield
                else:
                    self.error_message = "이메일 인증이 필요합니다. 메일함을 확인해주세요."
                    self.is_loading = False
                    yield rx.redirect("/login")
                    return # 함수 종료
            else:
                self.error_message = "Signup failed: " + (response.error.message if response.error else "Unknown error")
        except Exception as e:
            self.error_message = "Signup error: " + str(e)
        finally:
            self.is_loading = False
            yield # 에러 발생시 상태 업데이트를 위해 yield 추가

    async def check_auth(self):
        """
        앱 초기화 시 호출되어 사용자의 인증 상태를 확인하는 이벤트 핸들러.
        쿠키에 저장된 토큰을 사용하여 사용자 정보를 가져오고 인증 상태를 업데이트.
        """
        self.is_loading = True
        yield

        if not self.access_token:
            if self.is_authenticated:
                self.is_authenticated = False
                self.user = None
            yield rx.redirect("/login") # 인증되지 않은 사용자는 로그인 페이지로 리디렉션
            return
        
        try:
            # supabase_client.auth.get_user는 보통 비동기 함수이므로 await를 확인해보세요.
            response = await self.supabase_client.auth.get_user(self.access_token)
            self.user = response.user
            self.is_authenticated = True
            yield
        except Exception as e:
            if not self.refresh_token:
                self.access_token = ""
                self.is_authenticated = False
                self.user = None
                # 수정된 부분: return 대신 yield 사용
                yield rx.redirect("/login")
                return 
            
            try:
                # refresh_session 역시 비동기일 가능성이 높으므로 await 확인
                response = await self.supabase_client.auth.refresh_session(self.refresh_token)
                self.access_token = response.session.access_token
                self.refresh_token = response.session.refresh_token
                self.user = response.user
                self.is_authenticated = True
                yield
            except Exception as refresh_error:
                self.access_token = ""
                self.refresh_token = ""
                self.is_authenticated = False
                self.user = None
                yield rx.redirect("/login")

    async def handle_logout(self):
        self.is_loading = True
        yield

        await self.supabase_client.auth.sign_out()
        self.access_token = ""
        self.refresh_token = ""
        self.is_authenticated = False
        self.user = None
        self.is_loading = False
        yield rx.redirect("/login") # 로그아웃 후 로그인 페이지로 리디렉션