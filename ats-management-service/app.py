import connexion
from flask import Flask
from flask_cors import CORS

import settings

app = connexion.FlaskApp(
    __name__, specification_dir="./swagger/", options={"swagger_ui": False}
)
app.add_api("swagger.yaml")
cors = CORS(app.app, resources={r"*": {"origins": "*"}})
# app.app.config.from_object(settings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route("/test", methods=["GET", "POST", "OPTIONS"])
def home_test():
    return {}
