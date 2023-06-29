import requests
import api
from flask import Flask, render_template, request
import time

app = Flask(__name__, template_folder="templates")




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert/", methods=["POST", "GET"])
def convert():
    """This is where the converter function is"""
    try:
        if request.method == "POST":

            base_currency = request.form["base_currency"].upper()
            converted_currency = request.form["converted_currency"].upper()
            amount = float(request.form["amount"])
            api_endpoint = f'https://api.frankfurter.app/latest?amount={amount}&from={base_currency}&to={ converted_currency }'

            response = requests.get(api_endpoint)
            data = response.json()
            if response.status_code == 200:
                if "error" in data:
                    result = "Error"
                else:
                    rate = data["rates"][converted_currency]
                    #converted_amount = amount * rate
                    result = f"{rate}"

            else:
                result = "API request failed", response.text

            return render_template("index.html", result=result)

    except Exception as e:
        return str(e)



if __name__== "__main__" :
    while True:
        app.run(debug=True)
        time.sleep(120)

