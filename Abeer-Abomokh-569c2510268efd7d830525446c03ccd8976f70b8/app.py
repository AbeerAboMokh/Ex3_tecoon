from flask import Flask, redirect, url_for, render_template, request, session, jsonify
from datetime import timedelta

app = Flask(__name__)

app.secret_key = '123'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)


@app.route('/')
def first_page():  # put application's code here
    return redirect(url_for('display_home_page'))


@app.route('/home')
def display_home_page():  # put application's code here
    return render_template('home.html')


@app.route('/contact')
def display_contact_us():  # put application's code here
    return render_template('contact.html')


@app.route('/assignment3_1')
def display_hobbies_page():
    the_hobbies = ('Writing', 'Dancing', 'basketball')
    return render_template('assignment3_1.html',
                           hobbies_dic=the_hobbies,
                           no_hobbies_message='Ops, there is no hobbies to display!')


users = {
    "user1": {"name": "ahmd", "email": "ahmd@gmail.com", "user_name": "El ahmad"},
    "user2": {"name": "abeer", "email": "abeer@gmail.com", "user_name": "El abeer"},
    "user3": {"name": "thaer", "email": "thaer@gmail.com", "user_name": "El thaer"},
    "user4": {"name": "Messi", "email": "Messi@gmail.com", "user_name": "El Messi"},
    "user5": {"name": "roaa", "email": "roaa@gmail.com", "user_name": "El roaa"}

}

user_data = {
    'El ahmad': '123',
    'El abeer': '125',
    'El thaer': '126',
    'El Messi': '127',
    'El roaa': '128',
}


@app.route('/assignment3_2', methods=['GET', 'POST'])
def display_users_page():  # put application's code here
    if request.method == 'POST':
        user_name = request.form['user_name']
        password = request.form['password']
        if user_name in user_data:
            user_password = user_data[user_name]
            if user_password == password:
                session['user_name'] = user_name
                session['loged_in'] = True
                return render_template('assignment3_2.html',
                                       message='hi:)',
                                       user_name=user_name)
            else:
                return render_template('assignment3_2.html',
                                       message='The pass is Wrong!!')
        else:
            return render_template('assignment3_2.html',
                                   message=' sign in :)!')
    else:
        if 'name' in request.args:
            name = request.args["name"]
            if name == '':
                return render_template('assignment3_2.html', users=users)
            details = None
            for user_name in users.values():
                if user_name['name'] == name:
                    details = user_name
                    break
            if details:
                return render_template('assignment3_2.html',
                                       name=details['name'],
                                       email=details['email'],
                                       user_name=details['user_name']
                                       )
            else:
                return render_template('assignment3_2.html',
                                       no_user_message='No user found!!')
        return render_template('assignment3_2.html')


@app.route('/log_out')
def logout_func():
    session['loged_in'] = False
    session.clear()
    return redirect(url_for('display_users_page'))


@app.route('/session')
def session_func():
    return jsonify(dict(session))


if __name__ == '__main__':
    app.run()
