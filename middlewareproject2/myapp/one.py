from django.http import HttpResponse
class SimpleMiddleWare:
	def __init__(self,ob):
		self.get_response=ob
		#initialized get_response with request instace
	def __call__(self,request):
		print("Processing the request")
		response=self.get_response(request)
		print(response)
		print("Post Processing the response")
		return response
	def process_exception(self,request,exception):
		return HttpResponse("<h1>Sorry...Server is under maintainances</h1>")