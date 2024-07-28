from django.core.serializers import serialize
import json
from django.http import HttpResponse
class HttpResponseMixin(object):
	def render_to_http_response(self,json_data,status=200):
		return
		HttpResponse(json_data,content_type='application/json',status=status)
		
class SerializeMixin(object):
	def fun(self,qs):
		json_data=serialize('json',qs)
		p_dict=json.loads(json_data)
		result=[]

		for ob in p_dict:
			emp_data=ob['fields']
			result.append(emp_data)
			json_data=json.dumps(result)
			return json_data