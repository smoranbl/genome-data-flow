
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

    # Create a object node.
    @classmethod
    def create_object(cls, tx, object_schema, attributes):
        tx.run('CREATE (:Object {{{}}})'.format(object_schema), attributes)

    # Create a field node.
    @classmethod
    def create_field(cls, tx, field_schema, attributes):
        tx.run('CREATE (:Field {{{}}})'.format(field_schema), attributes)

    # Create a forward_to relationship between a pre-existing objects node.
    @classmethod
    def create_forward_to_relationship(cls, tx, from_name, to_name):
        tx.run("MATCH (raw:Object {physical_name: $from_name}) "
               "MATCH (master:Object {physical_name: $to_name}) "
               "CREATE (raw)-[:FORWARD_TO]->(master)",
               from_name=from_name, to_name=to_name)

    # Create a have_to relationship between a pre-existing objects node.
    @classmethod
    def create_forward_to_relationship(cls, tx, from_name, to_name):
        tx.run("MATCH (raw:Object {physical_name: $from_name}) "
               "MATCH (master:Object {physical_name: $to_name}) "
               "CREATE (raw)-[:FORWARD_TO]->(master)",
               from_name=from_name, to_name=to_name)
