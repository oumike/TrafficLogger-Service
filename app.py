from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse, abort
from pprint import pprint
from dotenv import load_dotenv
import os
from bson.json_util import dumps, loads 

from tlogs.traffic_log import TrafficLog
from tlogs.traffic_log_list import TrafficLogList

load_dotenv()

MONGODB_CONNECTION = os.getenv('MONGODB_CONNECTION')


app = Flask(__name__)
api = Api(app)

TRAFFIC_LOGS = {
    1: {"name":"donny","day":"monday"}
}


parser = reqparse.RequestParser()
parser.add_argument('name')
parser.add_argument('day')
parser.add_argument('date')


api.add_resource(TrafficLogList, '/tlogs', resource_class_kwargs={'parser': parser, 'mongodb_connection': MONGODB_CONNECTION})
api.add_resource(TrafficLog, '/tlogs/<traffic_log_id>', resource_class_kwargs={'parser': parser, 'mongodb_connection': MONGODB_CONNECTION})

if __name__ == '__main__':
    app.run(debug=True, port=os.getenv('TL_PORT'))