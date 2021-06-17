from flask import Flask, request, make_response, redirect, render_template,session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
app = Flask(__name__)
bootstrap=Bootstrap(app)

app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ['Comprar café', 'Solicitud de compra', 'Entregar video al productor' ]

class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
    # return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(error):
    return render_template('500.html', error=error)
    # return render_template('500.html')


@app.route('/')
def index():
    user_ip= request.remote_addr
    response = make_response(redirect('/hello'))
    # response.set_cookie('user_ip', user_ip)
    session['user_ip'] = user_ip
    return response

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')

    context = {
        'user_ip': user_ip,
        'todos': todos,
        'login_form': login_form,
        'username': username

    }
    
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username

        flash('Nombre de usario registrado con éxito!')

        return redirect(url_for('index'))

# @app.route('/hello')
# def hello():
#     user_ip= session.get('user_ip')
#     context={
#         'user_ip':user_ip, 
#         'todos':todos
#     }

    # user_ip= request.remote_addr
    # return 'hello world Flask, tu IP es {}'.format(user_ip)
    # return f'Hello World Platzi, tu IP es{user_ip}'
    # return render_template('hello.html', user_ip=user_ip)
    return render_template('hello.html', **context)