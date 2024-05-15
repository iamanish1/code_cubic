from django.contrib import admin
from social_media.models import Courses
from social_media.models import projects
from social_media.models import Internship
from social_media.models import Community
from social_media.models import Reguserstud
from social_media.models import Reguserteach
from social_media.models import ReguserRec 
# Register your models here.
admin.site.register(Courses)
admin.site.register(projects)
admin.site.register(Internship)
admin.site.register(Community)
admin.site.register(Reguserstud)
admin.site.register(ReguserRec)
admin.site.register(Reguserteach)