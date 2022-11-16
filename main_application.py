from flask import Flask, Response, request
from datetime import datetime
import json
from flask_cors import CORS

# Create the Flask application object.
app = Flask(__name__,
            static_url_path='/',
            static_folder='static/class-ui/',
            template_folder='web/templates')

CORS(app)


@app.get("/api/health")
def get_health():
    t = str(datetime.now())
    msg = {
        "name": "6156_team_project_shoppinglist_microservice",
        "Status": "Connected",
        "at time": t
    }

    # DFF TODO Explain status codes, content type, ... ...
    result = Response(json.dumps(msg), status=200, content_type="application/json")

    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5011)

