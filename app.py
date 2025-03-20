import streamlit as st
import re
import random

def set_background():
    page_bg = f"""
    <style>
    html, body, .stApp {{
        background-color: #87CEFA !important;
        color: black;
    }}
    .stTextInput input {{
        background-color: #ffffff;
        color: black;
        border-radius: 5px;
        padding: 10px;
        border: 1px solid #ccc;
    }}
    .stButton button {{
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px;
    }}
    </style>
    """
    st.markdown(page_bg, unsafe_allow_html=True)


def generate_strong_password():
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    return "".join(random.choice(characters) for _ in range(12))

def check_password_strength(password):
    strength = 0
    feedback = []
    common_passwords = ["password", "123456", "password123", "qwerty", "letmein"]
    
    if password.lower() in common_passwords:
        return 0, ["Avoid using common passwords!"]
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Include at least one uppercase letter.")
    
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Include at least one lowercase letter.")
    
    if re.search(r"\d", password):
        strength += 1
    else:
        feedback.append("Include at least one number.")
    
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character.")
    
    return strength, feedback

# Set background and styles
set_background()

# Streamlit UI
st.title("🔒 Password Strength Meter")
st.markdown("### Secure your accounts with a strong password!")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    st.subheader("Password Strength")
    
    if strength == 5:
        st.success("Strong Password! ✅")
    elif strength >= 3:
        st.warning("Moderate Password ⚠️")
    else:
        st.error("Weak Password ❌")
    
    st.progress(strength / 5)
    
    if feedback:
        st.subheader("🔹 Suggestions to Improve:")
        for tip in feedback:
            st.write(f"- {tip}")

if st.button("Generate Strong Password"):
    strong_password = generate_strong_password()
    st.success(f"💡 Suggested Strong Password: `{strong_password}`")
