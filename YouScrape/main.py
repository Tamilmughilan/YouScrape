import argparse
from utils.api_handler import YouTubeAPIHandler
from utils.data_cleaner import DataCleaner
from utils.visualizer import Visualizer

def main():
    parser = argparse.ArgumentParser(description="YouTube Data Scraper")
    parser.add_argument("--url", type=str, required=True, help="YouTube video or channel URL")
    args = parser.parse_args()

    handler = YouTubeAPIHandler()
    data_cleaner = DataCleaner()
    visualizer = Visualizer()

    if "channel" in args.url:
        data = handler.fetch_channel_data(args.url)
    elif "watch" in args.url:
        data = handler.fetch_video_data(args.url)
    else:
        print("Invalid URL provided.")
        return

    cleaned_data = data_cleaner.clean_data(data)
    data_cleaner.save_to_csv(cleaned_data, "data/extracted_data.csv")
    visualizer.plot_data(cleaned_data)

if __name__ == "__main__":
    main()
