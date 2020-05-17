from flask import Flask, jsonify, request
from covid19 import Covid
app = Flask(__name__)
@app.route('/api/v1/tc/country=<country>', methods=['GET'])
def total_cases(country):
    return jsonify({country: Covid().get_country_data(country)})


if __name__ == '__main__':
    app.run(debug=True)
