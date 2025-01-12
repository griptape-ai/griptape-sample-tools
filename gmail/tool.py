from google.oauth2 import service_account
from googleapiclient.discovery import build
from typing import List, Dict
import os
from schema import Schema
from griptape.artifacts import ListArtifact, JsonArtifact
from griptape.tools import BaseTool
from griptape.utils.decorators import activity

# JSON config approach
SERVICE_ACCOUNT_INFO = {
    "type": "service_account",
    "project_id": os.getenv('GOOGLE_PROJECT_ID'),
    "private_key_id": os.getenv('GOOGLE_PRIVATE_KEY_ID'),
    "private_key": os.getenv('GOOGLE_PRIVATE_KEY'),
    "client_email": os.getenv('GOOGLE_CLIENT_EMAIL'),
    "client_id": os.getenv('GOOGLE_CLIENT_ID'),
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": f"https://www.googleapis.com/robot/v1/metadata/x509/{os.getenv('GOOGLE_CLIENT_EMAIL').replace('@', '%40')}"
}

class GmailTool(BaseTool):
    @activity(
        config={
            "description": "Lists unread emails from Gmail inbox using service account credentials"
        }
    )
    def list_unread_emails(self, params: dict) -> ListArtifact:
        """Lists unread emails from Gmail inbox using service account credentials."""
        credentials = service_account.Credentials.from_service_account_info(
            SERVICE_ACCOUNT_INFO,
            scopes=['https://www.googleapis.com/auth/gmail.readonly']
        )
        
        delegated_credentials = credentials.with_subject(os.getenv('GOOGLE_DELEGATED_EMAIL'))
        
        service = build('gmail', 'v1', credentials=delegated_credentials)
        
        results = service.users().messages().list(
            userId='me',
            q='is:unread',
            labelIds=['INBOX'],
            maxResults=10
        ).execute()

        messages = results.get('messages', [])
        emails = []
        
        for message in messages:
            msg = service.users().messages().get(
                userId='me', 
                id=message['id'],
                format='metadata',
                metadataHeaders=['From', 'Subject', 'Date']
            ).execute()

            headers = msg['payload']['headers']
            email_data = {
                'id': msg['id'],
                'date': next(h['value'] for h in headers if h['name'] == 'Date'),
                'from': next(h['value'] for h in headers if h['name'] == 'From'),
                'subject': next(h['value'] for h in headers if h['name'] == 'Subject'),
                'has_attachments': bool(msg['payload'].get('parts', []))
            }
            emails.append(JsonArtifact(email_data))
            
        return ListArtifact(emails)

def init_tool() -> BaseTool:
    return GmailTool()