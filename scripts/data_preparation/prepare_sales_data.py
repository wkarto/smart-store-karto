import pandas as pd

def clean_sales_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with missing critical fields
    df.dropna(subset=['TransactionID', 'CustomerID', 'ProductID', 'SaleAmount'], inplace=True)

    # Remove outliers in SaleAmount
    Q1 = df['SaleAmount'].quantile(0.25)
    Q3 = df['SaleAmount'].quantile(0.75)
    IQR = Q3 - Q1
    df = df[(df['SaleAmount'] >= (Q1 - 1.5 * IQR)) & (df['SaleAmount'] <= (Q3 + 1.5 * IQR))]

    # Ensure correct data types
    df['TransactionID'] = df['TransactionID'].astype(int)
    df['CustomerID'] = df['CustomerID'].astype(int)
    df['ProductID'] = df['ProductID'].astype(int)
    df['SaleAmount'] = df['SaleAmount'].astype(float)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned sales data saved to {output_path}")

if __name__ == "__main__":
    clean_sales_data("data/raw/sales_data.csv", "data/prepared/sales_data_prepared.csv")
