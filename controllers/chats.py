from pylons import request, response, session, tmpl_context as c, url
from pylons.controllers.util import abort, redirect
from hw.lib.base import BaseController, render, Session
from hw.lib.funcs import *
from hw.model.chanel import Chanel
from hw.model.person import Person
from hw.model.message import Message
import json, time
class ChatsController(BaseController):
    def __before__(self):
        c.chanel=''
        c.messages=[]
        c.user={}
        c.search={}
        self.chanel_q=Session.query(Chanel)
        self.person_q=Session.query(Person)
        self.message_q=Session.query(Message)
    @login_required
    def main(self):
        c.title='Main page'
        c.name=session['name']
        chanels=self.chanel_q.filter_by(owner=c.name).all()
        c.chanels=chanels
        return render('cmain.mako')
    @login_required
    def create_chat(self):
        USER_CHATS_LIMIT=10
        if request.method=='GET':
            return ''
        chat_name=request.POST.get('chat_name')
        result_query=self.chanel_q.filter_by(name=chat_name).first()
        if result_query:
            return 'This chanel name exists'
        owner_email=session.get('email')
        owner=self.person_q.filter_by(email=owner_email).first()
        if not owner:
            redirect('/auth/signin')
        chanels=self.chanel_q.filter_by(owner=owner.name).all()
        if len(chanels)>USER_CHATS_LIMIT:
            return 'You can`t create a chat'
        chanel=Chanel(name=chat_name, owner=owner.name, created='test')
        Session.add(chanel)
        Session.commit()
        redirect('/chanel/'+chat_name)
    def chat_route(self, id):
        autorize()
        chanel=self.chanel_q.filter_by(name=id).first()
        if not chanel:
            return 'This chanel does not exist'
        user_id=session.get('person_id')
        if user_id!=None:
            user=self.person_q.filter_by(id=user_id).first()
            user.chanel_id=chanel.id
            Session.commit()
            session['chanel']={'id':chanel.id, 'name':chanel.name}
            session.save()
            c.user['name']=session.get('name')
            chanels=self.chanel_q.filter_by(owner=c.user['name']).all()
            c.user['chanels']=chanels
        c.title='#'+id
        c.chanel=id
        c.timestamp=int(time.time())
        return render('croute.mako')
    @login_required
    def add_message(self):
        if request.method=='GET':
            return ''
        person_id=session.get('person_id')
        person_name=session.get('name')
        chanel_name=request.POST.get('chanel')
        chanel=self.chanel_q.filter_by(name=chanel_name).first()
        body=request.POST.get('body')
        to=request.POST.get('to')
        message=Message(body=body, date=get_date(), timestamp=int(time.time()), to=to, type='public', person_id=person_id, person_name=person_name,chanel_id=chanel.id)
        Session.add(message)
        Session.commit()
        c.body=body
        c.name=person_name
        c.date=get_date()
#        return render('ajax_add_message.mako')
        redirect('/chanel/'+chanel_name)
    def display_messages(self, vars):
        id=session['chanel']['id']
        chanel=self.chanel_q.filter_by(id=id).first()
        users=[x.name for x in chanel.persons]
        c.messages=self.message_q.filter(Message.chanel_id==chanel.id, Message.timestamp>int(vars)).all()
        length=len(c.messages)        
        if length>20:
            c.messages=c.messages[-length:]
        data={}
        data['messages']=render('messages_json.mako')
        data['users']=users
        return json.dumps(data)
    @login_required
    def search(self):
        c.title="Search"
        if request.method=="GET":
            return render('search.mako')
        text=request.POST.get('query')
        if text:
            chanels=self.chanel_q.filter(Chanel.name.like(text)).all()
            c.search['results']=chanels
            return render('search.mako')
    def preview(self):
        return document_preview('http://docs.makotemplates.org/en/latest/inheritance.html')
    def chat_activity(self):
#Calculates a chat activity. Result of this function may be used to decrease  messages reload time interval
        DEFAULT_ACTIVITY=2
        id=session['chanel']['id']
        timestamp=int(time.time())-60
        messages=len(self.message_q.filter(Message.chanel_id==id, Message.timestamp>timestamp).all())
        chanel=self.chanel_q.filter_by(id=id).first()
        users_online=len(chanel.persons)
        activity=float(messages)/float(users_online)
        if activity<=DEFAULT_ACTIVITY:
            return 0
        result=activity-DEFAULT_ACTIVITY
        if result>1:
            result=1
        return result