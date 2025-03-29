import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r"C:\Users\imkc\OneDrive\Documents\Projects\Data Cleaning in Pandas\Taiwan Monthly Wage.csv")

df.drop_duplicates()

df.columns = ["Year_Month", "Industry_Services", "Male", "Female", "Industry", "Mining", "Manufacturing", "Electricity_Gas", "Water_Supply", "Construction", "Services", "Wholesale_Retail", "Transport_Storage", "Accommodation_Food", "Information_Communication", "Finance_Insurance", "Real_Estate", "Professional_Technical", "Support_Services", "Education", "Health_Social", "Arts_Entertainment", "Other_Services"]

df = df[df['Year_Month'].str.len() == 6]
df = df[df['Year_Month'] != '202501']
df['Year_Month'] = pd.to_datetime(df['Year_Month'], format='%Y%m').dt.strftime('%b %Y')

corr_matrix = df_numeric.corr()

plt.figure(figsize=(12, 8))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Columns")
plt.show()

df = df.drop(columns=["Industry_Services", "Education", "Industry", "Services", "Transport_Storage", "Support_Services"])
 
df.to_excel("cleaned_dataset.xlsx", index=False)