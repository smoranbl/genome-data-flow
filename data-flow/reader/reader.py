
import settings as stt

from entities import Schema, Attribute
from reader import helpers as rh


# Variable to store a sheet service object and reuse it in the flow
sheet_service = None


# Instance object schema with json version of data dictionary layout
def load_schema(version, level):
    """
    :param version: string, Version of the required data dictionary schema, is used to construct the json path
    :param level: string, Level of the required data dictionary schema, it can be Object or Field
    :return: entities.dd_layout.Schema, Object Schema with data dictionary meta data
    """
    stt.logger.info('load_schema is being calling with the params: version={}, level={}'.
                    format(version, level))

    template = rh.get_schema_template(version, level)
    # Creates a list of Attribute object instances with loaded json distribution and order it
    attrs = map(lambda c: Attribute(c['name'], c['description'], c['position'], c['family'], c['group']), template)
    attrs = rh.order_schema_template(list(attrs))

    return Schema(version, level, attrs)


# Auth google sheets service and get data from defined sheet and spreadsheet range
def load_sheet(sheet_id, sheet_range, settings):
    """
    :param sheet_id: string, id of the required sheet
    :param sheet_range: string, range definition of the required spreadsheet
    :param settings: script with default constant project variables
    :return: list, return the content of the spreadsheet
    """
    stt.logger.info('load_sheet is being calling with the params: sheet_id={}, sheet_range={}'.
                    format(sheet_id, sheet_range))

    global sheet_service

    credentials = rh.get_credentials(settings.secret, settings.scope, settings.credentials)
    sheet_service = load_service(credentials)

    return rh.get_spreadsheet(sheet_service, sheet_id, sheet_range)


# Load Google API sheet service
def load_service(credentials):
    """
    :param credentials: oauth2client.client.Credentials, Credentials with the authorization token
    :return: service, A Resource object with methods for interacting with the service
    """
    stt.logger.info('load_service is being calling')

    global sheet_service

    return rh.get_sheet_service(credentials) if sheet_service is None else sheet_service
