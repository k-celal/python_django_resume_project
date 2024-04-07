from django.contrib import admin
from core.models import *
# Register your models here.
@admin.register(GeneralSetting)
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'parameter', 'updated_date', 'created_date')
    search_fields = ('name', 'description', 'parameter')
    list_editable = ('description', 'parameter')
    class Meta:
        model = GeneralSetting
@admin.register(ImageSetting)
class ImageSettingAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description', 'image', 'updated_date', 'created_date')
    search_fields = ('name', 'description')
    list_editable = ('description', 'image')
    class Meta:
        model = ImageSetting
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id','order','name', 'percentage', 'updated_date', 'created_date')
    search_fields = ('name', 'percentage')
    list_editable = ('order','name','percentage')
    class Meta:
        model = Skill
@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ('id','company', 'job_title', 'position', 'location','start_date', 'end_date', 'updated_date', 'created_date', )
    search_fields = ('company', 'job_title', 'position', 'location')
    list_editable = ('job_title', 'position', 'start_date', 'end_date', 'location')
    class Meta:
        model = Experience
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('id','school_name', 'major', 'department','location', 'start_date', 'updated_date', 'created_date')
    search_fields = ('school_name', 'major', 'department', 'location')
    list_editable = ('major', 'department', 'start_date', 'location')
    class Meta:
        model = Education
@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id','order','name','link','icon', 'updated_date', 'created_date')
    search_fields = ('name','icon', 'link')
    list_editable = ('order','name','link', 'icon')
    class Meta:
        model = SocialLink

@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id','order','slug','button_text','file', 'updated_date', 'created_date')
    search_fields = ('slug','button_text')
    list_editable = ('order','slug','button_text','file')
    class Meta:
        model = Documents