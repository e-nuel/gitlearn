import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='testcallback.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/callback', methods=['POST'])
def callback():
    if request.method == 'POST':
	#Getting the IP
        if request.headers.getlist("X-Forwarded-For"):
            client_ip = request.headers.getlist("X-Forwarded-For")[0]
        else:
            client_ip = request.remote_addr
        
        logging.info('Received request from IP: %s', client_ip)

        # Get the payload data from the request
        payload_data = request.data.decode('utf-8')  # Assuming UTF-8 encoding
        logging.info('Received webhook payload: %s', payload_data)

        # You can also parse the payload as JSON if it's in JSON format
        try:
            json_data = request.get_json()
            logging.info('Received webhook JSON data: %s', json_data)
        except Exception as e:
            logging.error('Failed to parse JSON data: %s', str(e))

        # Perform your processing here

        # Return a response using jsonify
        response_data = {'message': 'Received POST request successfully'}
        return jsonify(response_data), 200  # 200 OK status code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000)  # Run the application on port  4000
