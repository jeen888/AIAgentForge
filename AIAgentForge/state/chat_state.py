import reflex as rx
from AIAgentForge.state.base import BaseState
import os
from google import genai  # 최신 google-genai 패키지 사용
from pydantic import BaseModel # rx.Base 대신 사용
from dotenv import load_dotenv

load_dotenv()

# Message 모델 정의: rx.Base 대신 pydantic.BaseModel 사용 (경고 해결)
class Message(BaseModel):
    role: str
    content: str

class ChatState(BaseState):
    question: str = ""
    chat_history: list[Message] = []

    def set_question(self, question: str):
        self.question = question

    @rx.event
    async def answer(self):
        if not self.question.strip():
            yield rx.window_alert("질문을 입력해주세요.")
            return

        # 사용자 메시지 추가
        self.chat_history.append(Message(role="user", content=self.question))
        user_input = self.question
        self.question = ""
        yield

        try:
            client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
            
            answer_text = ""
            self.chat_history.append(Message(role="assistant", content=answer_text))
            yield

            # 모델 이름을 아래와 같이 변경하여 시도
            response = await client.aio.models.generate_content_stream(
                model="models/gemini-flash-latest",  # 최신 모델 이름으로 변경
                contents=user_input,
            )
            # for m in client.models.list():
            #     print(m.name)
    
            async for chunk in response:
                if chunk.text:
                    answer_text += chunk.text
                    # 마지막 메시지 실시간 업데이트
                    self.chat_history[-1] = Message(role="assistant", content=answer_text)
                    yield

        except Exception as e:
            yield rx.window_alert(f"Gemini API 오류가 발생했습니다: {str(e)}")

# models/gemini-2.5-flash
# models/gemini-2.5-pro
# models/gemini-2.0-flash
# models/gemini-2.0-flash-001
# models/gemini-2.0-flash-lite-001
# models/gemini-2.0-flash-lite
# models/gemini-2.5-flash-preview-tts
# models/gemini-2.5-pro-preview-tts
# models/gemma-3-1b-it
# models/gemma-3-4b-it
# models/gemma-3-12b-it
# models/gemma-3-27b-it
# models/gemma-3n-e4b-it
# models/gemma-3n-e2b-it
# models/gemini-flash-latest
# models/gemini-flash-lite-latest
# models/gemini-pro-latest
# models/gemini-2.5-flash-lite
# models/gemini-2.5-flash-image
# models/gemini-2.5-flash-lite-preview-09-2025
# models/gemini-3-pro-preview
# models/gemini-3-flash-preview
# models/gemini-3.1-pro-preview
# models/gemini-3.1-pro-preview-customtools
# models/gemini-3.1-flash-lite-preview
# models/gemini-3-pro-image-preview
# models/nano-banana-pro-preview
# models/gemini-3.1-flash-image-preview
# models/gemini-robotics-er-1.5-preview
# models/gemini-2.5-computer-use-preview-10-2025
# models/deep-research-pro-preview-12-2025
# models/gemini-embedding-001
# models/gemini-embedding-2-preview
# models/aqa
# models/imagen-4.0-generate-001
# models/imagen-4.0-ultra-generate-001
# models/imagen-4.0-fast-generate-001
# models/veo-2.0-generate-001
# models/veo-3.0-generate-001
# models/veo-3.0-fast-generate-001
# models/veo-3.1-generate-preview
# models/veo-3.1-fast-generate-preview
# models/gemini-2.5-flash-native-audio-latest
# models/gemini-2.5-flash-native-audio-preview-09-2025
# models/gemini-2.5-flash-native-audio-preview-12-2025

# import reflex as rx
# from AIAgentForge.state.base import BaseState
# import os
# import openai
# from dotenv import load_dotenv  # python-dotenv import 추가

# # .env 파일 로드
# load_dotenv()

# # OpenAI API 키 설정 (환경 변수에서 가져오기), 구 방식
# # openai.api_key = os.getenv("OPENAI_API_KEY")

# # Message 모델 정의: 채팅 메시지의 구조 명확히 하기 위해 Pydantic 모델 사용
# class Message(rx.Base):
#     role: str  # 'user' 또는 'assistant'
#     content: str  # 메시지 내용

# class ChatState(BaseState):
#     """
#     채팅 페이지의 상태를 관리하는 클래스.
#     채팅에서 필요한 모든 상태 변수와 이벤트 핸들러 정의.
#     """
#     # 사용자의 현재 입력(Base Var)
#     question: str = ""
#     chat_history: list[Message] = []  # 채팅 메시지 목록을 저장할 기본 변수(Base Var).

#     def set_question(self, question: str):
#         self.question = question

#     # chat_history: list[Message] = []  # 채팅 메시지 목록을 저장할 기본 변수(Base Var).
    
#     @rx.event
#     async def answer(self): # async는 return에 데이터를 포함할 수 없다.
#         if not self.question.strip():
#             yield rx.window_alert("질문을 입력해주세요.")
#             return
        
#         self.chat_history.append(Message(role="user", content=self.question))
#         # self.chat_history.append(Message(role="assistant", content=f"You said: {self.question}"))
#         # self.question = ""  # 질문 입력 초기화
#         yield

#         session=None
#         try:
#             # 기존 로직...
#             client = openai.AsyncOpenAI(api_key=os.environ["OPENAI_API_KEY"])
#             session=await client.chat.completions.create(
#                 model="gpt-4o-mini",
#                 messages=[
#                     {"role": "user", "content": self.question}
#                 ],
#                 stop=None,
#                 temperature=0.7,
#                 stream=True,
#             )
#             # ... API 호출 부분 ...
#         except openai.RateLimitError:
#             yield rx.window_alert("OpenAI API 잔액이 부족합니다. 결제 상태를 확인해주세요.")
#         except Exception as e:
#             yield rx.window_alert(f"오류가 발생했습니다: {str(e)}")


#         self.question = ""  # 질문 입력 초기화

#         answer=""
#         self.chat_history.append(Message(role="assistant", content=answer))  # 빈 답변으로 초기 메시지 추가
#         yield

#         if session is not None:
#             async for item in session:
#                 if hasattr(item.choices[0].delta, "content"):
#                     if item.choices[0].delta.content is None:
#                         break
#                     answer += item.choices[0].delta.content
#                     self.chat_history[-1]=(
#                         Message(role="assistant", content=answer)
#                     )
#                     yield
#         else:
#             yield # rx.window_alert("응답을 받지 못했습니다. 다시 시도해주세요.")