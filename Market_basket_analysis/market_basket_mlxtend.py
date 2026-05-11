import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
from mlxtend.preprocessing import TransactionEncoder

order_items = pd.read_csv("ORDER_ITEM.csv")
products    = pd.read_csv("PRODUCT.csv")
orders      = pd.read_csv("ORDER.csv")

# Filter to completed orders only

print(orders["ORDER_STATUS"].value_counts().to_string())

completed_order_ids = orders[orders["ORDER_STATUS"] == "completed"]["ORDER_ID"]
oi_completed = order_items[order_items["ORDER_ID"].isin(completed_order_ids)].copy()

print(f"\n  Completed orders     : {oi_completed['ORDER_ID'].nunique():,}")
print(f"  Items in those orders: {len(oi_completed):,}")


# Attach category names to each item

oi_completed = oi_completed.merge(
    products[["PRODUCT_ID", "PRODUCT_NAME", "CATEGORY"]],
    on="PRODUCT_ID",
    how="left"
)

# Each transaction = list of unique categories bought in one order

# Group by ORDER_ID → list of unique categories per order
transactions = (
    oi_completed
    .groupby("ORDER_ID")["CATEGORY"]
    .apply(lambda cats: list(set(cats)))
    .tolist()
)

from collections import Counter
size_dist = Counter(len(t) for t in transactions)
print(f"\n  Total transactions : {len(transactions):,}")
print(f"  Transaction size distribution:")
for size in sorted(size_dist.keys()):
    pct = size_dist[size] / len(transactions) * 100
    print(f"    {size} category: {size_dist[size]:,} orders ({pct:.1f}%)")


# Encode transactions using mlxtend
# TransactionEncoder converts list-of-lists into a binary True/False DataFrame

te = TransactionEncoder()
te_array = te.fit(transactions).transform(transactions)
basket_df = pd.DataFrame(te_array, columns=te.columns_)

print(f"\n  Encoded basket matrix shape: {basket_df.shape}")
print(f"  Columns: {list(basket_df.columns)}")
print(f"\nfraction of orders containing it")
print((basket_df.mean().sort_values(ascending=False).round(4)).to_string())


# Running Apriori to find frequent itemsets


frequent_itemsets = apriori(
    basket_df,
    min_support=0.01,
    use_colnames=True,         
    max_len=2                  
)

frequent_itemsets["length"] = frequent_itemsets["itemsets"].apply(len)

print(f"\n  Frequent itemsets found: {len(frequent_itemsets)}")


# Generate association rule

rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=0.0
)

# Convert frozensets to readable strings for CSV export
rules["antecedents"] = rules["antecedents"].apply(lambda x: ", ".join(sorted(x)))
rules["consequents"] = rules["consequents"].apply(lambda x: ", ".join(sorted(x)))

# Round all metric columns to 4 decimal places
for col in ["support", "confidence", "lift", "leverage", "conviction"]:
    if col in rules.columns:
        rules[col] = rules[col].round(4)

# Sort by lift descending (strongest associations first)
rules = rules.sort_values("lift", ascending=False).reset_index(drop=True)

print(f"\n  Total association rules generated: {len(rules)}")
print(f"\n  Rules columns: {list(rules.columns)}")
print(f"\n  Lift range: {rules['lift'].min():.4f} – {rules['lift'].max():.4f}")
print(f"  Confidence range: {rules['confidence'].min():.4f} – {rules['confidence'].max():.4f}")
print(f"  Support range: {rules['support'].min():.4f} – {rules['support'].max():.4f}")

# STEP 8: Interpret lift results


rules_above_1 = rules[rules["lift"] > 1.0]   # positive association
rules_below_1 = rules[rules["lift"] < 1.0]   # independent
rules_equal_1 = rules[rules["lift"] == 1.0]  # negative association

rules.to_csv("basket_rules.csv", index=False)

frequent_itemsets["itemsets_str"] = frequent_itemsets["itemsets"].apply(
    lambda x: " + ".join(sorted(x))
)
frequent_itemsets[["itemsets_str", "support", "length"]].to_csv(
    "frequent_itemsets.csv", index=False
)

co_occurrence = (
    rules[["antecedents", "consequents", "support", "confidence", "lift"]]
    .drop_duplicates(subset=["support"])        # remove A→B / B→A duplicate support rows
    .sort_values("support", ascending=False)
    .head(20)
)
co_occurrence["support_pct"] = (co_occurrence["support"] * 100).round(2).astype(str) + "%"
co_occurrence.to_csv("top_cooccurrence_pairs.csv", index=False)


