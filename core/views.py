from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.template.loader import get_template
from django.contrib import messages
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from .models import *

# Create your views here.
# def fullsite(request):
# 	context_general = {}
# 	return render(request, 'core/index.html', context_general)

class Index(TemplateView):
	template_name = "core/home.html"

	def get_context_data(self, **kwargs):
		context = super(Index, self).get_context_data(**kwargs)
		context.update({
			'slide_itens': Fullwidth_slider_item.objects.all(),
		})
		return context

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
