import pandas as pd

def clean_customers_data(input_path, output_path):
    df = pd.read_csv(input_path)

    # Remove duplicates
    df.drop_duplicates(inplace=True)

    # Drop rows with missing critical fields
    df.dropna(subset=['CustomerID', 'Name'], inplace=True)

    # Fill missing values and enforce data types
    df['LoyaltyPoints'] = df['LoyaltyPoints'].fillna(0).astype(int)
    df['CustomerID'] = df['CustomerID'].astype(int)

    # Save cleaned data
    df.to_csv(output_path, index=False)
    print(f"Cleaned customer data saved to {output_path}")

if __name__ == "__main__":
    clean_customers_data("data/raw/customers_data.csv", "data/prepared/customers_data_prepared.csv")
