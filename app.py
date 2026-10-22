
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def dashboard():
    with open("server.log", "r") as file:
        logs = file.readlines()

    error_count = sum("ERROR" in line for line in logs)
    warning_count = sum("WARNING" in line for line in logs)

    return render_template(
        "index.html",
        error_count=error_count,
        warning_count=warning_count,
        logs=logs
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
