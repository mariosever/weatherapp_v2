import requests
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():

    query = "Tokyo"
    unit = "metric"
    api_key = "a584720c43c130d020ae58d96440565e"

    url = "https://api.openweathermap.org/data/2.5/weather?q={0}&units={1}&appid={2}&lang=HR".format(query, unit, api_key)

    data = requests.get(url=url)

    return render_template("index.html", data=data.json())

if __name__ == '__main__':
    app.run()