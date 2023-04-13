import frappe
from frappe.model.naming import parse_naming_series
import time
def name_outward_bank_payment(doc, action):
	ym = time.strftime("%y%m")
	if "gta.lnder.in" in frappe.utils.get_url():
		doc.name = parse_naming_series(f'OBP{ym}.#####')
	else:
		doc.name = parse_naming_series(f'DDBP{ym}.#####')