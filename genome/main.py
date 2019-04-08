
import settings as stt

from reader import reader as r


stt.logger.info('Initializing Genome')

# Read data dictionary schema
schema = r.load_schema('v1.0', 'object')

# TODO: Need to make the spreadsheet reader part more dynamic, must be prepared
#  to load data from different PI and sections (MASTER, RAW nd CUSTOM)
# Read spreadsheets data
master_spreadsheet = r.load_sheet(stt.sheet_id, stt.master_range, stt)
raw_spreadsheet = r.load_sheet(stt.sheet_id, stt.raw_range, stt)

master_spreadsheet.extend(raw_spreadsheet)
print(master_spreadsheet)
