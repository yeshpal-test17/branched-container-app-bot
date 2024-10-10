from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Root endpoint
@app.route('/', methods=['GET'])
def root():
    return 'Hello, ! World! what is up'

# Health check endpoint for Flask
@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=800)