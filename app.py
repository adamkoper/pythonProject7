import requests
import csv
from flask import Flask, render_template, request, redirect

response = requests.get("http://api.nbp.pl/api/exchangerates/tables/C?format=json")
data = response.json()
rates = data[0].get('rates')

app = Flask(__name__)

def get_codes():
    codes = []
    for data in rates:
        codes.append(data.get('code'))
    return sorted(codes)

codes = get_codes()

with open('rates.csv', 'w') as csvfile:
    fieldnames = ['currency', 'code', 'bid', 'ask']
    writer = csv.DictWriter(csvfile, delimiter=';', fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rates)


@app.route("/login/", methods=["GET", "POST"])
def message():
    return render_template("templates.html", codes=codes)







