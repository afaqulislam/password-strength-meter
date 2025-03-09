import streamlit as st
import re
import random
import string
import math

# Common weak passwords blacklist
COMMON_PASSWORDS = {"password", "123456", "qwerty", "12345678", "abc123", "password1", "admin", "welcome"}

# Function to calculate password entropy
def calculate_entropy(password):
    """Calculate password entropy to determine its security level."""
    charset_size = 0

    if re.search(r"[a-z]", password): charset_size += 26
    if re.search(r"[A-Z]", password): charset_size += 26
    if re.search(r"\d", password): charset_size += 10
    if re.search(r"[!@#$%^&*]", password): charset_size += 8

    entropy = len(password) * math.log2(charset_size) if charset_size else 0
    return entropy

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if password in COMMON_PASSWORDS:
        return "❌ This is a commonly used password. Please choose a more secure one."

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    entropy = calculate_entropy(password)

    # Password strength rating based on entropy and criteria
    if entropy >= 60 and score == 4:
        return "🔥 Ultra Strong Password! 🏆"
    elif score == 4:
        return "✅ Strong Password! 🎉"
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features."
    else:
        return "❌ Weak Password! Improve it:\n" + "\n".join(feedback)

# Strong password generator with customization
def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Streamlit UI
st.set_page_config(page_title="🔐 Password Strength Meter", page_icon="🔑", layout="centered")
st.title("🔐 Advanced Password Strength Meter")

# Password input with visibility toggle
password = st.text_input("Enter your password", type="password")

if st.button("Check Password Strength"):
    if password:
        strength_message = check_password_strength(password)
        entropy = calculate_entropy(password)

        st.write(strength_message)

        # Strength Meter Bar
        if entropy >= 60:
            st.progress(1.0, text="🔥 Ultra Strong!")
        elif entropy >= 40:
            st.progress(0.8, text="✅ Strong!")
        elif entropy >= 30:
            st.progress(0.6, text="⚠️ Moderate")
        else:
            st.progress(0.3, text="❌ Weak")

        if "Weak Password" in strength_message or "commonly used password" in strength_message:
            st.warning(f"🔑 Suggested Strong Password: `{generate_strong_password()}`")

    else:
        st.warning("⚠️ Please enter a password!")

# Password Generator Section
st.subheader("🔑 Generate a Strong Password")
length = st.slider("Select Password Length:", min_value=8, max_value=24, value=12)
if st.button("Generate Password"):
    st.success(f"🔐 Your Strong Password: `{generate_strong_password(length)}`")

st.markdown("""
---
### 👨‍💻 Developed by **Afaq Ul Islam**  
🔐 Ensuring better security, one password at a time! 🚀  
  
🐍 GitHub: [Afaq Ul Islam](https://github.com/afaqulislam)  
💼 LinkedIn: [Afaq Ul Islam](https://www.linkedin.com/in/afaq-ul-islam-5090612b8)  

📜 **Copyright © 2025 Afaq Ul Islam** | All Rights Reserved.  
""")

