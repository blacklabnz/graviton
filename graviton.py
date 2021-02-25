from flask import Flask, Response
from datetime import datetime
import json

app = Flask(__name__)

@app.route('/')
def rt_default():
    resp = {
      'data': [{
        'type': 'response',
        'id': '2',
        'attributes': {
          'status': "success",
          'timestamp': datetime.now()
        }
      }]
    }
    resp_json = json.dumps(resp)
    return Response(resp_json, mimetype='application/json')

#if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=80)
