from django.shortcuts import render,redirect
from .forms import UserCreationForm,ProfileForm,chat,replyform,AddCourses,AddLecture
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from .models import newuser,course,problems,reply,lectures
from django.forms import modelformset_factory
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.mail import send_mail
from django.core.mail import EmailMessage
# Create your views here.
def home(request):
	return render(request,'social/front.html')

def index(request):
	if request.method=='POST':
		form=UserCreationForm(request.POST)
		if form.is_valid():
			user=form.save(commit=False)
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()
			user=authenticate(username=username,password=password)
			login(request,user)
			return redirect('index')
	else:
		form=UserCreationForm()
		context={'form':form}
		return render(request,'registration/register.html',context)

class courses(generic.ListView):
	model=course
	template_name='social/courses.html'
	def get_queryset(self):
		return course.objects.all()

def show(request):
	god=[]
	obj=newuser.objects.filter(user=request.user).get()
	pro=course.objects.all()
	for pie in pro:
		pink={'teacher':pie.teacher,'name':pie.name,'price':pie.price,'logo':pie.logo,'is_completed':pie.is_completed,
		'description':pie.description,'id':pie.id}
		god.append(pink)
	print(obj.mentor)
	context={'god':god,'hi':obj}
	return render(request,'social/courses.html',context)
def lecture(request,pk):
	pro=course.objects.filter(pk=pk)
	y=lectures.objects.filter(course__exact=pro[0])
	con=[]
	for t in y:
		pink={'video':t.video,'name':t.name,'mentor':t.course.user.username}
		con.append(pink)
	context={'computer':con}
	print(con)
	return render(request,'social/lecture.html',context)
@login_required
def subscribe(request,pk):
	if request.user.is_authenticated:
		cup=course.objects.get(pk=pk)
		user=request.user
		pro=newuser.objects.filter(user=user)
		pro[0].subscribed.add(cup)
		pro[0].save()
		return redirect('courses')
@login_required
def profile(request):
	if request.method=='POST':
		form=UserChangeForm(request.POST,user=user)
		if form.is_valid():
			profile=form.save(commit=False)
			profile.user=request.user
			profile.save()
	user=request.user
	pro=newuser.objects.filter(user=user)
	if not pro:
		pro=newuser(user=user,photo="wallpaper2you_525070.jpg",rating=1)
		pro.save()
		context={'photo':pro.photo.url,'rating':pro.rating}
		return render(request,'social/profile.html',context)
	if pro[0].photo:
		context={'photo':pro[0].photo.url,'rating':pro[0].rating}
	return render(request,'social/profile.html',context)
@login_required
def update(request):
	user=request.user
	pro=newuser.objects.filter(user__exact=user)
	#language=modelformset_factory(newuser,fields=('photo',))
	language=inlineformset_factory(User,newuser,fields=('photo',))
	form=language(request.POST,instance=pro)
	context={'form':form,'rating':pro[0].rating}
	return render(request,'registration/register.html',context)


@login_required
def profile_change(request):
	if request.method=='POST':
		form=ProfileForm(request.POST,request.FILES)
		if form.is_valid():
			form=form.save(commit=False)
			user=request.user
			pro=newuser.objects.filter(user__exact=user).get()
			form.user=user
			pro.photo=form.photo
			pro.save()
			print(pro.photo.url)
			return redirect('profile')
	else:
		form=ProfileForm()
		context={'form':form}
		return render(request,'social/profile_change.html',context)

@login_required
def ChangePassword(request):
	if request.method=='POST':
		form=PasswordChangeForm(user=request.user,data=request.POST)
		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('profile')
		else:
			return redirect('ChangePassword')
	else:
		form=PasswordChangeForm(user=request.user)
		context={'form':form}
		return render(request,'social/pass.html',context)
@login_required
def chatroom(request):
	if request.method=='POST':
		form=chat(request.POST)
		if form.is_valid():
			user=request.user
			prob=form.cleaned_data['prob']
			pro=problems(prob=prob,user=user)
			pro.save()
			return redirect('chat')
	else:
		prob=problems.objects.all()
		pink=[]
		for pie in prob:
			repel=replyform()
			ji=problems.objects.filter(pk=pie.id)
			hi=ji[0].reply.all()
			god=[]
			for up in hi:
				to={'reply':up.answer}
				god.append(to)
			red={'problems':pie.prob,'reply':repel,'pro':pie,'answers':god}
			pink.append(red)
		form=chat()
		print(pink)
		context={'form':form,'pink':pink}
		return render(request,'social/chat.html',context)
@login_required
def reply_fun(request,pk):	
	if request.method == 'POST':
		form=replyform(request.POST)
		if form.is_valid():
			ques=problems.objects.filter(pk=pk).get()
			user=request.user
			answer=form.cleaned_data['answer']
			pro=reply(user=user,answer=answer)
			pro.save()
			ques.reply.add(pro)
			print(pro)
			ques.save()
			return redirect('chat')
	else:
		return redirect('chat')


def adding(request):
	if request.method=='POST':
		form=AddCourses(request.POST,request.FILES)
		if form.is_valid():
			teacher=form.cleaned_data['teacher']
			price=form.cleaned_data['price']
			name=form.cleaned_data['name']
			logo=form.cleaned_data['logo']
			description=form.cleaned_data['description']
			user=request.user
			hi=course(teacher=teacher,price=price,name=name,logo=logo,description=description,user=user)
			hi.save()
			return redirect('courses')
	else:
		form=AddCourses()
		context={'form':form}
		return render(request,'social/list.html',context)
def add_lecture(request,pk):
	if request.method=='POST':
		form=AddLecture(request.POST,request.FILES)
		cop=course.objects.filter(pk=pk).get()
		if form.is_valid():
			name=form.cleaned_data['name']
			video=form.cleaned_data['video']
			ki=lectures(name=name,video=video,course=cop)
			ki.save()
			return redirect('courses')
	else:
		form=AddLecture()
		object_list=course.objects.all()
		hell=[]
		for ri in object_list:
			ty={'id':ri.id}
			hell.append(ty)
		context={'form':form,'object_list':hell,'pk':pk}
		return render(request,'social/list.html',context)

def send(request):
	email = EmailMessage('title', 'body', to=[''])
	email.send()
	#send_mail=('hello','just checking','singhjishan2@gmail.com',['noposo@yourweb.email',],fail_silently=False)
	return redirect('index')

def about(request):
	return render(request,'social/about.html')
