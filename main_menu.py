import os
import sys
import time

# Add the root of the interactive_spammer_tool to the Python path
# This allows imports like 'from .ems_spammer import sms_sender' to work correctly
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Import modules (now relative to the interactive_spammer_tool package)
from .ems_spammer.sms_sender import send_sms, get_custom_sms_details, spam_sms, get_spam_sms_details
from .ems_spammer.call_spammer import initiate_call, get_call_details, spam_call
from .email_spammer.email_sender_module import send_single_email, get_custom_email_details, spam_email
import config # Import config from the same directory

def display_banner():
    """Displays the ASCII art banner."""
    banner = r"""
 _  _  __________                          
| || ||___ /___  |__ _ __   __ _ _ __ ___  
| || |_ |_ \  / / __| '_ \ / _` | '_ ` _ \ 
|__   _|__) |/ /\__ \ |_) | (_| | | | | | |
   |_||____//_/ |___/ .__/ \__,_|_| |_| |_|
                    |_|                    
"""
    print(banner)

def display_main_menu():
    """Displays the main menu options."""
    print("\n" + "="*30)
    print("       MAIN MENU")
    print("="*30)
    print("1. EMS Spammer (SMS/Calls)")
    print("2. Email Spammer")
    print("0. Exit")
    print("="*30)

def display_ems_menu():
    """Displays the EMS Spammer submenu."""
    print("\n" + "-"*30)
    print("    EMS SPAMMER MENU")
    print("-"*30)
    print("1. Send Custom SMS")
    print("2. Spam SMS to a number")
    print("3. Initiate a Call (Placeholder)")
    print("4. Spam Calls to a number (Placeholder)")
    print("0. Back to Main Menu")
    print("-"*30)

def display_email_menu():
    """Displays the Email Spammer submenu."""
    print("\n" + "-"*30)
    print("    EMAIL SPAMMER MENU")
    print("-"*30)
    print("1. Send Custom Email")
    print("2. Spam Emails to a recipient")
    print("0. Back to Main Menu")
    print("-"*30)

def handle_ems_spammer():
    """Handles the EMS Spammer submenu logic."""
    while True:
        display_ems_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            phone_number, message = get_custom_sms_details()
            send_sms(phone_number, message) # This is a placeholder call
        elif choice == '2':
            phone_number, message, num_messages = get_spam_sms_details()
            spam_sms(phone_number, message, num_messages) # This is a placeholder call
        elif choice == '3':
            phone_number = get_call_details()
            initiate_call(phone_number) # Placeholder call
        elif choice == '4':
            phone_number = get_call_details()
            num_calls = int(input("How many calls to initiate? (e.g., 3): "))
            spam_call(phone_number, num_calls) # Placeholder call
        elif choice == '0':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1) # Pause briefly

def handle_email_spammer():
    """Handles the Email Spammer submenu logic."""
    while True:
        display_email_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            recipient_email, subject, body = get_custom_email_details()
            # Sending a single custom email
            # Note: In a real scenario, you'd likely want to confirm sender details
            # or have them pre-configured. Here we use config defaults.
            print("\nUsing default sender credentials from config.py...")
            if send_single_email(
                config.EMAIL_SENDER_EMAIL,
                config.EMAIL_SENDER_PASSWORD,
                config.EMAIL_SMTP_SERVER,
                config.EMAIL_SMTP_PORT,
                recipient_email,
                subject,
                body
            ):
                print("Custom email sent.")
            else:
                print("Failed to send custom email. Check config.py and error messages.")
        elif choice == '2':
            recipient_email, subject, body = get_custom_email_details()
            num_emails = int(input("How many emails to send to this recipient? (e.g., 10): "))
            spam_email(recipient_email, subject, body, num_emails)
        elif choice == '0':
            print("Returning to Main Menu...")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1) # Pause briefly

def main():
    """Main function to run the application."""
    while True:
        display_banner()
        display_main_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            handle_ems_spammer()
        elif choice == '2':
            handle_email_spammer()
        elif choice == '0':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        time.sleep(1) # Pause briefly

if __name__ == "__main__":
    # Ensure the package structure is valid when run directly
    # Create dummy __init__.py files if they don't exist
    dirs_to_check = [
        'interactive_spammer_tool',
        'interactive_spammer_tool/ems_spammer',
        'interactive_spammer_tool/email_spammer'
    ]
    for dir_name in dirs_to_check:
        init_file = os.path.join(os.path.dirname(__file__), dir_name, '__init__.py')
        if not os.path.exists(init_file):
            with open(init_file, 'w') as f:
                pass # Create empty file

    main()
