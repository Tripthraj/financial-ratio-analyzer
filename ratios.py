# -----------------------------
# LIQUIDITY RATIOS
# -----------------------------

def current_ratio(current_assets, current_liabilities):
    return current_assets / current_liabilities if current_liabilities != 0 else None


def quick_ratio(current_assets, inventory, prepaid_expenses, current_liabilities):
    return (current_assets - inventory - prepaid_expenses) / current_liabilities \
        if current_liabilities != 0 else None


def cash_ratio(cash_and_securities, current_liabilities):
    return cash_and_securities / current_liabilities if current_liabilities != 0 else None


# -----------------------------
# PROFITABILITY RATIOS
# -----------------------------

def gross_profit_margin(revenue, cogs):
    return ((revenue - cogs) / revenue) * 100 if revenue != 0 else None


def net_profit_margin(net_income, revenue):
    return (net_income / revenue) * 100 if revenue != 0 else None


def roe(net_income, avg_equity):
    return (net_income / avg_equity) * 100 if avg_equity != 0 else None


def roa(net_income, avg_assets):
    return (net_income / avg_assets) * 100 if avg_assets != 0 else None


# -----------------------------
# SOLVENCY RATIOS
# -----------------------------

def debt_to_equity(total_debt, total_equity):
    return total_debt / total_equity if total_equity != 0 else None


def interest_coverage(ebit, interest_expense):
    return ebit / interest_expense if interest_expense != 0 else None


def equity_ratio(total_equity, total_assets):
    return total_equity / total_assets if total_assets != 0 else None


# -----------------------------
# EFFICIENCY RATIOS
# -----------------------------

def inventory_turnover(cogs, avg_inventory):
    return cogs / avg_inventory if avg_inventory != 0 else None


def asset_turnover(net_sales, avg_assets):
    return net_sales / avg_assets if avg_assets != 0 else None


def days_sales_outstanding(avg_receivables, credit_sales, days=365):
    return (avg_receivables / credit_sales) * days if credit_sales != 0 else None


# -----------------------------
# VALUATION RATIOS
# -----------------------------

def eps(net_income, shares_outstanding):
    return net_income / shares_outstanding if shares_outstanding != 0 else None


def pe_ratio(market_price, net_income, shares_outstanding):
    e = eps(net_income, shares_outstanding)
    return market_price / e if e not in (None, 0) else None


def dividend_yield(dividend_per_share, market_price):
    return (dividend_per_share / market_price) * 100 if market_price != 0 else None


def price_to_book(market_price, book_value_per_share):
    return market_price / book_value_per_share if book_value_per_share != 0 else None
