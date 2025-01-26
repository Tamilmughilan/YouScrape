# YouTube Data Scraper

This project allows you to scrape YouTube video details such as title, description, view count, like count, and comment count using the YouTube API. You can also fetch the channel name associated with the video.

## Tech Stack

1. **Python**: Ensure you have Python 3.6 or higher installed on your machine.
2. **Google API Client**: This project uses Google’s API client to interact with the YouTube API.

## Getting Started

### Step 1: Clone the repository

```bash
git clone [https://github.com/yourusername/youtube-data-scraper.git](https://github.com/Tamilmughilan/YouScrape)

cd youtube-data-scraper
```

### Step 2: Install the dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Get a YouTube API Key

1. Use the api from [Google Cloud Console](https://console.cloud.google.com/).
2. Complete the signup and verification process.
3. Create a new project.
4. Navigate to the **APIs & Services** > **Credentials**.
5. Click on **Create Credentials** and select **API Key**.
6. Copy the generated API key and store it securely.

### Step 4: Replace the API Key

In `main.py`, replace the placeholder for the API key with the one you just created.

'''python
self.api_key = "YOUR_API_KEY_HERE"
'''

### Step 5: Running the Application

#### 1. To Run in Terminal -> `main.py`

The `main.py` script handles the YouTube API calls and data extraction. It fetches video details using the provided YouTube video URL. The results are stored in a dictionary and can be used in your application.

```bash
python main.py
```

#### 2. For more interactive interface -> `app.py`

The `app.py` script sets up a simple web application using Flask. It allows you to interact with the `main.py` script through a web interface. You can input a YouTube URL, and it will fetch the video details and display them on the webpage.

To run the app:

```bash
python app.py
```

This will start a Flask server, and you can access the application by navigating to `http://127.0.0.1:5000` in your web browser.

### Step 6: Interact with the Web Interface

- Once the Flask app is running, open your web browser and go to `http://127.0.0.1:5000`.
- Input the YouTube video URL in the text box and click **Fetch Data**.
- The page will display the video details, including title, channel name, view count, like count, and comment count.
  
### Example Output

After submitting a YouTube video URL, the output will display:

- **Video Title**
- **Channel Name**
- **Views**
- **Likes**
- **Comments**
- **Description**

## Dependencies

- `google-api-python-client`: Python client for accessing Google APIs
- `Flask`: Web framework for creating the app interface

Install them using:

```bash
pip install -r requirements.txt
```

