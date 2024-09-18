from bank_api_integration.bank_api_integration.utils.bank_transaction.custom_field import bt_field_customization

def after_migrate():
	bt_field_customization()