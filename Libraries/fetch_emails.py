import email
import os
from email.header import decode_header
from unidecode import unidecode
from imapclient import IMAPClient, SEEN
from Variables.config import (NOW)
from Libraries.logger import get_logger

logger = get_logger(__name__)

IMAP_SERVER = os.environ["IMAP_SERVER"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]

# Conectando-se ao servidor IMAP
imap_conn = IMAPClient(IMAP_SERVER, ssl=True)
imap_conn.login(EMAIL, PASSWORD)


def fetch_emails():
    imap_conn.select_folder('INBOX', readonly=True)

    # Pesquisa por emails não lidos
    messages = imap_conn.search(['UNSEEN'])

    subjects = []
    # Loop through the unread messages
    for uid, message_data in imap_conn.fetch(messages, 'RFC822').items():
        email_message = email.message_from_bytes(message_data[b'RFC822'])

        # Decode the subject header
        subject_header = decode_header(email_message['Subject'])[0]
        subject_bytes = subject_header[0]
        subject_encoding = subject_header[1]

        try:
            # Convert subject to UTF-8
            if subject_encoding is None:
                subject = subject_bytes.decode('utf-8')
            else:
                subject = subject_bytes.decode(subject_encoding)
        except:
            subject = str(subject_header[0])

        # Convert subject to PT-BR
        subject = unidecode(subject)

        # Append the decoded subject to the list of subjects
        subjects.append(subject)

    # marcando os e-mails encontrados como lidos
    # imap_conn.set_flags(messages, [SEEN])
    imap_conn.logout()

    return subjects