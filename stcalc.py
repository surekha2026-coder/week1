import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")

st.title("🧮 Calculator App")
st.write("A simple calculator styled using Streamlit columns")

st.divider()

# Layout using columns
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)

st.divider()

# Operation selection
operation = st.radio(
    "Choose Operation",
    ["Addition", "Subtraction", "Multiplication", "Division"],
    horizontal=True
)

st.divider()

# Calculate button centered
center_col1, center_col2, center_col3 = st.columns([1, 2, 1])

with center_col2:
    calculate = st.button("Calculate", use_container_width=True)

# Calculation logic
if calculate:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("❌ Cannot divide by zero")
            result = None
        else:
            result = num1 / num2

    if result is not None:
        st.success(f"✅ Result: {result}")
