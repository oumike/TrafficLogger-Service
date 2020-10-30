from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


traffic_logs = {}

class TrafficLog(Resource):
    def get(self, traffic_log_id):
        return {traffic_log_id: traffic_logs[traffic_log_id]}

    def put(self, traffic_log_id):
        traffic_logs[traffic_log_id] = request.form['data']
        return {traffic_log_id: traffic_logs[traffic_log_id]}

api.add_resource(TrafficLog, '/<string:traffic_log_id>')

if __name__ == '__main__':
    app.run(debug=True, port=8080)