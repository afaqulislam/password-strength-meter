# 🔐 Advanced Password Strength Meter

This is a **password strength checker and generator** built using **Streamlit**. It evaluates the security of passwords using entropy calculations and provides instant feedback on improvements. Additionally, it includes a **strong password generator** to help users create secure passwords.

---

## 🚀 Features
- ✅ **Password Strength Analysis** (Checks length, complexity, and entropy)
- 🔥 **Strength Meter Bar** for easy visualization
- 🔑 **Suggests Strong Passwords** if entered password is weak
- 🎛 **Customizable Password Generator** (Length between 8-24 characters)
- 📊 **Entropy Calculation** for security assessment
- 🛠 **User-Friendly Interface** using Streamlit

---

## 📜 How It Works

### 🔍 Password Strength Checker
1. Enter a password in the input field.
2. Click the **"Check Password Strength"** button.
3. The app analyzes the password based on:
   - Length (Minimum 8 characters required)
   - Uppercase & lowercase letters
   - Numbers (0-9)
   - Special characters (!@#$%^&*)
4. It assigns a **strength rating**:
   - ❌ Weak
   - ⚠️ Moderate
   - ✅ Strong
   - 🔥 Ultra Strong
5. If the password is weak, suggestions for improvement are provided.

### 🔑 Strong Password Generator
1. Select a password length using the **slider** (8-24 characters).
2. Click **"Generate Password"**.
3. A secure password will be displayed.

---

## 🛠 Installation & Setup

### 1️⃣ Install Dependencies
Ensure you have Python installed. Then, install **Streamlit**:
```sh
pip install streamlit
```

### 2️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/password-strength-meter.git
cd password-strength-meter
```

### 3️⃣ Run the App
```sh
streamlit run app.py
```

The app will launch in your default web browser.

---

## 📌 Technologies Used
- **Python** (Core Logic)
- **Streamlit** (UI Framework)
- **Regular Expressions (re)** (Pattern Matching)
- **Math & Random Modules** (Entropy Calculation & Password Generation)

---

## 🎯 Example Output
### Weak Password:
```
❌ Weak Password! Improve it:
❌ Password should be at least 8 characters long.
❌ Include both uppercase and lowercase letters.
❌ Add at least one number (0-9).
❌ Include at least one special character (!@#$%^&*).
```

### Strong Password:
```
✅ Strong Password! 🎉
```

### Ultra Strong Password:
```
🔥 Ultra Strong Password! 🏆
```

---

## 📜 License
📄 This project is licensed under the **MIT License**.

---

## 👨‍💻 Developed By
**Afaq Ul Islam** 🚀

🔗 GitHub: [Afaq Ul Islam](https://github.com/afaqulislam)
🔗 LinkedIn: [Afaq Ul Islam](https://www.linkedin.com/in/afaq-ul-islam-5090612b8)

---

💡 *Contributions are welcome! Feel free to fork this repository and submit a pull request.*

