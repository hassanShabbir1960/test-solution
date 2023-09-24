def calculate_average_price_per_foot(df, exclude_outliers=False):
    # Handle rows with sq__ft equal to zero
    df = df[df['sq__ft'] != 0]
    
    # Calculate price per foot
    df['price_per_foot'] = df['price'] / df['sq__ft']
    
    if exclude_outliers:
        # Calculate Q1 and Q3
        Q1 = df['price_per_foot'].quantile(0.25)
        Q3 = df['price_per_foot'].quantile(0.75)

        # Calculate IQR
        IQR = Q3 - Q1

        # Define bounds for the outliers
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR

        # Filter out outliers
        df = df[(df['price_per_foot'] >= lower_bound) & (df['price_per_foot'] <= upper_bound)]

    # Calculate and return the average price per foot
    return df['price_per_foot'].mean()

if __name__ == "__main__":

    import pandas as pd

    df = pd.read_csv('assignment data.csv')
    df['price_per_foot'] = df['price'] / df['sq__ft']

    average_price_per_foot = calculate_average_price_per_foot(df, exclude_outliers=False)

    # Filter rows where the price per foot is less than the average price per foot
    below_average_df = df[df['price_per_foot'] < average_price_per_foot]
    below_average_df.to_csv("Results.csv",index=False)
