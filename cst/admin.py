from django.contrib import admin
from cst import models

# Register your models here.

admin.site.register([models.Student, models.Class, models.Teacher])
