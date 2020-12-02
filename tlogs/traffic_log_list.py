from .traffic_log_interface import TrafficLogInterface
from flask_restful import Resource, Api, reqparse, abort
from flask import jsonify
from datetime import datetime
from bson.json_util import dumps
from pymongo import MongoClient
from pprint import pprint

class TrafficLogList(TrafficLogInterface):

    __name__ = "TrafficLogList"

    def get(self):
        logs_collection = self.get_logs_collection()
        logs = list(
                logs_collection.find())
        return dumps(logs, separators=(',', ':'))

    def post(self):
        args = self.parser.parse_args()
        logs_collection = self.get_logs_collection()

        # TODO : Figure out why date isn't converting from rest call
        if not args['date']:
            submission_date = datetime.now()
        else:
            submission_date = datetime.strptime(args['date'], '%m/%d/%y')

        all_logs = logs_collection.find({})

        max_id = -1
        for log in all_logs:
            if log["id"] > max_id:
                max_id = log["id"]

        next_id = max_id + 1

        log_json = {
            'id': next_id,
            'name': args['name'],
            'day': args['day'],
            'date': submission_date,
            'created_at': datetime.now()
        }

        logs_collection.insert_one(log_json)
        return dumps(log_json), 201