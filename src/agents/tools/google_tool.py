from google.oauth2 import service_account
from googleapiclient.discovery import build
from langchain.tools import tool
import os

class GoogleTool():
    def __init__(self):
        self.USER_EMAIL = os.getenv("USER_GOOGLE_EMAIL")
        self.GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS") or "credentials.json"
        self.creds = service_account.Credentials.from_service_account_file(
            self.GOOGLE_APPLICATION_CREDENTIALS,
            scopes=["https://www.googleapis.com/auth/calendar"],
        )   
        self.service = build("calendar", "v3", credentials=self.creds)

    @tool()
    def create_calendar_event(
            self,
            summary: str,
            start_time: str,
            end_time: str,
            description: str = ""
    )->str:
        try:

            event_body = {
                "summary": summary,
                "description": description,
                "start": {
                    "dateTime": start_time,
                    "timeZone": "Asia/Taipei",
                },
                "end": {
                    "dateTime": end_time,
                    "timeZone": "Asia/Taipei",
                }
            }
            
            created_event = self.service.events().insert(
                calendarId=self.USER_EMAIL,
                body=event_body,
                sendUpdates="all"
            ).execute()

            return f"事件建立成功：{created_event.get('htmlLink')}"
        except Exception as e:
            return f"行事曆建立失敗:{e}"