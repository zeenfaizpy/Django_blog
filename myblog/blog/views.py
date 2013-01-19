from django.http import HttpResponseRedirect,HttpResponse
from django.core.context_processors import csrf
from django.core.urlresolvers import reverse
from blog.models import Post,Comment,CommentForm
from django.shortcuts import render_to_response, get_object_or_404

def home(request):
	posts = Post.objects.all()
	comments = Comment.objects.all()
	return render_to_response('index.html', { 'posts': posts , 'comments':comments })

def allpost(request):
	return HttpResponse("This is my allpost Page")

def singlepost(request,pk):
	post = Post.objects.get(pk=int(pk))
	comment = Comment.objects.filter(post=post)
	c = dict(post=post,comments=comment,form=CommentForm())
	c.update(csrf(request))
	return render_to_response('post.html',c)

def add_comment(request,pk):
	if request.method == "POST" and request.POST:
		p = request.POST
		comment = Comment(post=Post.objects.get(pk=pk))
		f = CommentForm(p)
		if f.is_valid():
			fi = CommentForm(p,instance=comment)
			fi.save()
			return HttpResponseRedirect(reverse("blog.views.singlepost",args=[pk]))
		else:
			return HttpResponse("Validation Error")
	else:
		return HttpResponse("Contact Admin.No Data from FORM")