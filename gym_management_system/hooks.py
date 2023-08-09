from . import __version__ as app_version

app_name = "gym_management_system"
app_title = "Gym Management System"
app_publisher = "Sathish Kumar"
app_description = "Gym management system"
app_email = "sathishkumardev07@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gym_management_system/css/gym_management_system.css"
# app_include_js = "/assets/gym_management_system/js/gym_management_system.js"

# include js, css files in header of web template
# web_include_css = "/assets/gym_management_system/css/gym_management_system.css"
# web_include_js = "/assets/gym_management_system/js/gym_management_system.js"

# web_include_js = {
#     "404": "gym_management_system/gym_management_system/www/404_page.js"
# }
# hooks.py

# web_include_js = {
#     "all": [
#         "gym_management_system/gym_management_system/www/404_page.js"
#     ]
# }
# website_catch_all = "Not found"

# website_catch_all = "gym_management_system.gym_management_system.WWW.not_found.html"

# update_website_context = ["frappe_docs.website_context.get_context"]

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gym_management_system/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
# extend_website_page_controller_context = {
#     "frappe.www.404": "gym_management_system.gym_management_system.www.not_found"
# }

# website_catch_all = "not_found"


# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "gym_management_system.utils.jinja_methods",
#	"filters": "gym_management_system.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gym_management_system.install.before_install"
# after_install = "gym_management_system.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gym_management_system.uninstall.before_uninstall"
# after_uninstall = "gym_management_system.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gym_management_system.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# hooks.py

doc_events = {
    "Gym membership": {
        # "onload": "gym_management_system.gym_management_system.doctype.gym_member.create_gym_member",
        "before_save": "gym_management_system.gym_management_system.doctype.gym_membership.gym_membership.calculate_remaining_days",
        "validate": "gym_management_system.gym_management_system.doctype.gym_membership.gym_membership.calculate_remaining_days"
    }
}

# doc_events = {
# 	"Gym membership": {
# 		"before_save": "gym_management_system.gym_management_system.doctype.gym_membership.gym_membership.before_save"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"gym_management_system.tasks.all"
#	],
#	"daily": [
#		"gym_management_system.tasks.daily"
#	],
#	"hourly": [
#		"gym_management_system.tasks.hourly"
#	],
#	"weekly": [
#		"gym_management_system.tasks.weekly"
#	],
#	"monthly": [
#		"gym_management_system.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "gym_management_system.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "gym_management_system.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "gym_management_system.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gym_management_system.utils.before_request"]
# after_request = ["gym_management_system.utils.after_request"]

# Job Events
# ----------
# before_job = ["gym_management_system.utils.before_job"]
# after_job = ["gym_management_system.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"gym_management_system.auth.validate"
# ]
