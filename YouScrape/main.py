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

    # Check if the URL is for a YouTube video or channel
    if "youtube.com" in args.url:
        if "channel" in args.url or '@' in args.url:  # Check for both channel and handle URLs
            data = handler.fetch_channel_data(args.url)
        elif "watch" in args.url:  # Check for video URL
            data = handler.fetch_video_data(args.url)
        else:
            print("Invalid URL provided. Please provide a valid video or channel URL.")
            return
    else:
        print("Invalid URL format provided. Ensure it's a valid YouTube URL.")
        return

    # Process the data
    cleaned_data = data_cleaner.clean_data(data)
    data_cleaner.save_to_csv(cleaned_data, "data/extracted_data.csv")
    visualizer.plot_data(cleaned_data)

if __name__ == "__main__":
    main()
