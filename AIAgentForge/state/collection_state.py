import reflex as rx
from .base import BaseState

class CollectionState(BaseState):
    """
    컬렉션 관련 상태를 관리하는 클래스.
    컬렉션 생성, 삭제, 업데이트 등 컬렉션과 관련된 모든 상태 변수와 이벤트 핸들러 정의.
    """

    # UI 구동 핵심 상태 변수들
    collections: list[dict] = []
    is_loading: bool = False
    new_collection_name: str = ""

    # 사용자 피드백을 위한 상태 변수
    show_alert: bool = False
    alert_message: str = ""

    async def load_collections(self):
        """
        컬렉션 목록을 서버에서 불러오는 이벤트 핸들러.
        """
        self.is_loading = True
        yield

        try:
            # 여기에 실제 API 호출 로직을 구현해야 합니다.
            client = await self._get_authenticated_client()
            response = await client.from_("collections").select("*").eq("owner_id", self.user.id).order("created_at", desc=True).execute()
            self.collections = response.data if response.data else []
        except Exception as e:
            self.alert_message = "컬렉션을 불러오는 중 오류가 발생했습니다: " + str(e)
            self.show_alert = True
        finally:
            self.is_loading = False
            yield
    
    async def create_collection(self):
        """
        새로운 컬렉션을 생성하는 이벤트 핸들러.
        """
        if not self.new_collection_name.strip():
            self.alert_message = "컬렉션 이름을 입력해주세요."
            self.show_alert = True
            yield
            return
        
        self.is_loading = True
        yield

        success = False
        try:
            client = await self._get_authenticated_client()
            response = await client.from_("collections").insert({
                "name": self.new_collection_name,
                "owner_id": self.user.id
            }).execute()
            
            # 입력 필드 초기화
            self.new_collection_name = ""
            self.show_alert = True
            success = True

            yield CollectionState.load_collections() # 컬렉션 목록 새로고침
        except Exception as e:
            self.alert_message = "컬렉션을 생성하는 중 오류가 발생했습니다: " + str(e)
            self.show_alert = True
        finally:
            self.is_loading = False
            yield

        # if success:
        #     yield CollectionState.load_collections()

    async def delete_collection(self, collection_id: int):
        """
        컬렉션을 삭제하는 이벤트 핸들러.
        """
        self.is_loading = True
        yield

        success = False
        try:
            client = await self._get_authenticated_client()
            await client.from_("collections").delete().eq("id", collection_id).execute()
            self.alert_message = "컬렉션이 성공적으로 삭제되었습니다."
            self.show_alert = True
            success = True

            yield CollectionState.load_collections()
        except Exception as e:
            self.alert_message = "컬렉션을 삭제하는 중 오류가 발생했습니다: " + str(e)
            self.show_alert = True
        finally:
            self.is_loading = False
            yield

        # if success:
        #     yield CollectionState.load_collections()