from django.contrib import admin
from issue_tracker.app import models

admin.site.register(models.Issue)
admin.site.register(models.IssueComment)
