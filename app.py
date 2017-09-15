#!/usr/bin/env python
from bottle import route, run, response, request

import psycopg2
import json
import datetime
from sqlalchemy import create_engine, Table, MetaData, text, inspect
from sqlalchemy.orm import sessionmaker

'''
Generate a DB connection string
'''
def getDatabaseString():
    if not is_db_access_permitted():
        return error_400_http_response(ACCESS_NOT_GRANTED_ERROR_STRING)
    username = 'postgre'
    password = 'postgre'
    db_server = os.environ.get('OPENSHIFT_POSTGRESQL_DB_URL')
    db_port = os.environ.get('OPENSHIFT_POSTGRESQL_DB_PORT')
    database_name = testdb
    return "postgresql://"+username+":"+password+"@"+db_server+":"+db_port+"/"+database_name


def build_json(query_result_list, page=0):
    if page == 0:
        dictionary = {"count": 0, "result": []}
    else:
        dictionary = {"count": 0, "page": page, "result": []}
    dictionary["count"] = len(query_result_list)
    dictionary["result"] = query_result_list
    return json.dumps(dictionary, indent=2, default=json_serializer)


@route('/')
def get_tables():

    db_string = getDatabaseString()

    schema_name = 'postgres'
    engine = create_engine(db_string)
    inspector = inspect(engine)
    #schema_names = inspector.get_schema_names()
    table_names = inspector.get_table_names(schema_name)
    json_output = build_json(table_names)
    response.status = 200
    response.set_header('Content-Type', 'application/json')
    return json_output            


if __name__ == '__main__':
    # host IP added to avoid running on 127.0.0.1
    run(host='0.0.0.0', port=5000, debug=True)
