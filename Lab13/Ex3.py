from flask import Flask
import requests

app = Flask(__name__)

@app.route("/")
def home():
    url = "https://meme-api.com/gimme/wholesomememes"

    # GET request to retrieve meme data
    response = requests.request("GET", url)

    meme_data = response.json()

    meme_url = meme_data["url"]
    subreddit = meme_data["subreddit"]

    # HTML page
    html = f"""
    <html>
    <head>
       <title>Memes'R'Us</title>
       <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
       <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000" />
    </head>
    <body style="text-align:center; font-family:Arial;">
        <h1>Welcome to Memes'R'Us</h1>
        <h3>Source: r/{subreddit}</h3>
        <img src="{meme_url}" width="500">
        <p>Refreshing every 10 seconds...</p>
    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(debug=True)