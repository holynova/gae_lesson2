import os
import cgi
import webapp2
import string
import jinja2
import re
from google.appengine.ex import db


template_dir = os.path.join(os.path.abspath('.'),'htmls')
env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

# def render(template,**kw):
# 	t = env.get_template(template)
class User(db.modle):
    username = db.StringProperty()
    password = db.StringProperty()
    mail = db.StringProperty()
    time = db.DateTimeProperty(auto_now_add = True)


class BaseClass(webapp2.RequestHandler):
	def render(self, template,**kw):
		t = env.get_template(template)
		self.response.write(t.render(**kw))


class MainPage(BaseClass):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'params
        self.response.out.write('Hello, World!<br><a href ="/sign_up" >sign_up</a>')

class SignUp(BaseClass):
    def get(self):
    	self.render('sign_up.html')
    # def verify(self,username,password,password_again,mail):


    def post(self):
    	username = self.request.get('username')
    	password = self.request.get('password')
    	password_again = self.request.get('password_again')
    	mail = self.request.get('mail')
    	# para = dict(us)

        #verify
        flag_error = False
        if not re.compile(r"^(?=.{8,20}$)(?![_.])(?!.*[_.]{2})[a-zA-Z0-9._]+(?<![_.])$").match(username):
            error_username = 'username is not avaliable'
            flag_error = True
        if password != password_again:
            error_password_again = 'password does not match the first one'
            flag_error = True
        if not re.compile(r"^[a-z]([a-z0-9]*[-_]?[a-z0-9]+)*@([a-z0-9]*[-_]?[a-z0-9]+)+[\.][a-z]{2,3}([\.][a-z]{2})?$").match(mail):
            error_mail = 'wrong e-mail'
            flag_error = True

        if not flag_error:
            new_user = User(name = name,
                            password = password,
                            mail = mail)
            new_user.push()

        params = dict(username = username,
                        password = password,
                        password_again = password_again,
                      mail = mail,
                      error_username = error_username,
                      error_password_again = error_password_again,
                      error_mail = error_mail,
                      success_msg = 'congratulations '+username+" successfully sign up")


        
    	# t = env.get_template('sign_up.html')
    	# self.write(t.render(username = username,password = password,password_again = password_again,mail=mail))
    	self.render('sign_up.html',**params)
	# def verify(self,username = '',password):
		# pass 

class SignIn(BaseClass):
    def get(self):
        pass
    def post(self):
        pass


class Password(BaseClass):
    def get(self):
        pass
    def post(self):
        pass






app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign_up',SignUp),
    ('/signin',SignIn),
    ('/password',PassWord),
], debug=True)