from flask import Flask, render_template, jsonify, request
from get_data import get_latest_data, get_averages


app = Flask(__name__)


@app.route('/')
def frisk_pust_side():
    # Renders the clean dashboard layout skeleton
    return render_template('frisk_pust_side.html')



@app.route('/api/device-data')
def device_data():
    device_id = request.args.get('id')
    if not device_id:
        return jsonify({"error": "Missing device ID"}), 400
        
    data = get_latest_data(device_id)
    averages = get_averages(device_id)
    
    if not data:
        return jsonify({"error": "Device not found"}), 404
        
    return jsonify({
        "device_id": data[5], # index 5 from your database layout
        "temperature": data[2],
        "humidity": data[3],
        "air": data[4],
        "averages": averages
    })


if __name__ == '__main__':
    app.run(debug=True)

