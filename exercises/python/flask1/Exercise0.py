"""
Flask: A minimal web application
"""


from flask import Flask, url_for

app = Flask(__name__)

postcodes = {
    "0001": "Oslo",
    "4036": "Stavanger",
    "4041": "Hafrsfjord",
    "7491": "Trondheim",
    "9019": "Tromsø"
}


@app.route("/")
def index():
    example_link = url_for("postcode_lookup", postcode="4041")
    return f"Postcode lookup service. Example usage: <a href='{example_link}'>{example_link}</a>"


@app.route("/postcode/<postcode>")
def postcode_lookup(postcode):
    if postcode in postcodes:
        city = postcodes[postcode]
        return f"Post code {postcode} is {city}"
    else:
        return f"Unknown post code ({postcode})"

if __name__ == "__main__":
    app.run()
