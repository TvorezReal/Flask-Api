from flask import Flask, render_template, request
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
   weather = None
   news = None
   if request.method == 'POST':
       city = request.form['city']
       weather = get_weather(city)
       news = get_news()
   return render_template("index.html", weather=weather, news=news)


#в функции прописываем город, который мы будем вводить в форме
def get_weather(city):
   api_key = "97aba1c9708dbacff0648ede33aedbb7"
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

def get_news():
   api_key = "a617b533135849c1b9cf361a6b4b84ea"
   url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
   response = requests.get(url)
   return response.json().get('articles', [])

if __name__ == '__main__':
   app.run(debug=True)