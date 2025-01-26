from googleapiclient.discovery import build

class YouTubeAPIHandler:
    def __init__(self):
        self.api_key = "API KEY HERE"
        self.youtube = build("youtube", "v3", developerKey=self.api_key)

    def fetch_channel_data(self, url):
        if '@' in url:
            handle = url.split('@')[1]
            response = self.youtube.channels().list(
                part="snippet,statistics",
                forUsername=handle  
            ).execute()
        else:
            channel_id = self._extract_id(url)
            response = self.youtube.channels().list(
                part="snippet,statistics",
                id=channel_id  
            ).execute()

        return response

    def fetch_video_data(self, url):
        video_id = self._extract_id(url)
        
        video_response = self.youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        ).execute()

        if video_response["items"]:
            video_item = video_response["items"][0]
            video_data = {
                "video_id": video_id,
                "title": video_item["snippet"]["title"],
                "description": video_item["snippet"]["description"],
                "view_count": video_item["statistics"].get("viewCount", "Not Available"),
                "like_count": video_item["statistics"].get("likeCount", "Not Available"),
                "comment_count": video_item["statistics"].get("commentCount", "Not Available"),
            }
        else:
            video_data = {
                "video_id": video_id,
                "title": "Not Available",
                "description": "Not Available",
                "view_count": "Not Available",
                "like_count": "Not Available",
                "comment_count": "Not Available",
            }

        return video_data


    def _extract_id(self, url):
        """Extract channel or video ID from the URL."""
        if "channel" in url:
            return url.split("/")[-1]
        elif "watch" in url:
            return url.split("v=")[-1].split("&")[0]
        else:
            raise ValueError("Invalid YouTube URL provided.")
