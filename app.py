import streamlit as st

st.markdown("""
<style>
/* Page background */
.stApp {
    background-color: #EAFBF2;
    font-family: "Inter", "Segoe UI", sans-serif;
}

/* Center container */
.block-container {
    max-width: 700px;
    padding-top: 3rem;
}

/* Card style */
.card {
    background: #FFFFFF;
    padding: 2rem;
    border-radius: 14px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.08);
    margin-bottom: 1.5rem;
}

/* Title */
.card h1 {
    font-size: 2rem;
    margin-bottom: 0.25rem;
}

/* Formula text */
.formula {
    color: #555;
    font-size: 0.95rem;
    margin-bottom: 1.5rem;
}

/* Inputs */
div[data-baseweb="input"] input {
    border-radius: 10px;
    padding: 0.6rem;
}

/* Buttons */
.stButton > button {
    border-radius: 10px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    background-color: #2ECC71;
    color: white;
    border: none;
}

.stButton > button:hover {
    background-color: #27AE60;
}

/* Back button tweak */
.back-btn button {
    background-color: #ECF0F1 !important;
    color: #333 !important;
}
</style>
""", unsafe_allow_html=True)


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

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.title("📈 Return on Equity (ROE)")
    st.markdown('<div class="formula">ROE = Net Profit / Equity</div>', unsafe_allow_html=True)

    net_profit = st.number_input("Net Profit (₹ Cr)", min_value=0.0, step=1.0)
    equity = st.number_input("Equity (₹ Cr)", min_value=0.0, step=1.0)

    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("Submit"):
            if equity == 0:
                st.error("Equity cannot be zero")
            else:
                roe = (net_profit / equity) * 100
                st.success(f"ROE = {roe:.2f}%")

    with col2:
        st.markdown('<div class="back-btn">', unsafe_allow_html=True)
        if st.button("← Back"):
            st.session_state.page = "home"
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)



# ---------------- ROA PAGE ----------------
elif st.session_state.page == "roa":
    st.title("🏦 Return on Assets (ROA)")
    st.write("ROA = Net Profit / Total Assets")

    if st.button("⬅ Back"):
        st.session_state.page = "home"
