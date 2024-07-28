from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.generic import View
from myapp.mixins import HttpResponseMixin
class CBV(View,HttpResponseMixin):
	def get(self,*args,**kwargs):
		json_data=json.dumps({'msg':'get method'})
		return self.render_to_http_response(json_data)