# 📦 Data Entry & Retrieval API

This project is a simple **Data Entry and Retrieval API** built with **Django** and **Django Rest Framework (DRF)**. It features:

✅ User Authentication via Token  
✅ Add Data (POST)  
✅ Retrieve Data (GET)  
✅ Secure endpoints ensuring each user only accesses their own data.

---

## 🛠️ Features

- **Add Data**  
  - `POST /api/add/`  
  - Requires authentication  
  - Allows users to submit data with `title` and `description`

- **Retrieve Data**  
  - `GET /api/entries/`  
  - Requires authentication  
  - Supports filtering by `title`

- **Authentication**  
  - `POST /api-token-auth/`  
  - Returns a token for authenticated requests

---

## 🗂️ Tech Stack

- Python 3.x
- Django 4.x
- Django Rest Framework
- Token Authentication

---

## 📌 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abhijeet-108/Jwork_Assignment.git
   cd data-entry-api

2. **Create a virtual environment**
    ```bash
   python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate


3. **Install dependencies**
    ```bash
   pip install -r requirements.txt

4. **Apply migrations**
    ```bash
   python manage.py migrate

5. **Create a superuser (optional, for admin access)**
    ```bash
   python manage.py createsuperuser

6. **Run the development server bash Copy code**
    ```bash
    python manage.py runserver

# 🔑 Authentication Flow  

## 1. Obtain a Token  
Send a POST request to `/api-token-auth/` with your username and password:  

```http  
POST /api-token-auth/  
Content-Type: application/json  

{  
    "username": "your_username",  
    "password": "your_password"  
}  
```  

### Response:  

```json  
{  
    "token": "your_token_here"  
}  
```  

## 2. Use the Token  
Include the token in your requests using the Authorization header:  

```makefile  
Authorization: Token your_token_here  
```  

# 📚 API Endpoints  

## ➕ Add Entry  
**POST** `/api/add/`  

### Headers:  
```makefile  
Authorization: Token your_token_here  
```  

### Body (JSON):  
```json  
{  
    "title": "Sample Title",  
    "description": "Sample Description"  
}  
```  

### Response:  
Returns the newly created entry object.  

## 📄 Retrieve Entries  
**GET** `/api/entries/`  

### Headers:  
```makefile  
Authorization: Token your_token_here  
```  

### Query Parameters (optional):  
- `title`: filter by title (partial match)  

### Response:  
```json  
[  
    {  
        "id": 1,  
        "title": "Sample Title",  
        "description": "Sample Description",  
        "user": 1  
    }  
]  
```  

# 🗂️ Models  

### Entry  
- `title`: string  
- `description`: text  
- `user`: ForeignKey to User  

# 🔧 Settings  

Ensure `settings.py` includes:  

```python  
INSTALLED_APPS = [  
        ...  
        'rest_framework',  
        'rest_framework.authtoken',  
        ...  
]  

REST_FRAMEWORK = {  
        'DEFAULT_AUTHENTICATION_CLASSES': [  
                'rest_framework.authentication.TokenAuthentication',  
        ],  
        'DEFAULT_PERMISSION_CLASSES': [  
                'rest_framework.permissions.IsAuthenticated',  
        ],  
}  
```  

# 📂 Project Structure  

```plaintext  
dataEntry/  
│  
├── dataEntry/  
│   ├── settings.py  
│   └── urls.py  
│  
├── api/  
│   ├── models.py  
│   ├── serializers.py  
│   ├── views.py  
│   └── urls.py  
│  
├── manage.py  
└── requirements.txt  
```  

# 🧩 Usage Notes  

- All requests to `/api/add/` and `/api/entries/` must include the Authorization header with the token.  
- Users can only see their own entries.  
- Ensure the token you use is valid and linked to your user.  

# 🤝 Contributing  

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.  


