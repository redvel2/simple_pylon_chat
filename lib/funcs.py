from pylons.templating import render_mako
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pylons import tmpl_context as c, request, response, session
import smtplib, hashlib, time, datetime, urllib2, json
from hw.model.person import Person
from hw.lib.base import Session
from pylons.controllers.util import redirect

def send_html_email(subject, to, text,template, link=''):
    test_email='email'
    password='password'
    mail_server='smtp.someserver.com'
    message=MIMEMultipart('alternative')
    message['Subject']=subject
    message['From']=test_email
    message['To']=to
    c.link=link
    body=render_mako(template)
    part1=MIMEText(text, 'plain')
    part2=MIMEText(body, 'html')
    message.attach(part1)
    message.attach(part2)
    s=smtplib.SMTP_SSL(mail_server)
    s.ehlo()
    s.login(test_email, password)
    print message.as_string()
    s.sendmail(test_email, to, message.as_string())
    s.quit()
    return True


def md5(value):
    return hashlib.md5(value).hexdigest()

def autorize():
    loged_in=session.get('loged_in')
    if loged_in:
        email=session.get('email')
        password=session.get('password')
        pers=Session.query(Person).filter_by(email=email, password=password).first()
        pers.last_activity=int(time.time())
        Session.commit()
        return True
    if 'email' and 'password' in request.cookies:
        email=request.cookies.get('email')
        password=request.cookies.get('password')
    elif request.method=='POST' and 'email' in request.POST:
        email=request.POST.get('password')
        password=md5(request.POST.get('password'))
    else:
        return False
    pers=Session.query(Person).filter_by(email=email, password=password).first()
    if pers:
        print 'pers is ', pers
        session['email']=email
        session['password']=password
        session['loged_in']=True
        session['name']=pers.name
        session['person_id']=pers.id
        session.save()
        return True
    return False
def login_required(func):
    def wrapper(self):
          if autorize():
              return func(self)
          else:
              redirect('/auth/signin')
    return wrapper

def get_date():
    time=datetime.datetime.now()
    return time.strftime('%d.%m.%Y %H:%M')
def document_preview(target_url):
    key='rca.1.1.20140729T133847Z.c5e76a9d7bb0d277.20ab36596feb419a8283b4a21557d53414834752'
    request_url='http://rca.yandex.com/?key=%s&url=%s'%(key, target_url)
    resp=urllib2.urlopen(request_url).read()
    json_decoder=json.JSONDecoder()
    result=json_decoder.decode(resp)
    if result:
        c.json=result
        return render_mako('page_preview.mako')
    return ''