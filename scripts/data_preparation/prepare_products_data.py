import pandas as pd

def clean_products_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Fill missing values and enforce data types
    df['UnitPrice'] = df['UnitPrice'].fillna(df['UnitPrice'].median()).astype(float)
    df['StockQuantity'] = df['StockQuantity'].fillna(0).astype(int)
    df['ProductID'] = df['ProductID'].astype(int)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned product data saved to {output_path}")

if __name__ == "__main__":
    clean_products_data("data/raw/products_data.csv", "data/prepared/products_data_prepared.csv")
