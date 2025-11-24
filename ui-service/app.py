from flask import Flask, render_template, request
import requests

app = Flask(__name__)

PROCESSOR_API = "http://processor:4000/process"   # Kubernetes Service name

@app.route("/", methods=["GET"])
def home():
    return render_template("form.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = {
        "name": request.form["name"],
        "age": request.form["age"],
        "gmail": request.form["gmail"],
        "branch": request.form["branch"],
        "rollno": request.form["rollno"]
    }

    try:
        res = requests.post(PROCESSOR_API, json=data)
        return res.text
    except:
        return "Processor service is not reachable!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
