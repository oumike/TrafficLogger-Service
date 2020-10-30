from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
import datetime
from pprint import pprint


app = Flask(__name__)
api = Api(app)

TRAFFIC_LOGS = {
    1: {"name":"donny","day":"monday"}
}

def abort_if_todo_doesnt_exist(traffic_log_id):
    if traffic_log_id not in TRAFFIC_LOGS:
        abort(404, message="Log {} doesn't exist".format(traffic_log_id))

parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('day')



class TrafficLogList(Resource):
    def get(self):
        return TRAFFIC_LOGS

    def post(self):
        args = parser.parse_args()
        pprint(args)
        traffic_log_id = int(max(TRAFFIC_LOGS.keys())) + 1
        TRAFFIC_LOGS[traffic_log_id] = {'name': args['name'], 'day': args['day']}
        return TRAFFIC_LOGS[traffic_log_id], 201

class TrafficLog(Resource):
    def get(self, traffic_log_id):
        abort_if_todo_doesnt_exist(traffic_log_id)
        return TRAFFIC_LOGS[traffic_log_id]
        
    def put(self, traffic_log_id):
        args = parser.parse_args()
        traffic_log = {
            'name': args['name'],
            'day': args['day'],
            'created_at': datetime.now()
        }
        TRAFFIC_LOGS[traffic_log_id] = traffic_log_id
        return traffic_log, 201

    def delete(self, traffic_log_id):
        abort_if_todo_doesnt_exist(traffic_log_id)
        del TRAFFIC_LOGS[traffic_log_id]
        return '', 204


api.add_resource(TrafficLogList, '/tlogs')
api.add_resource(TrafficLog, '/tlogs/<traffic_log_id>')

if __name__ == '__main__':
    app.run(debug=True, port=5000)