# 🏧 Python ATM Machine Project

A simple **ATM Machine simulation written in Python**.
This program allows users to create accounts, deposit money, withdraw money, and check account balances. All account data is stored in a **JSON file**, so the data remains saved even after closing the program.

---

## 📌 Features

* Create a new bank account
* Generate a **12-digit random account number**
* Create a secure **4-digit PIN**
* Deposit money
* Withdraw money
* Balance enquiry
* Persistent data storage using **JSON**
* Simple command-line interface

---

## 🛠 Technologies Used

* **Python**
* **JSON (for data storage)**
* **Random module**

---

## 📂 Project Structure

```
ATM-MACHINE-PROJECT
│
├── atm.py
├── Data
│   └── accounts.json.txt
└── README.md
```

---

## ⚙️ How It Works

1. When the program starts, it loads existing accounts from the JSON file.
2. If the file does not exist, it creates an empty account database.
3. Users can select options from the ATM menu:

   * Create account
   * Withdraw cash
   * Deposit cash
   * Check balance
4. Every transaction updates the JSON file automatically.

---

## ▶️ How to Run the Project

### 1️⃣ Install Python

Make sure Python is installed on your system.

Check with:

```bash
python --version
```

### 2️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
```

### 3️⃣ Go to Project Folder

```bash
cd YOUR-REPOSITORY
```

### 4️⃣ Run the Program

```bash
python atm.py
```

---

## 🧾 Example Menu

```
------ ATM MENU ------
1. Create Account
2. Withdraw Cash
3. Deposit Cash
4. Balance Enquiry
5. Exit
```

---

## 🔐 Security Features

* Each account has a **unique 12-digit account number**
* Users must enter a **4-digit PIN**
* PIN verification is required for:

  * Withdrawals
  * Deposits
  * Balance checks

---

## 💾 Data Storage

Account data is stored in:

```
accounts.json.txt
```

Example stored data:

```json
{
    "123456789012": {
        "name": "Abdullah",
        "age": 21,
        "pin": 1234,
        "balance": 5000
    }
}
```

---

## 🚀 Future Improvements

* Add **PIN encryption**
* Add **transaction history**
* Add **account deletion**
* Add **GUI interface (Tkinter / Web App)**
* Add **login system**

---

## 👨‍💻 Author

**Abdullah**

Python learner interested in **AI, Machine Learning, and Software Development**.

