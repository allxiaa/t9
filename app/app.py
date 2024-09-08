from flask import Flask, request
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
metrics = PrometheusMetrics(app)

@app.route('/submit', methods=['POST'])
def submit():
    value = request.form['value']
    print(f'Received value: {value}')  # Log the received value
    return 'Value submitted!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
