from django.shortcuts import render, redirect, get_object_or_404
from core.models import GeneralSetting, ImageSetting, Skill, Experience, Education, SocialLink, Documents

def get_general_settings(parameter):
    try:
        obj = GeneralSetting.objects.get(name=parameter).parameter
    except:
        obj = ''
    return obj
def get_image_settings(parameter):
    try :
        obj = ImageSetting.objects.get(name=parameter).image
    except:
        obj = ''
    return obj
def layout(request):
    site_title = get_general_settings('site_title')
    site_keywords = get_general_settings("site_keywords")
    site_description = get_general_settings("site_description")
    home_banner_name = get_general_settings("home_banner_name")
    home_banner_title = get_general_settings("home_banner_title")
    home_banner_description = get_general_settings("home_banner_description")
    about_myself_footer = get_general_settings("about_myself_footer")
    about_myself_welcome = get_general_settings("about_myself_welcome")

    # images
    home_banner_image = get_image_settings("home_banner_image")
    header_logo = get_image_settings("header_logo")
    site_icon = get_image_settings("site_icon")

    # documents
    documents = Documents.objects.all().order_by('order')

    # social links
    social_links = SocialLink.objects.all().order_by('order')
    context = {
        'documents': documents,
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
        'social_links': social_links,
    }
    return context


# Create your views here.
def index(request):
    # Skills
    skills = Skill.objects.all().order_by('order')

    # experiences
    experiences = Experience.objects.all().order_by('-start_date')

    # education
    educations = Education.objects.all().order_by('-start_date')

    context = {
        'skills': skills,
        'experiences': experiences,
        'educations': educations,

    }
    return render(request, 'index.html', context=context)


def redirect_urls(request, slug):
    doc = get_object_or_404(Documents, slug=slug)
    return redirect(doc.file.url)
