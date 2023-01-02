from django.contrib import admin
from .models import survey,doc_app,NavClass

# Register your models here.
admin.site.register(survey)
admin.site.register(doc_app)
admin.site.register(NavClass)

