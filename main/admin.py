from django.contrib import admin
from .models import Team, Teammate
from .forms import TeamForm

class TeammateInline(admin.TabularInline):
    model = Teammate
    extra = 1

class TeamAdmin(admin.ModelAdmin):
    inlines = [TeammateInline]

admin.site.register(Team, TeamAdmin)
admin.site.register(Teammate)
