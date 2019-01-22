from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    'my_list':[
     {
     'restaurant_name':'Dragon',
     'food_type':'chinese'
     },

    {
    'restaurant_name':'Wicked',
    'food_type':'Spells'
    },

    {
    'restaurant_name':'Braino',
    'food_type':'Brains'
    }]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    'my_object':{
    'restaurant_name': 'Wicked',
    'food_type': 'Spells',
    'manager': 'marwah' 

    }

    }
    return render(request, 'detail.html', context)
