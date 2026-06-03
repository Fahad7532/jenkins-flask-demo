from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello world from Jenkins CI/CD + Docker! 2:05"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
