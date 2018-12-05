# -*- coding=utf-8 -*-
import pymongo

__author__ = 'STM'

client = pymongo.MongoClient(host='localhost')
db = client['test']
db['test_table'].insert_one({"name": "cxq", "age": 20})
