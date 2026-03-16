import reflex as rx
from base import BaseState

class LanguageState(BaseState):
    locale: str = "ko"
    translcations: dict={
        "ko": {
            "dashboard_title": "사용자 대시보드",
            "name": "이름",
            "age": "나이",
            "role": "역할",
            "add_user": "사용자 추가",
            "total_users": "총 사용자 수",
            "login_heading": "로그인",
            "signup_heading": "회원가입",
            "email_placeholder": "이메일",
            "password_placeholder": "비밀번호",
            "password_confirm_placeholder": "비밀번호 확인",
            "login_button": "로그인",
            "signup_button": "회원가입",
            "no_account_yet": "계정이 없으신가요?",
            "signup_link": "회원가입",
            "already_have_account": "이미 계정이 있으신가요?",
            "login_link": "로그인"
        },
        "en": {
            "dashboard_title": "User Dashboard",
            "name": "Name",
            "age": "Age",
            "role": "Role",
            "add_user": "Add User",
            "total_users": "Total Users",
            "login_heading": "Login",
            "signup_heading": "Sign Up",
            "email_placeholder": "Email",
            "password_placeholder": "Password",
            "password_confirm_placeholder": "Confirm Password",
            "login_button": "Login",
            "signup_button": "Sign Up",
            "no_account_yet": "Don't have an account?",
            "signup_link": "Sign Up",
            "already_have_account": "Already have an account?",
            "login_link": "Login"
        },
        "ja": {
            "dashboard_title": "ユーザーダッシュボード",
            "name": "名前",
            "age": "年齢",
            "role": "役割",
            "add_user": "ユーザーを追加",
            "total_users": "総ユーザー数",
            "login_heading": "ログイン",
            "signup_heading": "サインアップ",
            "email_placeholder": "メールアドレス",
            "password_placeholder": "パスワード",
            "password_confirm_placeholder": "パスワード確認",
            "login_button": "ログイン",
            "signup_button": "サインアップ",
            "no_account_yet": "アカウントをお持ちでないですか？",
            "signup_link": "サインアップ",
            "already_have_account": "すでにアカウントをお持ちですか？",
            "login_link": "ログイン"
        },
        "cn": {
            "dashboard_title": "用户仪表板",
            "name": "姓名",
            "age": "年龄",
            "role": "角色",
            "add_user": "添加用户",
            "total_users": "总用户数",
            "login_heading": "登录",
            "signup_heading": "注册",
            "email_placeholder": "电子邮件",
            "password_placeholder": "密码",
            "password_confirm_placeholder": "确认密码",
            "login_button": "登录",
            "signup_button": "注册",
            "no_account_yet": "还没有账户吗？",
            "signup_link": "注册",
            "already_have_account": "已经有账户了？",
            "login_link": "登录"    
        }
    }

    def set_locale(self, lang: str):
        self.locale = lang

    @rx.var
    def t(self) -> dict:
        return self.translcations.get(self.locale, self.translcations["ko"])