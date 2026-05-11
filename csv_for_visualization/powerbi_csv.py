import pandas as pd


# Monthly revenue
orders = pd.read_csv("ORDER.csv")
orders["ORDER_DATES"] = pd.to_datetime(orders["ORDER_DATES"], dayfirst=True)
completed = orders[orders["ORDER_STATUS"] == "completed"].copy()
completed["YearMonth"] = completed["ORDER_DATES"].dt.to_period("M").astype(str)

monthly = completed.groupby("YearMonth").agg(
    total_revenue=("TOTAL_AMOUNT", "sum"),
    order_count=("ORDER_ID", "count"),
    avg_order_value=("TOTAL_AMOUNT", "mean")
).reset_index()
monthly.to_csv("monthly_revenue.csv", index=False)

# Top products
oi   = pd.read_csv("ORDER_ITEM.csv")
prod = pd.read_csv("PRODUCT.csv")
oi_prod = oi.merge(prod[["PRODUCT_ID","PRODUCT_NAME","CATEGORY","BRAND"]], on="PRODUCT_ID")

top_products = oi_prod.groupby(
    ["PRODUCT_ID","PRODUCT_NAME","CATEGORY","BRAND"]
).agg(
    total_revenue=("ITEM_TOTAL", "sum"),
    units_sold=("QUANTITY", "sum"),
    order_count=("ORDER_ID", "count")
).reset_index().sort_values("total_revenue", ascending=False)

top_products.to_csv("top_products.csv", index=False)