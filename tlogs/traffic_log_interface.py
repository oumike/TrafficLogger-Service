from flask_restful import Resource
from pymongo import MongoClient


class TrafficLogInterface(Resource):

    def __init__(self, mongodb_connection, parser):
        self.mongodb_connection = mongodb_connection
        self.parser = parser


    def get_logs_collection(self):
        client = MongoClient(self.mongodb_connection)
        return client.rachmaninoff.trafficlogs