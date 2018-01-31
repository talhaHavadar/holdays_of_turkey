from flask import Flask, jsonify
from holidayAgency import HolidayAgency

app = Flask(__name__)


@app.route("/holidays", methods=["GET"])
def get_holidays():
    return jsonify(sorted(HolidayAgency.get_holidays_for('tr'), key=lambda k: k['datetime']))

if __name__ == "__main__":
    app.run("0.0.0.0")