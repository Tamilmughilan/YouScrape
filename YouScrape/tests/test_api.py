from utils.api_handler import YouTubeAPIHandler

def test_fetch_channel_data():
    handler = YouTubeAPIHandler()
    data = handler.fetch_channel_data("https://www.youtube.com/channel/UC_x5XG1OV2P6uZZ5FSM9Ttw")
    assert len(data) > 0, "Channel data fetch failed"

def test_fetch_video_data():
    handler = YouTubeAPIHandler()
    data = handler.fetch_video_data("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    assert len(data) > 0, "Video data fetch failed"
