# Example: Load Balancer Template (Heart)
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def balance():
    # Dummy logic to redirect to a service
    return redirect("http://localhost:5001")

if __name__ == '__main__':
    app.run(port=5000)