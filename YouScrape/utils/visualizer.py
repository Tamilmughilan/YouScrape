import matplotlib.pyplot as plt

class Visualizer:
    def plot_data(self, df):
        if "statistics.viewCount" in df.columns:
            df["statistics.viewCount"] = df["statistics.viewCount"].astype(int)
            plt.bar(df["snippet.title"], df["statistics.viewCount"])
            plt.xlabel("Videos")
            plt.ylabel("Views")
            plt.title("Video Views")
            plt.xticks(rotation=45)
            plt.show()
        else:
            print("No view count data available to visualize.")
