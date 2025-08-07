# 🔐 OTP-Based User Authentication System (Email Verification) — Python + MySQL

A **complete command-line authentication system** featuring secure password hashing, email-based OTP verification, SQL injection protection, and modern Python standards. Perfect for internal tools, admin portals, or learning about secure authentication systems.

![OTP CLI Auth System](project-screenshot.png)

---

## 🚀 What is This?

This is a **Python-powered authentication system** that leverages:

✅ **One-Time Passwords (OTP)** via email for verifying users
✅ **Secure login/registration** with bcrypt hashing
✅ **SQL Injection detection & prevention**
✅ **OTP expiration logic** (auto-cleans expired codes)
✅ **User data storage in MySQL**
✅ **Command-line Interface** for interaction

Built to be **secure**, **extendable**, and **practical**, this app simulates real-world login mechanics in a local CLI environment.

---

## 💡 Why Use This?

Whether you're:

* A student learning about **authentication & security**
* A backend dev testing **email-verification workflows**
* An engineer building a **prototype login system**
* Or just someone who wants to **learn real security concepts in Python**

...this project covers the **core foundation** of secure authentication systems with simplicity and real-world logic.

---

## 📸 Screenshot

> *Below: OTP verification screen in CLI*

![OTP CLI Screenshot](project-screenshot.png)

---

## 🧰 Features at a Glance

| Feature                       | Description                                                             |
| ----------------------------- | ----------------------------------------------------------------------- |
| ✅ Email OTP Verification      | Sends time-limited OTP via Gmail SMTP                                   |
| ✅ OTP Expiration (5 mins)     | Auto-expires and deletes stale OTPs from database                       |
| ✅ Password Hashing            | Uses `bcrypt` for industry-standard hashing                             |
| ✅ SQL Injection Protection    | Detects and blocks known SQL injection patterns during login            |
| ✅ Strong Password Enforcement | Enforces rules (uppercase, digit, special chars, etc.)                  |
| ✅ User & Login Separation     | Stores user details and login credentials in separate normalized tables |
| ✅ Full CLI Interface          | Clean terminal interface for registering and logging in                 |

---

## 🛠 Tech Stack

* **Python 3**
* **MySQL**
* **SMTP (Gmail App Password)**

### 📦 Key Python Libraries

* `bcrypt` – Password hashing
* `pyotp` – OTP generation
* `mysql-connector-python` – MySQL connection
* `smtplib` – Sending emails
* `hashlib`, `re`, `datetime`, `getpass`, `time` – Core utilities

---

## 📁 Project Structure

```bash
OTP_System/
│
├── menu.py                # Main menu (signup / login)
├── Login.py               # Registration & login logic
├── otp_authenticate.py    # OTP generation, email sending, expiration logic
├── configure.py           # Email config (company email, app password)
├── database.py            # MySQL DB connection
├── requirements.txt       # Dependencies list
├── README.md              # Project documentation
└── assets/
    └── project-screenshot.png  # CLI screenshot image
```

---

## 🔧 Installation & Usage

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/otp-auth-system.git
cd otp-auth-system
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Gmail App Password

Update `configure.py` with your email and [Gmail App Password](https://support.google.com/accounts/answer/185833):

```python
company_email = "yourcompany@gmail.com"
company_email_password = "your_app_password"
```

✅ Make sure 2FA is enabled on your Gmail account. Generate a [Gmail App Password](https://myaccount.google.com/apppasswords) to use here.

---

### 4️⃣ Run the App

```bash
python menu.py
```

---

## 🧪 MySQL Setup

Before running, make sure your MySQL database has the following tables:

### `USERS` Table

```sql
CREATE TABLE USERS (
  user_id INT PRIMARY KEY AUTO_INCREMENT,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  username VARCHAR(100) UNIQUE,
  email VARCHAR(100)
);
```

### `LOGIN` Table

```sql
CREATE TABLE LOGIN (
  login_id INT PRIMARY KEY AUTO_INCREMENT,
  username VARCHAR(100),
  password VARCHAR(255)
);
```

### `OTP` Table

```sql
CREATE TABLE OTP (
  otp_id INT PRIMARY KEY AUTO_INCREMENT,
  otp_code VARCHAR(255),
  email VARCHAR(100),
  exp_time TIMESTAMP
);
```

---

## ✅ Security Considerations

* 🔒 Passwords are hashed with `bcrypt` before storing
* 🧪 OTPs are one-time-use and expire in 5 minutes
* ⚠️ SQL injection detection via regex pattern checks
* 🚫 Email + password fields are validated & sanitized

---

## 📦 Dependencies

```
bcrypt==4.1.2
pyotp
mysql-connector-python
stdiomask
```

> Standard libraries used: `hashlib`, `smtplib`, `email`, `re`, `datetime`, `getpass`, `time`

---

## 🙋 FAQ

**Q: Can I use another SMTP provider?**
A: Yes! Simply update the SMTP section in `otp_authenticate.py`. Any provider that supports SMTP can work.

**Q: Can this run on Mac/Linux?**
A: Yes. This is cross-platform — as long as Python and MySQL are installed.

**Q: Can I customize OTP length/expiration?**
A: Absolutely. Modify the `generate_and_send_otp` function in `otp_authenticate.py`.

---

## 👤 Author

* **GitHub:** [@SecureAuditX](https://github.com/SecureAuditX)
* **Email:** [abdulkarimumar86@gmail.com](mailto:yourcompany@gmail.com)
* **Twitter:** [@SecureAuditX](https://twitter.com/SecureAuditX)

---

## 🤝 Contribute

Found a bug? Want a new feature? Fork this repo and open a PR or raise an issue!

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify it.
