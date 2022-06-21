import csv
from flask import Flask, request, jsonify

app = Flask(__name__)

with open('articles.csv', encoding = "utf-8") as f:
    reader = csv.reader(f)
    articles = list(reader)
    all_articles = articles[1:]

liked_articles = []
disliked_articles = []

@app.route("/first")
def first():
    return jsonify({
        "data": all_articles[0],
        "message": "Success"
    }), 200

@app.route("/liked_articles", methods = ["POST"])
def get_liked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    liked_articles.append(article)

    return jsonify({
        "message": "Success"
    }), 200

@app.route("/disliked_articles", methods = ["POST"])
def get_disliked_articles():
    article = all_articles[0]
    all_articles = all_articles[1:]
    disliked_articles.append(article)

    return jsonify({
        "message": "Success"
    }), 200

if __name__ == "__main__":
    app.run()