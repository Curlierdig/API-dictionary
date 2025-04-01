from flask import Flask, render_template, request
from utils import get_definition, get_synonyms, get_youtube_video

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        word = request.form.get("word")
        definition = get_definition(word)
        synonyms = get_synonyms(word)
        youtube_url = get_youtube_video(word)
        return render_template("result.html", word=word, definition=definition, synonyms=synonyms, youtube_url=youtube_url)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
