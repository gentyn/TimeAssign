from django.contrib import admin
from .models import myUser
from .models import Course
from .models import Break

# Register your models here.
admin.site.register(myUser)
admin.site.register(Course)
admin.site.register(Break)
