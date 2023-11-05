from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="templates")

# Define the URL of service2
service2_url = "http://127.0.0.1:8002"

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/mainPage')  # Define a route for mainPage
def mainPage():
    return render_template('mainPage.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()  # Retrieve the data as JSON
    print("Data received:", data)
    
    # Send a POST request to service2
    response = requests.post(f"{service2_url}/calculate_match_percentage", json=data)
    
    if response.status_code == 200:
        result = response.json()
        return jsonify(result=result)
    else:
        return jsonify(error="Failed to communicate with service2")

@app.route('/get_geolocation', methods=['GET'])
def get_geolocation():
    response = requests.get(f"{service2_url}/get_geolocation")
    
    if response.status_code == 200:
        geolocation_data = response.json()
        return jsonify(geolocation_data)
    else:
        return jsonify(error="Failed to get geolocation data from service2")
    
@app.route('/submit_form', methods=['POST'])
def submit_form():
    data = request.get_json()  # Retrieve the data as JSON
    print("Data received from front end:", data)
    
    # Process the data or perform any required actions
    
    # Return a response to the front end
    response_data = {'message': 'Form data received successfully'}
    return jsonify(response_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
