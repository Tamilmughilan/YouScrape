from googleapiclient.discovery import build

class YouTubeAPIHandler:
    def __init__(self):
        self.api_key = "YOUR_API_KEY"
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def fetch_channel_data(self, channel_url):
        
        channel_id = self._extract_id(channel_url)
        response = self.youtube.channels().list(part="snippet,statistics", id=channel_id).execute()
        return response.get("items", [])

    def fetch_video_data(self, video_url):
        
        video_id = self._extract_id(video_url)
        response = self.youtube.videos().list(part="snippet,statistics", id=video_id).execute()
        return response.get("items", [])

    def _extract_id(self, url):
        if "channel" in url:
            return url.split("/")[-1]
        elif "watch" in url:
            return url.split("v=")[-1].split("&")[0]
