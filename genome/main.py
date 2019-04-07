
import settings as stt

from reader import reader as r


spreadsheet = r.load_sheet(stt.g_sheet_id, stt.g_master_range, stt)
print(spreadsheet)

# l.logger.error('Hola esto es una prueba')
