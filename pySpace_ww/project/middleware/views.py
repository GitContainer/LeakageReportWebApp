from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from middleware.models import User, Message, Choice
from django import forms
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
import datetime
from middleware.hello import Hello
from django.core.urlresolvers import reverse

# for test the app register
def reg(request):
    return render_to_response('regforapp.html')

# for test the app login
def logg(request):
    return render_to_response('loginforapp.html')

# for test the app login
def content(request):
    return render_to_response('contentforapp.html')

# for the app use
def regforapp(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username__exact=username)
    if user:
        return HttpResponse(status='300')
    else:
        newuser = User()
        newuser.username = username
        newuser.password = password
        newuser.save()
        return HttpResponse(status='200')

#for the app use
def loginforapp(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username__exact=username, password__exact=password)
    if user:
        request.session['username'] = username
        return HttpResponse(status="200")
    else:
        return HttpResponse(status="300")

#for the app use
def contentforapp(request):
    username = request.session.get('username', 'anybody')
    content = request.POST['content']
    location = request.POST['location']
    user = User.objects.get(username__exact=username)
    message = Message()
    message.user = user
    message.content = content
    message.location = location
    message.pub_date = datetime.datetime.now()
    message.save()
    return HttpResponse(status='200')

#for the web use
class UserForm(forms.Form):
    username = forms.CharField(label='username:',max_length=100,)
    password = forms.CharField(label='password:',widget=forms.PasswordInput())

class MessageForm(forms.Form):
    content = forms.CharField(label='content',max_length=100,)
    location = forms.CharField(label='location',max_length=30,)

class PosForm(forms.Form):
    location = forms.CharField(label='location',max_length=30,)

# def login(request):
#     if request.method == 'POST':
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             #get username and password
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #compare with database
#             user = User.objects.filter(username__exact = username,password__exact = password)
#             if user:
#                 message_list = Message.objects.filter(user = user)
#                 message = message_list.latest('id')
#                 recent_post_check = message.was_published_recently()
#                 request.session['username'] = username
#                 if recent_post_check:
#                     # return HttpResponse("recent_post_check is true")
#                     return HttpResponseRedirect('/middleware/index/', {'recent_post_check':recent_post_check})
#                 else:
#                     # return HttpResponseRedirect('/middleware/index/')
#                     return HttpResponse("recent_post_check is false")
#             else:
#                 return HttpResponseRedirect('/middleware/login/')
#     else:
#         uf = UserForm()
#     return render_to_response('login.html',{'uf':uf})
def login(request):
    return render_to_response('login.html')

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username__exact=username, password__exact=password)
    if user:
        message_list = Message.objects.filter(user=user)
        request.session['username'] = username
        if message_list:
            message = message_list.latest('id')
            recent_post_check = message.was_published_recently()
            return render_to_response('index.html', {'recent_post_check':recent_post_check, 'username':username,})
        else:
            return render_to_response('index.html', {'recent_post_check':False, 'username':username,})
    else:
        return HttpResponseRedirect('/middleware/login/')

# def index(request):
#     username = request.session.get('username', 'anybody')
#     if request.method == "POST":
#         mf = MessageForm(request.POST)
#         if mf.is_valid():
#             content = mf.cleaned_data['content']
#             location = mf.cleaned_data['location']
#             # username = request.session.get('username', 'anybody')
#             user = User.objects.get(username__exact=username)
#             message = Message()
#             message.user = user
#             message.content = content
#             message.location = location
#             message.pub_date = datetime.datetime.now()
#             message.save()
#
#
#             h = Hello()
#             test2 = h.helloworld(message.content)
#             return HttpResponse(test2)
#     else:
#         mf = MessageForm()
#         # username = request.session.get('username', 'anybody')
#         return render_to_response('index.html' ,{'mf':mf,'username':username})

def index(request):
    username = request.session.get('username', 'anybody')
    return render_to_response('index.html',{'username':username})

def message_update(request):
    username = request.session.get('username', 'anybody')
    content = request.POST['content']
    location = request.POST['location']
    user = User.objects.get(username__exact=username)
    message = Message()
    message.user = user
    message.content = content
    message.location = location
    message.pub_date = datetime.datetime.now()
    h = Hello()
    test2 = h.helloworld(message.content)
    message.status = test2
    message.save()
    choice1 = Choice()
    choice1.choice_text="True"
    choice1.message = message
    choice1.save()
    choice2 = Choice()
    choice2.message = message
    choice2.choice_text="False"
    choice2.save()
    return HttpResponseRedirect('/middleware/index/')

# def register(request):
#     if request.method == "POST":
#         uf = UserForm(request.POST)
#         if uf.is_valid():
#             #get form info
#             username = uf.cleaned_data['username']
#             password = uf.cleaned_data['password']
#             #write into database gai
#             user = User()
#             user.username = username
#             user.password = password
#             user.save()
#             #return and success
#             return HttpResponseRedirect('/middleware/login/')
#     else:
#         uf = UserForm()
#     return render_to_response('register.html',{'uf':uf})

def register(request):
    return render_to_response('register.html')

def register_update(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.filter(username__exact=username)
    if user:
        repeat_username = True
        return render_to_response('register.html',{'repeat_username':repeat_username})
    else:
        newuser = User()
        newuser.username = username
        newuser.password = password
        newuser.save()
        return HttpResponseRedirect('/middleware/login/')

def logout(request):
    del request.session['username']
    return HttpResponseRedirect('/middleware/login/')

# def posfilter(request):
#     if request.method == "POST":
#         pf = PosForm(request.POST)
#         if pf.is_valid():
#             # get form info
#             loc = pf.cleaned_data['location']
#             #
#             filtered_messages = Message.objects.filter(location = loc)
#             #
#             return render_to_response('result.html', {'filtered_messages': filtered_messages})
#     else:
#         pf = PosForm()
#     return render_to_response('filter.html', {'pf': pf})

def history_data(request):
    return render_to_response('filter.html')

def data_filter(request):
    location = request.POST['location']
    filtered_messages = Message.objects.filter(location = location)
    return render_to_response('result.html', {'filtered_messages': filtered_messages})


#for test
def hello(request):
    h = Hello()
    test = "chen"
    test2 = h.helloworld(test)
    return HttpResponse(test2)
    # print request

def vote(request, message_id):
    p = get_object_or_404(Message, pk = message_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request,'detail.html',{
         'message':p,
         'error_message':"You didn't select a choice.",
        })
    else:
        selected_choice.votes+=1
        selected_choice.save()
        message = get_object_or_404(Message, pk=message_id)
        return render_to_response('voteresults.html', {'message': message})
        # return HttpResponseRedirect(reverse('voteresults',args=(p.id)))

def voteresults(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'voteresults.html', {'message': message})

def detail(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    return render(request, 'detail.html', {'message': message})