from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import os
import datetime

SCOPES = ['https://www.googleapis.com/auth/calendar']

class CalendarManager:
    def __init__(self):
        self.service = self.authenticate()

    def authenticate(self):
        creds = None
        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            with open('token.json', 'w') as token:
                token.write(creds.to_json())
        return build('calendar', 'v3', credentials=creds)

    def add_event(self, summary, location, description, start_time, end_time):
        event = {
            'summary': summary,
            'location': location,
            'description': description,
            'start': {'dateTime': start_time, 'timeZone': 'Europe/Istanbul'},
            'end': {'dateTime': end_time, 'timeZone': 'Europe/Istanbul'},
        }
        created_event = self.service.events().insert(calendarId='primary', body=event).execute()
        print('Randevu oluşturuldu:', created_event.get('htmlLink'))

    def list_events(self):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = self.service.events().list(calendarId='primary', timeMin=now, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])
        if not events:
            print('Hiç randevu bulunamadı.')
            return
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(f"{start}: {event['summary']}")

    def delete_event(self, event_id):
        self.service.events().delete(calendarId='primary', eventId=event_id).execute()
        print("Randevu başarıyla silindi.")

    def update_event(self, event_id, summary=None, description=None, start_time=None, end_time=None):
        event = self.service.events().get(calendarId='primary', eventId=event_id).execute()
        if summary:
            event['summary'] = summary
        if description:
            event['description'] = description
        if start_time:
            event['start']['dateTime'] = start_time
        if end_time:
            event['end']['dateTime'] = end_time
        updated_event = self.service.events().update(calendarId='primary', eventId=event_id, body=event).execute()
        print('Randevu güncellendi:', updated_event.get('htmlLink'))
