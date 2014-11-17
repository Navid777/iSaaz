__author__ = 'Aiida'
from InstrumentSeller.forms import *

def include_login_form(request):
    loginform = login_form()
    regform = register_form()
    return {'login_form': loginform, 'reg_form' : regform}