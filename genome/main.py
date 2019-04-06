
from helpers import context as ctx
from job import reader as r


def on_start():
    ctx.schema = r.load_schema('v1.0', 'object')
    ctx.G = r.load_network()


spreadsheet = r.load_sheet(ctx.g_sheet_id, ctx.g_master_range)

print(spreadsheet)
