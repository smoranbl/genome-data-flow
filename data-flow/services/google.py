

from googleapiclient import discovery
from oauth2client import file, client, tools

import httplib2


# Default API scope for read spreadsheets in readonly mode
SCOPE = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# Default path for storage temporal credentials once the first
CRED = '../resources/google_api/credentials.json'
# Default path for the client secret json that contains the google_api values
SECRET = '../resources/google_api/client_id.json'

# Sheet service variable to reused it
sheet_service = None


# Create Google API credentials
def create_credentials(secret, scope, storage):
    """
    :param secret: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param storage: oauth2client.file.Storage, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    flow = client.flow_from_clientsecrets(filename=secret, scope=scope)
    # Execute all steps needed for get new authorization credentials
    return tools.run_flow(flow, storage)


# Get Google API credentials
def get_credentials(secret, scope, temp_cred):
    """
    :param secret: string, Contains the path for client secrets json parameters
    :param scope: string, Attribute for delimit the scope of the  Google API requests
    :param temp_cred: string, Contains the path for credentials.json temporal storage
    :return: oauth2client.client.Credentials, Credentials with the authorization token
    """
    storage = file.Storage(temp_cred)
    credentials = storage.get()
    # TODO: Pending to review the function "credentials.invalid" for exception management
    #       This function can throw a WARNING and the idea is to put it in a LOG.INFO
    # If temporal credentials is in force return it, other way create new credentials
    if not credentials or credentials.invalid:
        credentials = create_credentials(secret, scope, storage)

    return credentials


# Get Google API sheet service
def get_sheet_service(credentials):
    """
    :param credentials: oauth2client.client.Credentials, Credentials with the authorization token
    :return: service, A Resource object with methods for interacting with the service
    """
    # Build http request with the authorization credentials
    http = credentials.authorize(httplib2.Http())

    # Create a sheets service object
    return discovery.build(serviceName='sheets', version='v4', http=http)


# Load google API sheet_service when the file is imported
cred = get_credentials(SECRET, SCOPE, CRED)
sheet_service = get_sheet_service(cred) if sheet_service is None else sheet_service
