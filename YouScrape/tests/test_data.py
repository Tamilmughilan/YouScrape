from utils.data_cleaner import DataCleaner
import pandas as pd

def test_clean_data():
    data_cleaner = DataCleaner()
    sample_data = [{"snippet.title": "Test Video", "statistics.viewCount": "1234"}]
    df = data_cleaner.clean_data(sample_data)
    assert isinstance(df, pd.DataFrame), "Cleaned data is not a DataFrame"

def test_save_to_csv():
    data_cleaner = DataCleaner()
    df = pd.DataFrame([{"title": "Test Video", "views": 1234}])
    data_cleaner.save_to_csv(df, "data/test.csv")
