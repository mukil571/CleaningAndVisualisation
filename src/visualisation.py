import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("output/plots", exist_ok=True)

def load_data():
    return pd.read_csv("D:/My DOCs/Intership-thiranex/CleaningAndVisualisation/CleaningAndVisualisation/Data/cleaned_data.csv")

def plot_income_distribution(df):
    plt.figure()
    sns.histplot(df['income'], kde=True)
    plt.title("Income Distribution")
    plt.savefig("output/plots/income_distribution.png")
    plt.close()

def plot_age_vs_income(df):
    plt.figure()
    sns.scatterplot(x='age', y='income', data=df)
    plt.title("Age vs Income")
    plt.savefig("output/plots/age_income.png")
    plt.close()

def plot_spending_vs_income(df):
    plt.figure()
    sns.scatterplot(x='income', y='spending_score', data=df)
    plt.title("Spending Score vs Income")
    plt.savefig("output/plots/spending_vs_income.png")
    plt.close()

def plot_credit_vs_balance(df):
    plt.figure()
    sns.scatterplot(x='credit_score', y='account_balance', data=df)
    plt.title("Credit Score vs Account Balance")
    plt.savefig("output/plots/credit_vs_balance.png")
    plt.close()

def correlation_heatmap(df):
    plt.figure(figsize=(10,6))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    plt.title("Feature Correlation Heatmap")
    plt.savefig("output/plots/correlation_heatmap.png")
    plt.close()

def main():
    df = load_data()

    plot_income_distribution(df)
    plot_age_vs_income(df)
    plot_spending_vs_income(df)
    plot_credit_vs_balance(df)
    correlation_heatmap(df)

    print("✅ All plots saved in output/plots/")

if __name__ == "__main__":
    main()
