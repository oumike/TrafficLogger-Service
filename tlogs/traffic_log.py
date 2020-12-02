from .traffic_log_interface import TrafficLogInterface
from bson.json_util import dumps
from flask import jsonify
from datetime import datetime


class TrafficLog(TrafficLogInterface):

    __name__ = "TrafficLog"

    def get(self, traffic_log_id):
        
        logs_collection = self.get_logs_collection()
        log = logs_collection.find_one({"id":int(traffic_log_id)})

        return dumps(log), 201
        
    def put(self, traffic_log_id):
        args = self.parser.parse_args()

        # TODO : Figure out why date isn't converting from rest call
        if not args['date']:
            submission_date = datetime.now()
        else:
            submission_date = datetime.strptime(args['date'], '%m/%d/%y')

        log_json = {
            'id': traffic_log_id,
            'name': args['name'],
            'day': args['day'],
            'date': submission_date,
            'created_at': datetime.now()
        }

        logs_collection = self.get_logs_collection()
        logs_collection.replace_one({"id":int(traffic_log_id)}, log_json, upsert=True)

        return log_json, 201

    def delete(self, traffic_log_id):
        logs_collection = self.get_logs_collection()
        logs_collection.delete_one({"id":int(traffic_log_id)})
        return '', 204

