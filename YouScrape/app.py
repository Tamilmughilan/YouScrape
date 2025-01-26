from flask import Flask, render_template, request
from utils.api_handler import YouTubeAPIHandler
from utils.data_cleaner import DataCleaner
from utils.visualizer import Visualizer
import os
import csv

app = Flask(__name__)

# Route for the home page
@app.route("/", methods=["GET", "POST"])
def index():
    video_data = None
    if request.method == "POST":
        url = request.form["url"]
        
        # Check if the URL is a valid YouTube URL
        if "youtube.com" in url:
            # Extract video ID and fetch data based on URL type (video/channel)
            video_id = url.split("v=")[-1].split("&")[0] if "watch" in url else None

            handler = YouTubeAPIHandler()
            data_cleaner = DataCleaner()
            visualizer = Visualizer()

            # Handle video or channel URL
            if "watch" in url:  # If it's a video URL
                data = handler.fetch_video_data(url)
            elif "channel" in url or '@' in url:  # If it's a channel URL
                data = handler.fetch_channel_data(url)
            else:
                return render_template("index.html", error="Invalid URL format. Please provide a valid video or channel URL.")
            
            # Clean the data and save it to CSV
            cleaned_data = data_cleaner.clean_data(data)
            data_cleaner.save_to_csv(cleaned_data, "data/extracted_data.csv")
            
            # Visualize data (optional)
            visualizer.plot_data(cleaned_data)

            # Return data to the frontend for display
            video_data = cleaned_data.to_dict(orient="records")  # Convert DataFrame to list of dicts
        else:
            video_data = {"error": "Invalid YouTube URL format. Please ensure it's a valid video or channel URL."}

    return render_template("index.html", video_data=video_data)

if __name__ == "__main__":
    app.run(debug=True)
