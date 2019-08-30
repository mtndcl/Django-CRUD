from django.shortcuts import render,get_object_or_404

from django.http import HttpResponseRedirect, HttpResponse


from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.models import User
from django.urls import reverse ,reverse_lazy
from .models  import  Profile ,Post
from django.contrib.auth.decorators import login_required

from .forms import registerform ,UserUpdateForm, ProfileUpdateForm ,Postform


from django.contrib import messages



from django.utils.decorators import method_decorator

from django.http import Http404
from django.views.generic.edit import DeleteView
@login_required
def updateprofilepage(request):

	if request.method == 'POST':



		print('gettıng new ınformatıon ********************************')
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST,
								   request.FILES,
								   instance=request.user.profile)
		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			
			return HttpResponseRedirect(reverse('profile-page'))

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	

	users=User.objects.all()

	context={
		
		'u_form': u_form,
		'p_form': p_form,
		
	}

	return render(request,'User/updateprofile.html',context)

@login_required
def logoutpage(request):

	print('logout page come down ---------------------------------')
	logout(request)
	
	return render(request,'User/logout.html')

@login_required
def profilepage(request):

	if request.method == 'POST':
		form = Postform(request.POST,request.FILES)

		if len(form['posttext'].value().strip())>0:

			print("we get your posy request ************************")
			if form.is_valid():
				instance=form.save(commit=False)
				instance.user=request.user
				instance.save()
				print("dont worruyy  we saved ************************")
				return HttpResponseRedirect(reverse('profile-page'))
		else:
			messages.warning(request, 'You cant share empty post')
			form = Postform()
	else:
		print('----------------------------->>>>>>>>>>>>Fill the form')
		form = Postform()

	posts=Post.objects.order_by('-date')
	


	context={'form':form,
				'posts':posts}
	return render(request,'User/home.html',context)
def homepage(request):
	

	print('home page work here ---------------------------------')
	return render(request,'User/base.html')
def loginpage(request):

	print('login page work here ---------------------------------')
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username, password=password)
		if user is not None:
			
			login(request, user)
			
				
			return HttpResponseRedirect(reverse('profile-page'))
			
		else:
			messages.warning(request, 'Username and Password Mismatch')
			return HttpResponseRedirect(reverse('login-page'))
	else:
		return render(request, 'User/login.html', {})

def registerpage(request):

	print('register page work here ---------------------------------')

	if request.method == 'POST':
		form = registerform(request.POST)

		if form.is_valid():
			form.save()
			username=request.POST.get('username')
			print('----------------------------->>>>>>>>>>>> User Saved {} ' ,request.POST.get('username'))
			messages.success(request, 'Good Job {0} .You can login now'.format(username) )
			return HttpResponseRedirect(reverse('login-page'))
	else:
		print('----------------------------->>>>>>>>>>>>Fill the form')
		form = registerform()
	return render(request, 'User/register.html', {'form': form})

def confirmdeletepage(request,  slug):

	post = Post.objects.get(id=slug)
	#uid.delete()

	if request.method == 'POST':
		print()
		post.delete()
		messages.success(request, 'Your mesages deleted successfuly' )
		return HttpResponseRedirect(reverse('profile-page'))

	return render(request, 'User/delete.html',{'post':post})


def displaymessages(request):
	
	storage = messages.get_messages(request)
	storage.used = True

	return HttpResponseRedirect(reverse('profile-page'))

def userprofilepage(request, slug):
	

	print('the user is  ===  >>>  ',slug)
	user = User.objects.get(username=slug)
	posts=Post.objects.filter(user=user)

	print('posrrttt  --->>>>>>>  ' ,posts)
	return render(request, 'User/userprofile.html',{'spying_user':user
		,'posts':posts})

def searchpage(request):

	data=request.POST.get('data')
	print('Serach ................................................................................',data)
	result=User.objects.filter(first_name__contains=data)	
	return render(request, 'User/search.html',{'users':result})

def addfriendpage(request, slug):
	
	user=User.objects.get(username=slug)

	messages.success(request, 'You are Friend with {0} {1}'.format(user.first_name,user.last_name) )

	return HttpResponseRedirect(reverse('profile-page'))
	  