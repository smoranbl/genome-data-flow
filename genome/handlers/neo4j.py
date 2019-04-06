
from neo4j.v1 import GraphDatabase


class Neo4jHandler:

    # TODO: Temp constants for graph_db connection, pass to a config file
    URI = 'bolt://localhost:7687'
    USER = 'neo4j'
    PASS = 'admin'

    def __init__(self, uri=URI, user=USER, password=PASS):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def get_driver(self):
        return self._driver
