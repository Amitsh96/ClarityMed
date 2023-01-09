from django.contrib import admin
from .models import survey,doc_app,NavClass,clients1,recep_eq,order_recep,order_doc,doc_eq

# Register your models here.
admin.site.register(survey)
admin.site.register(doc_app)
admin.site.register(NavClass)
admin.site.register(clients1)
admin.site.register(recep_eq)
admin.site.register(order_recep)
admin.site.register(doc_eq)
admin.site.register(order_doc)