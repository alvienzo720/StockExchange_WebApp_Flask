from flask import Flask , render_template, request, url_for  
import requests
import json

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
	return render_template("home.html")


@app.route("/details", methods=["POST"])
def details():
	quotes = []
	ticker_data = request.form['ticker']
	requestResponse = requests.get("https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol="+ ticker_data + "&apikey=ZSYZ6WRPHPY4RUX8")
	json_object = requestResponse.json()
	quotes.append(json_object)
	return render_template("details.html", json_object=json_object['Global Quote'], quotes=quotes)



@app.route("/history", methods=["POST"])
def history():
	if request.method == "POST":
		ticker_data = request.form['ticker']
		requestResponse = requests.get("https://www.alphavantage.co/query?function=OVERVIEW&symbol="+ ticker_data+"&apikey=ZSYZ6WRPHPY4RUX8")
		company = requestResponse.json()
		return render_template("history.html", company=company)




 # ZSYZ6WRPHPY4RUX8 Alpha vantage API KEY 