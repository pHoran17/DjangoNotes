from django.shortcuts import render

# Create your views here.
def example_view(request):
    # will refer to my_app/templates/my_app/example.html
    return render(request, 'my_app/example.html')
#Tags used to iterate thrpugh lists
def variable_view(request):
    my_var = {'first_name': 'Rosalind', 'last_name': 'Franklin', 
                'some_list':[1,2,3], 'some_dict': {'inside_key': 'inside_value'}, 'user_logged_in':False}
    return render(request, 'my_app/variable.html', context=my_var)
