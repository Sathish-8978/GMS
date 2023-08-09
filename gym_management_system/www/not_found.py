# from frappe import _
# def get_context(context):
#     context.title = _('Not Found')
#     context.meesage = _('The requested page could not be found.')
#     return context

def get_context(context):
	context.http_status_code = 404
