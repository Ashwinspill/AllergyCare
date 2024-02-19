# file created: 2024-02-18 06:14:00.817681

# this files has been generated by CandyTranslate.com  Please do not change manually
# author: Next Level Sense

# Available functions:
#    render - replacement for django render function
#    path - replacement for django path function. please use with * when replacing in urls.py
#    supported_languages - list that contains all available languages for this site
# Functions to be used in django templates:
#    languageReferences - create 'alternate' language references for SEO.
#        put it inside of the <head> section of the page in format {{languageReferences|safe}}
#    lang - current language. Used mostly in <html lang="{{lang}}">
#    languageMenu - adding language selection for your page. Format: {{languageMenu|safe}}
#    <<link variables>> - create linking to correct language link. 
#    usage:
#    for translated pages change {% url "my_page" %}
#    to name without quotes:     {% url my_page %}


supported_languages = ['en', 'ar', 'bn', 'zh', 'de', 'hi', 'pa', 'ur']

def translation_dictionary(lang):
    if lang == 'en': return {
        'phome_welcome':'''Welcome,''',
        'phome_home':'''Home''',
        'phome_doctor':'''Doctors''',
        'phome_clinic':'''Clinics''',
        'phome_medicines':'''Medicines''',
        'phome_other':'''Other''',
        'phome_myprofile':'''My Profile''',
        'phome_replies':'''Replies''',
        'phome_testimonials':'''Testimonials''',
        'phome_logout':'''Logout''',
        'phome_best':'''Best care for your allergies''',
        'phome_medicine':'''Medicines''',
        'phome_appointment':'''Appointment''',
        'phome_welcomet':'''Welcome To AllergyCare''',
        'phome_odoctors':'''Our Doctors''',
        'phome_qhp':'''Qualified Healthcare Professionals''',
        'phome_tmnls':'''Testimonials''',
        'phome_git':'''Get In Touch''',
        'phome_ps':'''We are here provide you with the best care possible from our side.''',
        'phome_newsletter':'''Newsletter''',
        'phome_follow':'''Follow Us''',
        }
    if lang == 'ar': return {
        'phome_welcome':'''مرحباً،''',
        'phome_home':'''بيت''',
        'phome_doctor':'''الأطباء''',
        'phome_clinic':'''العيادات''',
        'phome_medicines':'''الأدوية''',
        'phome_other':'''آخر''',
        'phome_myprofile':'''ملفي''',
        'phome_replies':'''الردود''',
        'phome_testimonials':'''الشهادات - التوصيات''',
        'phome_logout':'''تسجيل خروج''',
        'phome_best':'''أفضل رعاية لحساسيةكم''',
        'phome_medicine':'''الأدوية''',
        'phome_appointment':'''ميعاد''',
        'phome_welcomet':'''مرحبا بكم في حساسية الرعاية''',
        'phome_odoctors':'''أطبائنا''',
        'phome_qhp':'''المهنيون في مجال الرعاية الصحية المؤهلين''',
        'phome_tmnls':'''الشهادات - التوصيات''',
        'phome_git':'''ابقى على تواصل''',
        'phome_ps':'''نحن هنا نوفر لك أفضل رعاية ممكنة من جانبنا.''',
        'phome_newsletter':'''النشرة الإخبارية''',
        'phome_follow':'''تابعنا''',
        }
    if lang == 'bn': return {
        'phome_welcome':'''স্বাগত,''',
        'phome_home':'''বাড়ি''',
        'phome_doctor':'''চিকিত্সকরা''',
        'phome_clinic':'''ক্লিনিক''',
        'phome_medicines':'''ওষুধগুলো''',
        'phome_other':'''অন্য''',
        'phome_myprofile':'''আমার প্রোফাইল''',
        'phome_replies':'''উত্তর''',
        'phome_testimonials':'''প্রশংসাপত্র''',
        'phome_logout':'''প্রস্থান''',
        'phome_best':'''আপনার অ্যালার্জির জন্য সেরা যত্ন''',
        'phome_medicine':'''ওষুধগুলো''',
        'phome_appointment':'''অ্যাপয়েন্টমেন্ট''',
        'phome_welcomet':'''অ্যালার্জি কেয়ারে আপনাকে স্বাগতম''',
        'phome_odoctors':'''আমাদের ডাক্তার''',
        'phome_qhp':'''যোগ্য স্বাস্থ্যসেবা পেশাদার''',
        'phome_tmnls':'''প্রশংসাপত্র''',
        'phome_git':'''যোগাযোগ পেতে''',
        'phome_ps':'''আমরা এখানে আপনাকে আমাদের পক্ষ থেকে সর্বোত্তম যত্ন প্রদান করছি।''',
        'phome_newsletter':'''নিউজলেটার''',
        'phome_follow':'''আমাদের অনুসরণ করো''',
        }
    if lang == 'zh': return {
        'phome_welcome':'''欢迎，''',
        'phome_home':'''家''',
        'phome_doctor':'''医生''',
        'phome_clinic':'''诊所''',
        'phome_medicines':'''药物''',
        'phome_other':'''其他''',
        'phome_myprofile':'''我的简历''',
        'phome_replies':'''答复''',
        'phome_testimonials':'''推荐''',
        'phome_logout':'''登出''',
        'phome_best':'''对过敏的最佳护理''',
        'phome_medicine':'''药物''',
        'phome_appointment':'''预约''',
        'phome_welcomet':'''欢迎来到AllergyCare''',
        'phome_odoctors':'''我们的医生''',
        'phome_qhp':'''合格的医疗保健专业人员''',
        'phome_tmnls':'''推荐''',
        'phome_git':'''保持联系''',
        'phome_ps':'''我们在这里为您提供了我们这方面的最佳照顾。''',
        'phome_newsletter':'''通讯''',
        'phome_follow':'''跟着我们''',
        }
    if lang == 'de': return {
        'phome_welcome':'''Willkommen,''',
        'phome_home':'''Heim''',
        'phome_doctor':'''Ärzte''',
        'phome_clinic':'''Kliniken''',
        'phome_medicines':'''Medikamente''',
        'phome_other':'''Andere''',
        'phome_myprofile':'''Mein Profil''',
        'phome_replies':'''Antworten''',
        'phome_testimonials':'''Referenzen''',
        'phome_logout':'''Ausloggen''',
        'phome_best':'''Beste Pflege Ihrer Allergien''',
        'phome_medicine':'''Medikamente''',
        'phome_appointment':'''Termin''',
        'phome_welcomet':'''Willkommen bei Allergycare''',
        'phome_odoctors':'''Unsere Ärzte''',
        'phome_qhp':'''Qualifizierte Angehörige der Gesundheitsberufe''',
        'phome_tmnls':'''Referenzen''',
        'phome_git':'''In Kontakt kommen''',
        'phome_ps':'''Wir sind hier, um Ihnen die bestmögliche Pflege von unserer Seite zu bieten.''',
        'phome_newsletter':'''Newsletter''',
        'phome_follow':'''Folgen Sie uns''',
        }
    if lang == 'hi': return {
        'phome_welcome':'''स्वागत,''',
        'phome_home':'''घर''',
        'phome_doctor':'''डॉक्टरों''',
        'phome_clinic':'''क्लिनिक''',
        'phome_medicines':'''दवाइयाँ''',
        'phome_other':'''अन्य''',
        'phome_myprofile':'''मेरी प्रोफाइल''',
        'phome_replies':'''जवाब''',
        'phome_testimonials':'''प्रशंसापत्र''',
        'phome_logout':'''लॉग आउट''',
        'phome_best':'''अपनी एलर्जी के लिए सबसे अच्छी देखभाल''',
        'phome_medicine':'''दवाइयाँ''',
        'phome_appointment':'''नियुक्ति''',
        'phome_welcomet':'''एलर्जीकेयर में आपका स्वागत है''',
        'phome_odoctors':'''हमारे डॉक्टर''',
        'phome_qhp':'''योग्य स्वास्थ्य पेशेवर''',
        'phome_tmnls':'''प्रशंसापत्र''',
        'phome_git':'''संपर्क में रहो''',
        'phome_ps':'''हम यहां आपको अपनी तरफ से सर्वोत्तम देखभाल प्रदान कर रहे हैं।''',
        'phome_newsletter':'''समाचार पत्रिका''',
        'phome_follow':'''हमारे पर का पालन करें''',
        }
    if lang == 'pa': return {
        'phome_welcome':'''ਜੀ ਆਇਆਂ ਨੂੰ,''',
        'phome_home':'''ਘਰ''',
        'phome_doctor':'''ਡਾਕਟਰ''',
        'phome_clinic':'''ਕਲੀਨਿਕ''',
        'phome_medicines':'''ਦਵਾਈਆਂ''',
        'phome_other':'''ਹੋਰ''',
        'phome_myprofile':'''ਮੇਰਾ ਪ੍ਰੋਫ਼ਾਈਲ''',
        'phome_replies':'''ਜਵਾਬ''',
        'phome_testimonials':'''ਪ੍ਰਸੰਸਾ ਪੱਤਰ''',
        'phome_logout':'''ਲਾੱਗ ਆਊਟ, ਬਾਹਰ ਆਉਣਾ''',
        'phome_best':'''ਤੁਹਾਡੀ ਐਲਰਜੀ ਦੀ ਸਭ ਤੋਂ ਵਧੀਆ ਦੇਖਭਾਲ''',
        'phome_medicine':'''ਦਵਾਈਆਂ''',
        'phome_appointment':'''ਨਿਯੁਕਤੀ''',
        'phome_welcomet':'''ਐਲਰਜੀਕੇਅਰ ਵਿੱਚ ਤੁਹਾਡਾ ਸਵਾਗਤ ਹੈ''',
        'phome_odoctors':'''ਸਾਡੇ ਡਾਕਟਰ''',
        'phome_qhp':'''ਯੋਗ ਸਿਹਤ ਸੰਭਾਲ ਪੇਸ਼ੇਵਰ''',
        'phome_tmnls':'''ਪ੍ਰਸੰਸਾ ਪੱਤਰ''',
        'phome_git':'''ਸੰਪਰਕ ਵਿੱਚ ਰਹੇ''',
        'phome_ps':'''ਅਸੀਂ ਇੱਥੇ ਹਾਂ ਤੁਹਾਨੂੰ ਸਾਡੇ ਪੱਖ ਤੋਂ ਸਭ ਤੋਂ ਵਧੀਆ ਦੇਖਭਾਲ ਪ੍ਰਦਾਨ ਕਰਦੇ ਹਾਂ.''',
        'phome_newsletter':'''ਨਿ let ਜ਼ਲੈਟਰ''',
        'phome_follow':'''ਸਾਡੇ ਪਿਛੇ ਆਓ''',
        }
    if lang == 'ur': return {
        'phome_welcome':'''خوش آمدید،''',
        'phome_home':'''گھر''',
        'phome_doctor':'''ڈاکٹر''',
        'phome_clinic':'''کلینک''',
        'phome_medicines':'''دوائیاں''',
        'phome_other':'''دیگر''',
        'phome_myprofile':'''میری پروفائل''',
        'phome_replies':'''جوابات''',
        'phome_testimonials':'''تعریف''',
        'phome_logout':'''لاگ آوٹ''',
        'phome_best':'''آپ کی الرجی کی بہترین نگہداشت''',
        'phome_medicine':'''دوائیاں''',
        'phome_appointment':'''تقرری''',
        'phome_welcomet':'''الرجی کیئر میں خوش آمدید''',
        'phome_odoctors':'''ہمارے ڈاکٹر''',
        'phome_qhp':'''اہل صحت کی دیکھ بھال کرنے والے پیشہ ور افراد''',
        'phome_tmnls':'''تعریف''',
        'phome_git':'''رابطے میں رہنا''',
        'phome_ps':'''ہم یہاں موجود ہیں آپ کو اپنی طرف سے بہترین نگہداشت فراہم کرتے ہیں۔''',
        'phome_newsletter':'''نیوز لیٹر''',
        'phome_follow':'''ہمیں فالو کریں''',
        }


def detectLanguage(request):
    languageDetected = supported_languages[0]
    pagePath = request.path
    if pagePath[-1] == '/': pagePath=pagePath[:-1]
    pagePath = pagePath.split('?')[0]
    pagePath = pagePath.split('#')[0]
    lastPath = pagePath.split('/')[-1]
    if lastPath in supported_languages[1:]:
        languageDetected = lastPath
    return languageDetected


def translated(requestOrLang,TranslateVariable):
    if requestOrLang in supported_languages:
        lang=requestOrLang
    else:
        lang = detectLanguage(requestOrLang)
    return translation_dictionary(lang)[TranslateVariable]


def localizeLink(request, link):
    lang=detectLanguage(request)
    if lang == supported_languages[0]: return link
    index1 = link.find('#')
    index2 = link.find('?')
    if index1 == -1 and index2 == -1: smallest_index = len(link)
    elif index1 == -1: smallest_index = index2
    elif index2 == -1: smallest_index = index1
    else: smallest_index = min(index1, index2)
    path = link[:smallest_index]
    if path[-1] == '/': path=path[:-1]
    return path+'/'+lang+link[smallest_index:]


from django.shortcuts import redirect as org_redirect
def redirect(request, to, *args, permanent=False, **kwargs):
    lang=detectLanguage(request)
    if lang in supported_languages[1:]:
        to=to+'_'+lang
    return org_redirect(to, *args, permanent=permanent, **kwargs)


from django.urls import path as org_path
def path(route, view, kwargs=None, name=None):
    if route == '':
        return [org_path('', view, kwargs, name),org_path('ar', view, kwargs, name+'_ar'),org_path('bn', view, kwargs, name+'_bn'),org_path('zh', view, kwargs, name+'_zh'),org_path('de', view, kwargs, name+'_de'),org_path('hi', view, kwargs, name+'_hi'),org_path('pa', view, kwargs, name+'_pa'),org_path('ur', view, kwargs, name+'_ur'),]
    if route[-1] == '/': route=route[:-1]
    return [org_path(route, view, kwargs, name),org_path(route+'/ar', view, kwargs, name+'_ar'),org_path(route+'/bn', view, kwargs, name+'_bn'),org_path(route+'/zh', view, kwargs, name+'_zh'),org_path(route+'/de', view, kwargs, name+'_de'),org_path(route+'/hi', view, kwargs, name+'_hi'),org_path(route+'/pa', view, kwargs, name+'_pa'),org_path(route+'/ur', view, kwargs, name+'_ur'),]


def langRef(path_ref):
    last=path_ref.split('/')[-1]
    if last in supported_languages:
        path_ref=path_ref[:-len(last)-1]
    result='<link rel="alternate" hreflang="en" href="'+addLinks(path_ref,'')+'" />\n'
    result+='<link rel="alternate" hreflang="ar" href="'+addLinks(path_ref,'ar')+'" />\n'
    result+='<link rel="alternate" hreflang="bn" href="'+addLinks(path_ref,'bn')+'" />\n'
    result+='<link rel="alternate" hreflang="zh" href="'+addLinks(path_ref,'zh')+'" />\n'
    result+='<link rel="alternate" hreflang="de" href="'+addLinks(path_ref,'de')+'" />\n'
    result+='<link rel="alternate" hreflang="hi" href="'+addLinks(path_ref,'hi')+'" />\n'
    result+='<link rel="alternate" hreflang="pa" href="'+addLinks(path_ref,'pa')+'" />\n'
    result+='<link rel="alternate" hreflang="ur" href="'+addLinks(path_ref,'ur')+'" />\n'
    result+='<link rel="alternate" hreflang="x-default" href="'+addLinks(path_ref,'')+'" />\n'
    return result


from django.urls import get_resolver
def translatedLinks(lang):
    names=[]
    for i in get_resolver().url_patterns:
        if hasattr(i, 'name'):
            if i.name:
                names.append(i.name)
    result = {}
    if lang == supported_languages[0]:
        for i in names:
            if i[-3:] not in ['_ar', '_bn', '_zh', '_de', '_hi', '_pa', '_ur'] and names.count(i+'_ar'):
                result.update({i:i})
        return result
    for i in names:
        if names.count(i+'_'+lang):
            result.update({i:i+'_'+lang})
    return result


def languageMenu(request, lang):
    path = request.path
    remainder = request.get_full_path()[len(path):]
    selected = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    selected[supported_languages.index(lang)]=' selected '
    if supported_languages.index(lang):
        path=path[:-3]
    result = '<select id="languageMenu" onchange="window.location = this.value;">'
    if path == '/': path = ''
    if path =='':
        result += '<option'+selected[0]+'value="/'+remainder+'">English (English)</option>'
    else:
        result += '<option'+selected[0]+'value="' + path + remainder +'">English (English)</option>'
    result += '<option'+selected[1]+'value="' + path +'/ar'+remainder+'">Arabic (العربية)</option>'
    result += '<option'+selected[2]+'value="' + path +'/bn'+remainder+'">Bengali (বাংলা)</option>'
    result += '<option'+selected[3]+'value="' + path +'/zh'+remainder+'">Chinese (中文)</option>'
    result += '<option'+selected[4]+'value="' + path +'/de'+remainder+'">German (Deutsch)</option>'
    result += '<option'+selected[5]+'value="' + path +'/hi'+remainder+'">Hindi (हिन्दी)</option>'
    result += '<option'+selected[6]+'value="' + path +'/pa'+remainder+'">Punjabi (ਪੰਜਾਬੀ)</option>'
    result += '<option'+selected[7]+'value="' + path +'/ur'+remainder+'">Urdu (اردو)</option>'
    result += '</select>'
    return result


from django.shortcuts import render as org_render
def render(request, template_name, context=None, *args, **kwargs):
    lang=detectLanguage(request)
    if context == None:
        context={}
    return org_render(request, template_name, {**context,
                                                **translation_dictionary(lang),
                                                'lang':lang,
                                                'languageReferences':langRef(request.build_absolute_uri()),
                                                'languageMenu':languageMenu(request, lang),
                                                'candyLink':translatedLinks(lang),
                                                }, *args, **kwargs)


def addLinks(*args):
    result=''
    for i in args:
        if result and result[-1]=='/':result=result[:-1]
        if i and i[-1]=='/':i=i[:-1]
        if i and i[0]=='/':i=i[1:]
        if result and i: result+='/'
        result+=i
    return result


def provideSitemap(request, add_pages=[], remove_pages=[], remove_paths=[]):
    from django.http import HttpResponse
    result='<?xml version="1.0" encoding="UTF-8"?>'+'\n'
    result+='<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+'\n'
    domain= request.build_absolute_uri()
    domain=domain.split('/')[0]+'//'+domain.split('/')[2]+'/'
    paths = []
    for i in get_resolver().url_patterns:
        if str(type(i))=="<class 'django.urls.resolvers.URLPattern'>":
            try:
                route=i.pattern._route
                route=route.split('<')[0]
                if not route == 'sitemap.xml':
                    if 'robots.txt' not in route:
                        paths.append(addLinks(domain,route))
            except: pass
    paths+=add_pages
    paths=list(dict.fromkeys(paths))
    for route in paths:
        removed_path = False
        for removal in remove_paths:
            if route[:len(removal)] == removal: removed_path = True
        if not removed_path and route not in remove_pages:
            result+='<url>'+'\n'
            result+='<loc>'+route+'</loc>'+'\n'
            result+='</url>'+'\n'
    result+='</urlset>'
    result= result.encode('utf-8')
    return HttpResponse(result, content_type='application/xml; charset=utf-8')


def sitemap(add_pages=[], remove_pages=[], remove_paths=[]):
    return [org_path('sitemap.xml', provideSitemap,{'add_pages' :add_pages,'remove_pages': remove_pages, 'remove_paths': remove_paths})]


