
import logging


# Default API scope for read spreadsheets in readonly mode
scope = 'https://www.googleapis.com/auth/spreadsheets.readonly'
# Default path for storage temporal credentials once the first
credentials = '../resources/google_api/credentials.json'
# Default path for the client secret json that contains the google_api values
secret = '../resources/google_api/client_id.json'
# Default sample sheet id for testing
sheet_id = '1p01TJG6K19E7_Abb0kDigZFOPCTIh9VZ7ZKLQCajgUc'
# Default sample sheet range of raw data for testing
raw_range = 'DC-DD-Object-RAW!A5:AI'
# Default sample sheet range of master data for testing
master_range = 'DC-DD-Object-MASTER!A5:AI'


# TODO: Must to reorganize all this logging stuff
# Create a custom logger
logger = logging.getLogger('GENOME')
logger.setLevel(logging.INFO)

# Create handlers, formatter and add it to handlers
c_handler = logging.StreamHandler()
c_format = logging.Formatter('%(asctime)s - [%(name)s][%(levelname)s]: %(message)s')
c_handler.setFormatter(c_format)

# Add handlers to the logger
logger.addHandler(c_handler)

if __name__ != '__main__':
    logger.info('Loading default variables configuration')