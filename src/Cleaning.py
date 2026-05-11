import pandas as pd

# Load dataset
def read_dataset(file_path):
    data = pd.read_csv(file_path)

    print("========== RAW DATA ==========")
    print(data.head())

    return data


# Fill missing values
def fill_missing_data(data):

    # Replace missing age with median age
    data["age"] = data["age"].fillna(data["age"].median())

    # Replace missing income with median income
    data["income"] = data["income"].fillna(data["income"].median())

    return data


# Remove duplicate rows
def delete_duplicates(data):

    before = len(data)

    data = data.drop_duplicates()

    after = len(data)

    print(f"\nDuplicates Removed: {before - after}")

    return data


# Detect and remove outliers
def remove_income_outliers(data):

    q1 = data["income"].quantile(0.25)
    q3 = data["income"].quantile(0.75)

    iqr = q3 - q1

    minimum_limit = q1 - (1.5 * iqr)
    maximum_limit = q3 + (1.5 * iqr)

    cleaned_data = data[
        (data["income"] >= minimum_limit) &
        (data["income"] <= maximum_limit)
    ]

    print("\nOutliers Removed:",
          len(data) - len(cleaned_data))

    return cleaned_data


# Main cleaning pipeline
def preprocess_dataset(file_path):

    data = read_dataset(file_path)

    data = fill_missing_data(data)

    data = delete_duplicates(data)

    data = remove_income_outliers(data)

    print("\n========== CLEANED DATA ==========")
    print(data.head())

    print("\n========== DATA SUMMARY ==========")
    print(data.describe())

    return data


# Execute program
if __name__ == "__main__":

    cleaned_df = preprocess_dataset(
        "D:/My DOCs/Intership-thiranex/CleaningAndVisualisation/CleaningAndVisualisation/Data/raw_data.csv"
    )

    cleaned_df.to_csv(
        "D:/My DOCs/Intership-thiranex/CleaningAndVisualisation/CleaningAndVisualisation/Data/cleaned_data.csv",
        index=False
    )

    print("\nCleaned dataset saved successfully.")
