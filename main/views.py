from multiprocessing import context
from pyexpat import model
from re import template
from django.shortcuts import render
from django.contrib import messages
from .models import Portfolio, Skill, UserProfile, ContactProfile, Testimonial, Blog, Media, Certificate
from django.views import generic
from .forms import ContactForm


class IndexView(generic.TemplateView):
    template_name = 'main/index.html'
    context_object_name = 'skills'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        
        testimonials=Testimonial.objects.filter(is_active=True)
        certificates=Certificate.objects.filter(is_active=True)
        blogs=Blog.objects.filter(is_active=True)
        portfolio=Portfolio.objects.filter(is_active=True)
        
        # context['testimonials']=testimonials
        context['certificates']=certificates
        context['blogs']=blogs
        context['portfolio']=portfolio
        return context
    def get_queryset(self):
        return Skill.objects.all()
    
class ContactView(generic.FormView):
    template_name = 'main/contact.html'
    form_class = ContactForm
    success_url="/"
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your message has been sent!')
        return super().form_valid(form)


class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = 'main/portfolio_detail.html'
    context_object_name = 'portfolio'
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)
    
class PortfolioDetailView(generic.DeleteView):
    model = Portfolio
    template_name = 'main/portfolio_detail.html'
    
class BlogView(generic.ListView):
    model=Blog
    template_name='main/blog.html'
    paginate_by=10
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DeleteView):
    model=Blog
    template_name='main/blog_detail.html'
     