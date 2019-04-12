
import settings as stt

from reader import reader as r
from process import process as p


stt.logger.info('Initializing Genome')

# Read data dictionary schema
schema = r.load_schema('v1.0', 'object')

# TODO: Need to make the spreadsheet reader part more dynamic, must be prepared
#  to load data from different PI and sections (MASTER, RAW nd CUSTOM)
# Read spreadsheets data
data = r.load_sheet(stt.sheet_id, stt.master_range, stt)
data.extend(r.load_sheet(stt.sheet_id, stt.raw_range, stt))

p.process_data(schema, data)
