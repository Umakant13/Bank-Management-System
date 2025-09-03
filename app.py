import streamlit as st
from bank import Bank

st.set_page_config(page_title="Bank Management System", layout="centered")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox("Menu", [
    "Create Account", "Deposit Money", "Withdraw Money",
    "Show Details", "Update Details", "Delete Account"
])

if menu == "Create Account":
    st.subheader("Create New Account")
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    email = st.text_input("Email")
    pin = st.text_input("4-digit PIN", type="password")

    if st.button("Create"):
        if not pin.isdigit() or len(pin) != 4:
            st.error("PIN must be 4 digits")
        else:
            result = Bank.createAccount(name, age, email, int(pin))
            st.success(result.get("success")) if "success" in result else st.error(result.get("error"))

elif menu == "Deposit Money":
    st.subheader("Deposit Money")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Deposit"):
        result = Bank.depositMoney(acc, int(pin), amt)
        st.write(result)

elif menu == "Withdraw Money":
    st.subheader("Withdraw Money")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    amt = st.number_input("Amount", min_value=1)

    if st.button("Withdraw"):
        result = Bank.withdrawMoney(acc, int(pin), amt)
        st.write(result)

elif menu == "Show Details":
    st.subheader("Account Details")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        result = Bank.showDetails(acc, int(pin))
        st.write(result)

elif menu == "Update Details":
    st.subheader("Update Details")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")
    name = st.text_input("New Name (optional)")
    email = st.text_input("New Email (optional)")
    newPin = st.text_input("New 4-digit PIN (optional)", type="password")

    if st.button("Update"):
        newPin_val = int(newPin) if newPin.isdigit() else None
        result = Bank.updateDetails(acc, int(pin), name, email, newPin_val)
        st.write(result)

elif menu == "Delete Account":
    st.subheader("Delete Account")
    acc = st.text_input("Account No")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        result = Bank.deleteAccount(acc, int(pin))
        st.write(result)
