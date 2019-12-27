from flask import Flask, request, json, make_response

from dna.service import Dna
from dna.validator import Validator

app = Flask(__name__)

HOST: str = '0.0.0.0'
PORT: int = 5000


@app.route("/simian", methods=['POST'])
def simian() -> str:
    service = Dna()
    try:
        Validator.request(request.data)
        dna = json.loads(request.data).get("dna", [])
        item = service.store(dna)
        return make_response("", 200 if item.get('is_simian', False) else 403)
    except Exception as exc:
        return make_response({'status': "error", 'message': str(exc)}, 500)


@app.route("/stats", methods=['GET'])
def stats() -> str:
    service = Dna()
    return make_response(service.stats())


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
