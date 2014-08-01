import logging
from pylons.decorators import validate
from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from hw.model.forms import EmailForm, SignInForm
from hw.lib.funcs import *
from hw.model.person import Person
from hw.lib.base import BaseController, render, Session

log = logging.getLogger(__name__)

class AuthController(BaseController):
    def __before__(self):
        self.person_q=Session.query(Person)
    def index(self):
        return render('/new_action.mako')
    @validate(schema=EmailForm(), form='index')
    def signup(self):
        if request.method=='GET':
            redirect('/')
        email=self.form_result.get('email')
        name=self.form_result.get('name')
        password=self.form_result.get('password')
        result=self.person_q.filter_by(name=name).first()
        if result:
            return 'This nickname is used by another one'
        result2=self.person_q.filter_by(email=email).first()
        if result2:
            return 'This email registered yet. Do u forget your password?'
        pers=Person(name=name, email=email, password=md5(password))
        Session.add(pers)
        Session.commit()
        response.set_cookie('email', email)
        response.set_cookie('password', md5(password))
        redirect('/chanel/main')
    @validate(schema=SignInForm(), form='signin')
    def signin(self):
        if request.method=='GET':
            return render('sign_in.mako')
        email=self.form_result.get('email')
        password=self.form_result.get('password')
        pers=self.person_q.filter_by(email=email, password=md5(password)).first()
        if pers:
            response.set_cookie('email', email)
            response.set_cookie('password', md5(password))
            redirect('/chanel/main')
        return 'Invalid user name and/or password %s'%dir
    def logout(self):
        if session.get('email'):
            session.clear()
            session.save()
            if request.cookies.get('email'):
                response.delete_cookie('email')
                response.delete_cookie('password')
        redirect('/')