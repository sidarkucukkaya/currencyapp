from flask import Flask, render_template, request
import requests

apiKey = "6b48309ac53bede1d3c70c46831cc2d7"
url = "http://data.fixer.io/api/latest?access_key=" + apiKey

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency")   # name'e göre alındı. Birinci Para Birimi
        secondCurrency = request.form.get("secondCurrency") # İkinci Para Birimi
        amount = request.form.get("amount") # Miktar

        response = requests.get(url)    # get request atmak için requests metoduna url'imizi gönderdik. Başarılı sonuç alınırsa response alınmış olacak
        app.logger.info(response)   # response değerini console'da görmek
        
        infos = response.json() # respons'umuzu json verimize atadık.
        
        firstValue = infos["rates"][firstCurrency]  # json verisinde rates'teki ilk değer. rates de bir json verisi
        secondValue = infos["rates"][secondCurrency]

        result = (secondValue / firstValue)*float(amount)  # 1$ = ?TL

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        app.logger.info(infos)

        return render_template("index.html",info=currencyInfo)

    else:
        return render_template("index.html")

if (__name__ == "__main__"):
    app.run(debug=True)
