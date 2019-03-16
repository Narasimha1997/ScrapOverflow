from flask import Flask, jsonify, request
from scraper import ScrapOverflow

app = Flask("__main__")

HOST = 'localhost'
PORT = 9800


@app.route('/api/search', methods = ['POST'])
def search() :

    data = request.get_json()

    count = data['count']

    question = data['question']

    scraper = ScrapOverflow(count)
    result = scraper.get_answers(scraper.get_html(question))

    return jsonify(result)

app.run(host = HOST, port = PORT)