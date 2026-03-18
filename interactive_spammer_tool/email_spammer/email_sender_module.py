import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys
import config
import time

def send_single_email(sender_email, sender_password, smtp_server, smtp_port, recipient_email, subject, body):
    """Sends a single email."""
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Secure the connection
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print(f"Email sent successfully to {recipient_email}")
        return True
    except smtplib.SMTPAuthenticationError:
        print(f"Authentication Error: Failed to send email to {recipient_email}. Check your email and password in config.py.")
        print("If using Gmail, you might need to enable 'Less secure app access' or use an 'App Password'.")
        return False
    except smtplib.SMTPConnectError:
        print(f"Connection Error: Could not connect to SMTP server {smtp_server}:{smtp_port}. Check server address and port.")
        return False
    except Exception as e:
        print(f"Failed to send email to {recipient_email}: {e}")
        return False

def get_custom_email_details():
    """Gets recipient, subject, and custom message for email."""
    recipient_email = input("Enter the recipient's email address: ")
    subject = input("Enter the email subject: ")
    print("Enter the email body. Press Enter on an empty line to finish:")
    body_lines = []
    while True:
        try:
            line = input()
            if line:
                body_lines.append(line)
            else:
                # Detect double Enter for finishing input
                # This check is a bit tricky in standard input, we'll assume
                # a single empty line signifies the end for simplicity here.
                # For more robust input handling, you might need libraries or
                # more complex logic.
                break
        except EOFError: # Handle end-of-file if input is piped
            break
    body = "\n".join(body_lines)
    return recipient_email, subject, body

def spam_email(recipient_email, subject, body, num_emails=1):
    """Sends multiple emails to a single recipient or a list."""
    print(f"\nStarting email spam to {recipient_email} ({num_emails} emails)...")
    sent_count = 0

    sender_email = config.EMAIL_SENDER_EMAIL
    sender_password = config.EMAIL_SENDER_PASSWORD
    smtp_server = config.EMAIL_SMTP_SERVER
    smtp_port = config.EMAIL_SMTP_PORT

    if not sender_email or not sender_password or sender_email == 'your_test_email@example.com':
        print("\n[ERROR] Email sender credentials not configured in config.py. Please update them.")
        return 0

    for i in range(num_emails):
        print(f"Sending email {i+1}/{num_emails}...")
        if send_single_email(sender_email, sender_password, smtp_server, smtp_port, recipient_email, subject, body):
            sent_count += 1
        if i < num_emails - 1:
            time.sleep(1) # Small delay between sending emails to avoid rate limits
    print(f"Finished email spam. Successfully sent: {sent_count}/{num_emails}")
    return sent_count
