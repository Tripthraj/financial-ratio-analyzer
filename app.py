import streamlit as st

# ---------------- PAGE MEMORY ----------------
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    st.title("📊 Financial Ratio Analyzer")
    st.subheader("Select a Ratio")

    if st.button("📈 Return on Equity (ROE)"):
        st.session_state.page = "roe"

    if st.button("🏦 Return on Assets (ROA)"):
        st.session_state.page = "roa"

# ---------------- ROE PAGE ----------------
elif st.session_state.page == "roe":
    st.title("📈 Return on Equity (ROE)")
    st.write("ROE = Net Profit / Equity")

    net_profit = st.number_input("Net Profit (₹ Cr)", min_value=0.0)
    equity = st.number_input("Equity (₹ Cr)", min_value=0.0)

    if st.button("Submit"):
        if equity == 0:
            st.error("Equity cannot be zero")
        else:
            roe = (net_profit / equity) * 100
            st.success(f"ROE = {round(roe, 2)} %")

    if st.button("⬅ Back"):
        st.session_state.page = "home"


# ---------------- ROA PAGE ----------------
elif st.session_state.page == "roa":
    st.title("🏦 Return on Assets (ROA)")
    st.write("ROA = Net Profit / Total Assets")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
