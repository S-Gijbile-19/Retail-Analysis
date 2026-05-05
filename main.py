import pandas as pd

# Load data
rfm = pd.read_csv("RESULT.csv")

print(rfm.head())
print(rfm.dtypes)
print(rfm.describe())

# Convert to numeric (important)
rfm['Recency'] = pd.to_numeric(rfm['Recency'], errors='coerce')
rfm['Frequency'] = pd.to_numeric(rfm['Frequency'], errors='coerce')
rfm['Monetary'] = pd.to_numeric(rfm['Monetary'], errors='coerce')

# Drop missing values
rfm = rfm.dropna()

# RFM Score (SAFE version)
rfm['R_score'] = pd.qcut(rfm['Recency'], 5, labels=[5,4,3,2,1], duplicates='drop')
rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method='first'), 5, labels=[1,2,3,4,5], duplicates='drop')
rfm['M_score'] = pd.qcut(rfm['Monetary'], 5, labels=[1,2,3,4,5], duplicates='drop')

# Convert to int
rfm['R_score'] = rfm['R_score'].astype(int)
rfm['F_score'] = rfm['F_score'].astype(int)
rfm['M_score'] = rfm['M_score'].astype(int)

# Combine score
rfm['RFM_Score'] = (
    rfm['R_score'].astype(str) +
    rfm['F_score'].astype(str) +
    rfm['M_score'].astype(str)
)

# Assign Segments
def segment(row):
    if row['R_score'] == 5 and row['F_score'] >= 4 and row['M_score'] >= 4:
        return 'Champions'
    elif row['R_score'] >= 4 and row['F_score'] >= 3:
        return 'Loyal Customers'
    elif row['R_score'] >= 4:
        return 'Potential Loyalists'
    elif row['R_score'] == 3:
        return 'Need Attention'
    elif row['R_score'] <= 2 and row['F_score'] >= 3:
        return 'At Risk'
    else:
        return 'Hibernating'

rfm['Segment'] = rfm.apply(segment, axis=1)

# Output
print(rfm.head())

print("\nSegment Distribution:\n")
print(rfm['Segment'].value_counts())

# Validation 
print("\nValidation:\n")
print(rfm.groupby('Segment')[['Recency','Frequency','Monetary']].mean())

# Save final file
rfm.to_excel("final_rfm.xlsx", index=False)
