from flask import jsonify

def register_routes(app):
    @app.route("/")
    def home():
        return "Welcome to the Enhanced CI/CD Flask App!"

    @app.route("/health")
    def health_check():
        return jsonify(status="OK", message="Service is healthy.")
