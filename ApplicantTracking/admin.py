from django.contrib import admin
from .models import Openings, Candidates, Pipeline, Placements, Account
# Register your models here.

admin.site.register(Openings)
admin.site.register(Candidates)
admin.site.register(Pipeline)
admin.site.register(Placements)
admin.site.register(Account)
