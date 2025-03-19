from flask import Flask, request

# Tehtävä 13.1

app = Flask(__name__)


@app.route("/isPrime")
def summa():
    args = request.args
    luku = float(args.get("luku"))
    isPrime = False

    vastaus = {"Number": luku, "isPrime": isPrime}

    return vastaus


if __name__ == "__main__":
    app.run(use_reloader=True, host="127.0.0.1", port=3000)
