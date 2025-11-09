from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/spellcast', methods=['POST'])
def cast_spell():
    data = request.json
    spell = data.get('spell')
    return jsonify({'result': f'You cast {spell} with glowing runes!'})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)