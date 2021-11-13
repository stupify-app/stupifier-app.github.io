from functools import wraps
from flask import Flask, render_template, redirect, request, session
import random
from django.http import JsonResponse

##session.get >>>> gets from current session >>> user_id >>> gets id from current session/user

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is None:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function



def dictionary(dictionary):
    #create an empty dictionary
    d = {}

    key = 0

    #open dictionary file and store it in 'dic'
    with open(dictionary,encoding="utf8", errors='ignore') as dic:
        #read every line and give it a number
        for line in dic:
            ##STRIPING \N >>>>>>https://stackoverflow.com/questions/275018/how-can-i-remove-a-trailing-newline
            value = line.replace('\n', '')
            key += 1
            d[key] = value

    #PYTHON'S RANDOM MODULE >>>>> https://www.w3schools.com/python/module_random.asp

    #select a random number in the range of the dictionary (and store it in a variable)
    rand = random.randrange(1, len(d) + 1)

    #get the word with that number (and store it in a variable)
    word = d[rand]

    return word #Javascript object notation >>> dictionary for javascript
