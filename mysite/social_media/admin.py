from django.contrib import admin
from social_media.models import Reguser
from social_media.models import Courses
from social_media.models import projects
from social_media.models import Internship
from social_media.models import Community

# Register your models here.
admin.site.register(Reguser)
admin.site.register(Courses)
admin.site.register(projects)
admin.site.register(Internship)
admin.site.register(Community)