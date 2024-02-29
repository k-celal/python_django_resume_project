from django.shortcuts import render
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialLink


# Create your views here.
def index(request):
    site_title = GeneralSetting.objects.get(name='site_title').parameter
    site_keywords = GeneralSetting.objects.get(name='site_keywords').parameter
    site_description = GeneralSetting.objects.get(name='site_description').parameter
    home_banner_name=GeneralSetting.objects.get(name='home_banner_name').parameter
    home_banner_title=GeneralSetting.objects.get(name='home_banner_title').parameter
    home_banner_description=GeneralSetting.objects.get(name='home_banner_description').parameter
    about_myself_footer=GeneralSetting.objects.get(name='about_myself_footer').parameter
    about_myself_welcome=GeneralSetting.objects.get(name='about_myself_welcome').parameter

    #images
    home_banner_image=ImageSetting.objects.get(name='home_banner_image').image
    header_logo=ImageSetting.objects.get(name='header_logo').image
    site_icon=ImageSetting.objects.get(name='site_icon').image

    #Skills
    skills = Skill.objects.all().order_by('order')

    #experiences
    experiences = Experience.objects.all().order_by('-start_date')

    #education
    educations = Education.objects.all().order_by('-start_date')

    #social links
    social_links = SocialLink.objects.all().order_by('order')
    context = {
        'site_title': site_title,
        'site_keywords': site_keywords,
        'site_description': site_description,
        'home_banner_name': home_banner_name,
        'home_banner_title': home_banner_title,
        'home_banner_description': home_banner_description,
        'about_myself_footer': about_myself_footer,
        'about_myself_welcome': about_myself_welcome,
        'home_banner_image': home_banner_image,
        'header_logo': header_logo,
        'site_icon': site_icon,
        'skills': skills,
        'experiences': experiences,
        'educations': educations,
        'social_links': social_links,
        }
    return render(request, 'index.html',context=context)
