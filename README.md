
## Getting Started

### Prerequisites

*   **Python 3:** Ensure you have Python 3 installed on your Linux Chromebook.
*   **Pip:** Python's package installer.

### Installation

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/your_username/437spam.git
    cd 437spam
    ```
    *(Replace `your_username` with your actual GitHub username)*

2.  **Install Dependencies:**
    This project primarily uses standard Python libraries. If you integrate with third-party services (like Twilio for SMS/Calls), you'll need to install their SDKs.
    ```bash
    # Example for Twilio:
    # pip install twilio
    ```
    *(Use `pip3` if `pip` is linked to Python 2)*

3.  **Configure Settings:**
    *   Open the `interactive_spammer_tool/config.py` file in a text editor.
    *   **For Email Spammer:** Update `EMAIL_SMTP_SERVER`, `EMAIL_SMTP_PORT`, `EMAIL_SENDER_EMAIL`, and `EMAIL_SENDER_PASSWORD`.
        *   **Security Note:** For services like Gmail, you might need to enable "Less secure app access" or generate an "App Password" if 2-Factor Authentication is enabled. **Use a disposable email account for testing.**
    *   **For EMS Spammer (SMS/Calls):** If you plan to implement actual SMS/Call functionality, you'll need to sign up for a service (e.g., Twilio), obtain API credentials (`TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`), and your service's phone number. Update these in `config.py`.

### Running the Application

1.  Navigate to the root directory of the cloned repository (`437spam/`).
2.  Run the main script:
    ```bash
    python interactive_spammer_tool/main_menu.py
    ```
    *(Again, you might need to use `python3`)*

3.  Follow the on-screen prompts to navigate the menus and choose your desired actions.

## Usage

### Main Menu:

*   `1`: Access the EMS Spammer (SMS/Calls) options.
*   `2`: Access the Email Spammer options.
*   `0`: Exit the application.

### EMS Spammer Menu:

*   `1`: Send a custom SMS message to a specified phone number.
*   `2`: Send multiple SMS messages to a phone number for spamming.
*   `3`: Initiate a single voice call (requires service integration).
*   `4`: Initiate multiple voice calls (spamming calls, requires service integration).
*   `0`: Return to the main menu.

### Email Spammer Menu:

*   `1`: Send a single custom email to a recipient.
*   `2`: Send multiple identical emails to a recipient for spamming.
*   `0`: Return to the main menu.

## Important Notes & Warnings

*   **Educational Use Only:** This tool is designed strictly for educational purposes to understand programming concepts and API interactions.
*   **Legal Compliance:** Unauthorized sending of emails or SMS messages, or making unsolicited calls, is illegal in most jurisdictions. Ensure you have explicit consent from recipients before using any messaging features. Familiarize yourself with laws like CAN-SPAM (USA), GDPR (Europe), and others relevant to your location.
*   **Service Costs:** Utilizing third-party services like Twilio for SMS and calls incurs costs. Be mindful of their pricing structures.
*   **Security:** Never commit sensitive credentials (like email passwords or API keys) directly into your code. Use environment variables or a secure configuration management system for production environments. The `config.py` provided is for simple demonstration and testing.
*   **Ethical Considerations:** Responsible use of technology is paramount. Do not use this tool to harass, deceive, or harm others.

## Contributing

This project is for educational exploration. Contributions are not actively sought at this time, but feedback is welcome.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details. *(You would need to create a `LICENSE.md` file with the MIT License text if you want to formally license it.)*
