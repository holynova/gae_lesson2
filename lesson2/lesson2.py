import os
import cgi
import webapp2
import string
import jinja2
template_dir = os.path.join(os.path.abspath('.'),'htmls')
env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape = True)

# def render(template,**kw):
# 	t = env.get_template(template)

class BaseClass(webapp2.RequestHandler):
	def render(self, template,**kw):
		t = env.get_template(template)
		self.response.write(t.render(**kw))

# class TestHandler(webapp2.RequestHandler):
#     def get(self):
#         self.response.out.write('test hello world')

class MainPage(BaseClass):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'params
        self.response.out.write('Hello, World!<br><a href ="/sign_up" >sign_up</a>')

class SignUp(BaseClass):
    def get(self):
    	self.render('sign_up.html')
    def post(self):
    	username = self.request.get('username')
    	password = self.request.get('password')
    	password_again = self.request.get('password_again')
    	mail = self.request.get('mail')
    	# para = dict(us)
    	params = dict(username = username,
    					password = password,
    					password_again = password_again,
                      mail = mail,
                      error_username = username,
                      error_mail = mail)
    	# t = env.get_template('sign_up.html')
    	# self.write(t.render(username = username,password = password,password_again = password_again,mail=mail))
    	self.render('sign_up.html',**params)
	# def verify(self,username = '',password):
		# pass 	




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/sign_up',SignUp),
], debug=True)