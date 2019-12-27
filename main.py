from flask import Flask, request, json, make_response

from dna.service import Dna

app = Flask(__name__)

HOST: str = 'localhost'
PORT: int = 5000


@app.route("/simian", methods=['POST'])
def simian() -> str:
    dna = json.loads(request.data).get("dna", "")
    service = Dna()
    try:
        item = service.store(dna)
        return make_response("", 200 if item.get('is_simian', False) else 403)
    except Exception as exc:
        return make_response(str(exc), 500)


@app.route("/stats", methods=['GET'])
def stats() -> str:
    service = Dna()
    return make_response(service.stats())


if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
