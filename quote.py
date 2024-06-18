from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        quote_data = response.json()
        quote = quote_data['content']
        author = quote_data['author']
    else:
        quote = "Не удалось получить цитату. Попробуйте позже."
        author = ""

    return render_template('quote_index.html', quote=quote, author=author)

@app.route('/quote')
def get_quote():
    response = requests.get('https://api.quotable.io/random')
    if response.status_code == 200:
        data = response.json()
        return jsonify(data)
    else:
        return jsonify({'content': 'Ошибка при получении цитаты', 'author': ''}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)