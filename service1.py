# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__, template_folder="templates")

# @app.route("/")
# def hello():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.get_json()  # Retrieve the data as JSON
#     print("Data received:", data)
#     # Process the data using Python code
#     # result = data['latitude'] + data['longitude']  # Process the data
#     return jsonify(result="Data received successfully")

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__, template_folder="templates")

# @app.route("/")
# def hello():
#     return render_template('index.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.get_json()
#     print("Data received:", data)
#     return jsonify(result="Data received successfully")

# @app.route('/get_geolocation', methods=['GET'])  # New route for the GET request
# def get_geolocation():
#     # Simulate geolocation data as a dictionary
#     geolocation_data = {
#         'latitude': 40.7128,
#         'longitude': -74.0060
#     }
#     return jsonify(geolocation_data)

# if __name__ == '__main__':
#     app.run(host = '0.0.0.0', port = 8001, debug=True)




# from flask import Flask, render_template, request, jsonify

# app = Flask(__name__, template_folder="templates")

# # @app.route("/")
# # def hello():
# #     return render_template('index.html')

# @app.route('/')
# def hello():
#     return render_template('main.html')

# @app.route('/signup')
# def signup():
#     return render_template('signup.html')

# @app.route('/process', methods=['POST'])
# def process():
#     data = request.get_json()  # Retrieve the data as JSON
#     print("Data received:", data)
#     # Process the data using Python code
#     # result = data['latitude'] + data['longitude']  # Process the data
#     return jsonify(result="Data received successfully")

# @app.route('/get_geolocation', methods=['GET'])  # New route for the GET request
# def get_geolocation():
#     # Simulate geolocation data as a dictionary
#     geolocation_data = {
#         'latitude': 40.7128,
#         'longitude': -74.0060
#     }
#     return jsonify(geolocation_data)
# if __name__ == '__main__':
#     app.run(debug=True)






from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__, template_folder="templates")

# Define the URL of service2
service2_url = "http://127.0.0.1:8002"

@app.route('/')
def hello():
    return render_template('main.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

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
    

# @app.route('/', methods=['GET'])
# def process():
#     data = request.get_json()  # Retrieve the data as JSON
#     print("Data received:", data)
    
#     # Send a POST request to service2
#     response = requests.post(f"{service2_url}/calculate_match_percentage", json=data)
    
#     if response.status_code == 200:
#         result = response.json()
#         return jsonify(result=result)
#     else:
#         return jsonify(error="Failed to communicate with service2")

@app.route('/get_geolocation', methods=['GET'])
def get_geolocation():
    response = requests.get(f"{service2_url}/get_geolocation")
    
    if response.status_code == 200:
        geolocation_data = response.json()
        return jsonify(geolocation_data)
    else:
        return jsonify(error="Failed to get geolocation data from service2")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True)
