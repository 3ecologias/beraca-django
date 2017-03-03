from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from .models import *
from .forms import *
import operator
from django.db.models import Q

# Create your views here.
# def fullsite(request):
# 	context_general = {}
# 	return render(request, 'core/index.html', context_general)

class Index(FormView):
	template_name = "core/home.html"
	form_class = ContactUs
	success_url = '/'

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context.update({
			'slide_itens': Fullwidth_slider_item.objects.all(),
			'posts': BlogPost.objects.all().order_by('-date')[:3],
		})
		return context

	def form_valid(self, form):
		form.send_email()

		return super(Index, self).form_valid(form)

class AboutView(TemplateView):
    template_name = "core/about.html"

class CasesView(TemplateView):
	template_name = "core/cases.html"

	def get_context_data(self, **kwargs):
		context = super(CasesView, self).get_context_data(**kwargs)
		context.update({
			'cases': PortfolioItem.objects.all(),
		})
		return context

class CaseDetailView(DetailView):
	template_name = "core/detail_templates/case_detail.html"
	model = PortfolioItem


class BlogListView(ListView):
	template_name = "core/list_templates/blog.html"
	model = BlogPost
	paginate_by = 10

	def get_queryset(self):
		queryset = super(BlogListView, self).get_queryset()
		query = self.request.GET.get('search')
		if query:
			query_list = query.split('search')
			queryset = queryset.filter(
                reduce(operator.and_,
                       (Q(title__icontains=word) for word in query_list))|
                reduce(operator.and_,
                       (Q(sub_title__icontains=word) for word in query_list))|
                reduce(operator.and_,
                       (Q(content__icontains=word) for word in query_list))
            )
		return queryset

class BlogDetailView(DetailView):
	template_name = "core/detail_templates/blog_detail.html"
	model = BlogPost
