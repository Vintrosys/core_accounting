from . import __version__ as app_version

app_name = "core_accounting"
app_title = "core accounting"
app_publisher = "accounting"
app_description = "accounting"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "accounting@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/core_accounting/css/core_accounting.css"
# app_include_js = "/assets/core_accounting/js/core_accounting.js"

# include js, css files in header of web template
# web_include_css = "/assets/core_accounting/css/core_accounting.css"
# web_include_js = "/assets/core_accounting/js/core_accounting.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "core_accounting/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Company" : "patches/js/company.js",
"Sales Order":"patches/js/sales_order.js",
"Delivery Note":"patches/js/delivery_note.js",
"Sales Invoice":"patches/js/sales_invoice.js",
"Purchase Order":"patches/js/purchase_order.js",
"Purchase Receipt":"patches/js/purchase_receipt.js",
"Purchase Invoice":"patches/js/purchase_invoice.js",
"POS Invoice":"patches/js/pos_invoice.js",
"Item":"patches/js/item.js",
"Quotation": 'patches/js/quotation.js'
}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

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

# Installation
# ------------

# before_install = "core_accounting.install.before_install"
after_install = "core_accounting.patches.py.custom_field.execute"

# Uninstallation
# ------------

# before_uninstall = "core_accounting.uninstall.before_uninstall"
# after_uninstall = "core_accounting.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "core_accounting.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events
doc_events = {
	"Sales Invoice":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
		 "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],

	},
	"Sales Order":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
				    "core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
        			"core_accounting.patches.py.item_tax_percentage.item_tax_amount",
           ],
		   "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
	},
	"Purchase Invoice":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount",
         ],
		 "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
	},
	"Purchase Order":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
			"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
   			"core_accounting.patches.py.item_tax_percentage.item_tax_amount",
      ],
	  "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
	},
	"POS Invoice":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount",
         ],
		 "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
	},
	"Item":{
			"validate":"core_accounting.patches.py.item.data_import"
		},
	"Quotation":{
		"validate":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount",
         ],
		 "on_update_after_submit":["core_accounting.patches.py.tax_breakup_gst.ts_tax_breakup_separater",
					"core_accounting.patches.py.tax_breakup_hsn.ts_tax_breakup_separater",
     				"core_accounting.patches.py.item_tax_percentage.item_tax_amount"
         ],
	}
}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"core_accounting.tasks.all"
# 	],
# 	"daily": [
# 		"core_accounting.tasks.daily"
# 	],
# 	"hourly": [
# 		"core_accounting.tasks.hourly"
# 	],
# 	"weekly": [
# 		"core_accounting.tasks.weekly"
# 	]
# 	"monthly": [
# 		"core_accounting.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "core_accounting.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "core_accounting.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "core_accounting.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"core_accounting.auth.validate"
# ]

# Translation
# --------------------------------

# Make link fields search translated document names for these DocTypes
# Recommended only for DocTypes which have limited documents with untranslated names
# For example: Role, Gender, etc.
# translated_search_doctypes = []
