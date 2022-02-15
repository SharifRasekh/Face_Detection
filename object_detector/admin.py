from django.contrib import admin
from .models import DetectionFile, DetectedObject
# Register your models here.

class DetectedObjecInline(admin.StackedInline):
    model = DetectedObject

class DetectionFileAdmin(admin.ModelAdmin):
    inlines = [
        DetectedObjecInline,
    ]

admin.site.register(DetectionFile, DetectionFileAdmin)