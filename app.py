import streamlit as st
import ratios

# -------------------------------------------------
# Helpers
# -------------------------------------------------
def cr_to_num(x):
    return x * 10_000_000


# -------------------------------------------------
# Page config
# -------------------------------------------------
st.set_page_config(
    page_title="Financial Ratio Analyzer",
    layout="centered"
)

# -------------------------------------------------
# Page state
# -------------------------------------------------
if "page" not in st.session_state:
    st.session_state.page = "home"


# -------------------------------------------------
# HOME PAGE
# -------------------------------------------------
if st.session_state.page == "home":

    st.title("📊 Financial Ratio Analyzer")
    st.write("Select a ratio category")

    if st.button("💧 Liquidity Ratios"):
        st.session_state.page = "liquidity"
        st.rerun()

    if st.button("📈 Profitability Ratios"):
        st.session_state.page = "profitability"
        st.rerun()

    if st.button("⚖️ Solvency Ratios"):
        st.session_state.page = "solvency"
        st.rerun()

    if st.button("🔄 Efficiency Ratios"):
        st.session_state.page = "efficiency"
        st.rerun()

    if st.button("💹 Valuation Ratios"):
        st.session_state.page = "valuation"
        st.rerun()


# =================================================
# LIQUIDITY RATIOS
# =================================================
elif st.session_state.page == "liquidity":

    st.title("💧 Liquidity Ratios")

    ca = st.number_input("Current Assets (₹ Cr)", min_value=0.0)
    cl = st.number_input("Current Liabilities (₹ Cr)", min_value=0.0)
    inventory = st.number_input("Inventory (₹ Cr)", min_value=0.0)
    prepaid = st.number_input("Prepaid Expenses (₹ Cr)", min_value=0.0)
    cash = st.number_input("Cash & Marketable Securities (₹ Cr)", min_value=0.0)

    if st.button("Calculate Liquidity Ratios"):
        st.success(f"Current Ratio = {ratios.current_ratio(cr_to_num(ca), cr_to_num(cl)):.2f}")
        st.success(
            f"Quick Ratio = {ratios.quick_ratio(cr_to_num(ca), cr_to_num(inventory), cr_to_num(prepaid), cr_to_num(cl)):.2f}"
        )
        st.success(
            f"Cash Ratio = {ratios.cash_ratio(cr_to_num(cash), cr_to_num(cl)):.2f}"
        )

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()


# =================================================
# PROFITABILITY RATIOS
# =================================================
elif st.session_state.page == "profitability":

    st.title("📈 Profitability Ratios")

    revenue = st.number_input("Revenue (₹ Cr)", min_value=0.0)
    cogs = st.number_input("Cost of Goods Sold (₹ Cr)", min_value=0.0)
    net_income = st.number_input("Net Income (₹ Cr)", min_value=0.0)
    avg_equity = st.number_input("Average Shareholder Equity (₹ Cr)", min_value=0.0)
    avg_assets = st.number_input("Average Total Assets (₹ Cr)", min_value=0.0)

    if st.button("Calculate Profitability Ratios"):
        st.success(
            f"Gross Profit Margin = {ratios.gross_profit_margin(cr_to_num(revenue), cr_to_num(cogs)):.2f}%"
        )
        st.success(
            f"Net Profit Margin = {ratios.net_profit_margin(cr_to_num(net_income), cr_to_num(revenue)):.2f}%"
        )
        st.success(
            f"ROE = {ratios.roe(cr_to_num(net_income), cr_to_num(avg_equity)):.2f}%"
        )
        st.success(
            f"ROA = {ratios.roa(cr_to_num(net_income), cr_to_num(avg_assets)):.2f}%"
        )

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()


# =================================================
# SOLVENCY RATIOS
# =================================================
elif st.session_state.page == "solvency":

    st.title("⚖️ Solvency Ratios")

    debt = st.number_input("Total Debt (₹ Cr)", min_value=0.0)
    equity = st.number_input("Total Shareholder Equity (₹ Cr)", min_value=0.0)
    ebit = st.number_input("EBIT (₹ Cr)", min_value=0.0)
    interest = st.number_input("Interest Expense (₹ Cr)", min_value=0.0)
    total_assets = st.number_input("Total Assets (₹ Cr)", min_value=0.0)

    if st.button("Calculate Solvency Ratios"):
        st.success(
            f"Debt–Equity Ratio = {ratios.debt_to_equity(cr_to_num(debt), cr_to_num(equity)):.2f}"
        )
        st.success(
            f"Interest Coverage Ratio = {ratios.interest_coverage(cr_to_num(ebit), cr_to_num(interest)):.2f}"
        )
        st.success(
            f"Equity Ratio = {ratios.equity_ratio(cr_to_num(equity), cr_to_num(total_assets)):.2f}"
        )

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()


# =================================================
# EFFICIENCY RATIOS
# =================================================
elif st.session_state.page == "efficiency":

    st.title("🔄 Efficiency Ratios")

    cogs = st.number_input("COGS (₹ Cr)", min_value=0.0)
    avg_inventory = st.number_input("Average Inventory (₹ Cr)", min_value=0.0)
    sales = st.number_input("Net Sales (₹ Cr)", min_value=0.0)
    avg_assets = st.number_input("Average Total Assets (₹ Cr)", min_value=0.0)
    avg_receivables = st.number_input("Average Accounts Receivable (₹ Cr)", min_value=0.0)

    if st.button("Calculate Efficiency Ratios"):
        st.success(
            f"Inventory Turnover = {ratios.inventory_turnover(cr_to_num(cogs), cr_to_num(avg_inventory)):.2f}"
        )
        st.success(
            f"Asset Turnover = {ratios.asset_turnover(cr_to_num(sales), cr_to_num(avg_assets)):.2f}"
        )
        st.success(
            f"Days Sales Outstanding = {ratios.days_sales_outstanding(cr_to_num(avg_receivables), cr_to_num(sales)):.2f} days"
        )

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()


# =================================================
# VALUATION RATIOS
# =================================================
elif st.session_state.page == "valuation":

    st.title("💹 Valuation Ratios")

    net_income = st.number_input("Net Income (₹ Cr)", min_value=0.0)
    shares = st.number_input("Shares Outstanding (Cr)", min_value=0.0)
    price = st.number_input("Market Price per Share (₹)", min_value=0.0)
    dividend = st.number_input("Dividend per Share (₹)", min_value=0.0)
    book_value = st.number_input("Book Value per Share (₹)", min_value=0.0)

    if st.button("Calculate Valuation Ratios"):
        eps_val = ratios.eps(cr_to_num(net_income), cr_to_num(shares))
        pe_val = ratios.pe_ratio(price, cr_to_num(net_income), cr_to_num(shares))

        st.success(f"EPS = ₹ {eps_val:.2f}")
        st.success(f"P/E Ratio = {pe_val:.2f}")
        st.success(
            f"Dividend Yield = {ratios.dividend_yield(dividend, price):.2f}%"
        )
        st.success(
            f"P/B Ratio = {ratios.price_to_book(price, book_value):.2f}"
        )

    if st.button("⬅ Back"):
        st.session_state.page = "home"
        st.rerun()
