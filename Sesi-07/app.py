# # import basic buat make flask
from flask import Flask

# # ini buat make fitur escape
from markupsafe import escape

# # ini buat yang login, dia make request
# # ini bisa juga langsung di tiban di flaks atas
# # from flask import Flask, request
from flask import request

# # ini buat make template html yang udh dibuat
# # ini bisa juga langsung di tiban di flaks atas
# # from flask import Flask, request, render_template
from flask import render_template

app = Flask(__name__)

# # ini buat routing halaman, (mirip routing module di angular(?))
@app.route('/')
def index():
    # # ini kek html biasa
    # return 'Index Page'
    return render_template('index.html')


# @app.route('/hello')
# # kalo ada 2< diatas def gini, kalo di run di browser dua2nya ngehasilin yang sama
@app.route('/world')
@app.route('/hello/')
@app.route('/hello/<name>')
# def hello_world():
#     # # ini kek html biasa
#     return '<h1>Hello, World!</h1>'
def hello_n(name=None):
    return render_template('hello.html', name=name)

# # pake <> itu namany dynamic routing
@app.route('/<name>')
# # kalo di run di browser
# # http://localhost:5000/andi
# # hasilnya hello, andi
def hello(name):
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/book/<title>')
def show_book_profile(title):
    # show the book profile for that title
    return f'Book detail: {escape(title)}'

@app.route('/post/<int:post_id>')
# # baru bisa di run kalo angka
# # http://localhost:5000/post/21
# # ini error
# # http://localhost:5000/post/2i
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/post/<string:post_id>')
# # kalo ini bisa run semua
# # http://localhost:5000/post/ateng
def show_str_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
# # contoh
# # http://localhost:5000/path/dir
# # http://localhost:5000/path/a/b/c/d
# # kalo gini error
# # http://localhost:5000/path/
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
        # pass
    else:
        return show_the_login_form()
        # pass
def do_the_login():
    # # ini sementara buat run pake "curl -d 'username=rebekah' localhost:5000/login"
    return "Do the login"
def show_the_login_form():
    # # soalnya kalo nggak ini di run auto yang ini
    return "Displaying login form"

    
if __name__ == '__main__':
    # app.run()
    # # ini buat sekalian nyalain debug
    app.run(debug=True)