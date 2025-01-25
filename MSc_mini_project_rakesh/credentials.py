import os
import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

# Set up Gmail API credentials
credentials = Credentials.from_authorized_user_file('client_secret_334849614598-fip3auae19bq8hakdr4k003rqq7f6ni3.apps.googleusercontent.com(1).json', ['https://www.googleapis.com/auth/gmail.readonly'])
gmail_service = build('gmail', 'v1', credentials=credentials)

# Search for unread emails
query = "is:unread"  # Search query for unread emails
results = gmail_service.users().messages().list(q=query, userId='me').execute()
messages = results.get('messages', [])

# Process emails
if not messages:
    print('No unread emails found.')
else:
    print(f'Number of Unread Emails: {len(messages)}')
    for msg in messages:
        email = gmail_service.users().messages().get(userId='me', id=msg['id']).execute()
        email_payload = email['payload']

        # Extract email details
        email_headers = email_payload['headers']
        email_subject = None
        email_from = None

        # Parse email headers to get subject and sender
        for header in email_headers:
            if header['name'] == 'Subject':
                email_subject = header['value']
            elif header['name'] == 'From':
                email_from = header['value']

        print(f'Subject: {email_subject}')
        print(f'From: {email_from}')

        # Process transaction verification logic
        # Add your custom logic here for verifying transactions based on email contents

        # Mark email as read
       
        print('-----')


