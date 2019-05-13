from flask import Flask, render_template, request, flash, url_for, redirect
from forms import ContactForm
from flask_mail import Message, Mail 



app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisismysecret'


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'yourusername@gmail.com'
app.config['MAIL_PASSWORD'] = 'your app specific password'

mail = Mail(app)




# mail.init_app(app)

@app.route('/index')
def index():
	return render_template('index3.html', title='Flask Index', success=True)

@app.route('/form', methods=['GET', 'POST'])
def contactForm():
	form = ContactForm()
	if request.method == 'GET':
		return render_template('contact.html', form=form)
	elif request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required !')
			return render_template('contact.html', form=form)
		else:
			msg = Message(form.subject.data, sender='[SENDER EMAIL]', recipients=['your reciepients gmail id'])
			msg.body = """
			from: %s &lt;%s&gt
			%s
			"""% (form.name.data, form.email.data, form.message.data)
			mail.send(msg)
			return redirect(url_for('index'))
		return '<h1>Form submitted!</h1>'

if __name__ == '__main__':
	app.run(debug=True)


