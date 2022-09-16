from django.contrib import admin

# Register your models here.
from .models import customUser, officeMail, officeSDI, userLan #, officeAdweb, userAdweb,userEmail,

# Register your models here.
# it allows to have a user friendly interface to input data in the db

#admin.site.register(User)
admin.site.register(customUser)

admin.site.register(officeMail)
#admin.site.register(officeAdweb)
admin.site.register(officeSDI)

#admin.site.register(userAdweb)
#admin.site.register(userEmail)
admin.site.register(userLan)
