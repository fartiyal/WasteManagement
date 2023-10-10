from django.contrib import admin
from .models import WorkerDetails
@admin.register(WorkerDetails)
class WorkerDetailsAdmin(admin.ModelAdmin):
    list_display=('First_Name','Middle_Name','Last_Name','Mobile_Number','Gender','Age','Address','Pin_Code')
