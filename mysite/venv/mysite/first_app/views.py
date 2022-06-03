from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


# Create your views here.
# def simple_view(request):
#     return HttpResponse("Simple View")

# articles ={
#     'sports': 'Sports Page',
#     'finance': 'Finance Page',
#     'politics': 'Politics Page',
# }

#Try Except is djangos equivalent of try catch
# def news_view(request,topic):
#     try:
#         result = articles[topic]
#         return HttpResponse(result)
#     except:
#         # result = 'No page for that topic!'
#         # return HttpResponseNotFound(result)
#         raise Http404("404 Generic Error")
    
    

# def add_view(request, num1, num2):
#     result = num1 + num2
#     return HttpResponse(str(result))

# def finance_view(request):
#     return HttpResponse(articles['finance'])


#domain.com/first_app/0
#Uses array of keys to provide redirects to specified pages
# def num_page_view(request, num_page):
#     topics_list = list(articles.keys()) #['sports', 'finance', 'politics']
#     topic = topics_list[num_page]
#     #Reverse function included in responseDirect to show general usage
#     return HttpResponseRedirect(reverse('topic-page', args =[topic]))
#     #return HttpResponseRedirect(topic)

#Linking view to template
def simple_view(request):
    return render(request, 'first_app/example.html') #.html