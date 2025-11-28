# 🔐 Password Manager (Python)

# 

A secure and beginner-friendly **Password Manager** built using Python.  
This application allows users to:

-   Create an account
    
-   Login securely
    
-   Save multiple website credentials
    
-   View saved passwords when logged in
    

Passwords are stored using hashing and encoding to provide basic security for learning purposes.

* * *

* * *

## 📁 Project Structure

# 

`password_manager/ │── password_manager.py     # Main program └── data.json               # Auto-generated encrypted storage file`

* * *

* * *

## 🛠 Tech Stack

# 

| Component | Technology |
| --- | --- |
| Language | Python |
| Data Storage | JSON |
| Security Features | SHA-256 hashing + Base64 encoding |

* * *

* * *

## 🚀 Features

# 

✔ User Registration  
✔ Secure Login System  
✔ Store Username/Email & Password for Websites  
✔ View Saved Credentials Anytime  
✔ Automatic JSON Storage  
✔ Beginner-friendly and extendable

* * *

* * *

## 📌 Setup Instructions

### 1️⃣ Clone the repository

# 

`git clone https://github.com/YOUR_USERNAME/password_manager.git cd password_manager`

* * *

### 2️⃣ Run the application

# 

`python password_manager.py`

* * *

### 3️⃣ Use the application

# 

| Action | What happens |
| --- | --- |
| Register | Creates a new hashed user account |
| Login | Unlocks access to features |
| Add Credential | Saves website login details |
| View Credentials | Displays all saved logins |
| Logout | Returns to main screen |

* * *

* * *

## 🔒 Security Notes

# 

-   Passwords are stored using a mix of **SHA-256 hashing** (for login passwords) and **Base64 encoding** (for stored site credentials).
    
-   Base64 is **not real encryption** — just obfuscation.
    
-   For real-world apps, use AES or an encrypted password vault model.
    

This project is intended for **learning purposes only**.

* * *

* * *

## ⭐ Future Improvements

# 

| Enhancement | Status |
| --- | --- |
| Password generator | ⏳ Planned |
| GUI using Tkinter | ⏳ Planned |
| Export to CSV | ⏳ Planned |
| Cloud secure sync | ❌ Advanced |

* * *

* * *

## 🧠 Concepts Learned

# 

-   File handling
    
-   JSON storage
    
-   Password hashing (`hashlib`)
    
-   Encoding & decoding (`base64`)
    
-   User authentication workflow
    
-   CRUD operations
