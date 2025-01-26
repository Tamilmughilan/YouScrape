import pandas as pd

class DataCleaner:
    def clean_data(self, data):
        
        df = pd.json_normalize(data)
        return df

    def save_to_csv(self, df, filepath):
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
