# -*- coding: utf-8 -*-
import webapp2
import cgi
import string
form = '''
<style>
body{
    font-size: 20px;
    background-color: #eee;
}
body form label
{
    color: red;
}
body form textarea
{
    height: 200px;
    width: 400px;
}
</style>
<h1>Hello World</h1>
<form method = 'post'>
    <label for='my_text'>
        rot13 translation
    </label>
    <br>
    <textarea name = 'my_text'>%(value)s</textarea>
    <br>
    <input type='submit' value = 'translate it now'> 
</form>
'''

form_show ='''
<p>the input is:</p>
'''
def escape_html(s):
    return cgi.escape(s,quote = True)

def translate(str):
    lower = 'abcdefghijklmnopqrstuvwxyz'
    upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    if str:
        for char in str:
            index = string.find(lower,char)

            if index != -1:
                result += lower[(index + 13) % 26]
            else:
                index = string.find(upper,char)
                if index != -1:
                    result += upper[(index + 13) % 26]
                else:
                    result += char
    
    return result


class MainPage(webapp2.RequestHandler):
    def get(self):
        # self.response.headers['Content-Type'] = 'text/plain'
        # self.response.write(u'sym first page 我的第一个页面')
        # self.response.write(form)
        my_text = self.request.get("my_text")
        my_text = escape_html(my_text)
        self.response.write(form+my_text)

    def post(self):
        my_text = self.request.get('my_text')
        my_text = translate(my_text)
        my_text = cgi.escape(my_text)
        self.response.write(form % {'value':my_text })


class TestformPage(webapp2.RequestHandler):
    def get(self):
        pass
        # self.response.headers['Content-Type'] = 'text/plain'
        # my_text = self.request.get("my_text")
        # my_text = escape_html(my_text)
        # self.response.write(form+my_text)
        # self.request
    def post(self):
        pass




app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/testform', TestformPage),

], debug=True)