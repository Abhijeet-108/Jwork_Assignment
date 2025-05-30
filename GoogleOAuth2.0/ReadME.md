# Google OAuth 2.0 Integration

## Overview
This project demonstrates the integration of Google OAuth 2.0 for secure authentication in a Django application. It allows users to log in using their Google accounts, ensuring a seamless and secure experience.

## Features
- Google account authentication.
- Secure token handling.
- Easy integration with Django applications.

## Prerequisites
- A Google Cloud account.
- A registered OAuth 2.0 client ID and client secret.
- Python and Django installed on your system.

## Setup Instructions
1. Clone the repository:
    ```bash
    git clone https://github.com/Abhijeet-108/Jwork_Assignment.git
    cd GoogleOAuth2.0
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Configure environment variables:
    Create a `.env` file in the root directory and add the following:
    ```env
    CLIENT_ID=your-google-client-id
    CLIENT_SECRET=your-google-client-secret
    REDIRECT_URI=http://localhost:8000/auth/callback
    ```

4. Apply migrations:
    ```bash
    python manage.py migrate
    ```

5. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

6. Visit `http://localhost:8000` in your browser to test the integration.

## Usage
- Navigate to the login page.
- Click the "Sign in with Google" button.
- Authenticate using your Google account.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or improvements.
