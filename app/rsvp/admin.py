from django.contrib import admin

from .models import Invitation, Invitee


class InvitationAdmin(admin.ModelAdmin):
    pass

class InviteeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Invitee, InviteeAdmin)
