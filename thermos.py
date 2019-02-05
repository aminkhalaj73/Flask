from datetime import datetime
from flask import Flask , render_template , url_for , request , redirect , flash

app = Flask(__name__)
bookmark = []
app.config['SECRET_KEY'] = b'b\x8e6\xf8\xf7\x88\xbe\x00\x06rwn\xe8\xcbQ-\x96\x86\xaa\x1a;\xc0\x85['



def store_bookmarks(url):
    bookmark.append(dict(
    url = url,
    user = "reindert",
    date = datetime.utcnow()
))

class User:
    def __init__(self , firstname , lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def initialise(self):
        return "{}. {}.".format(self.firstname , self.lastname)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html' , man = User('Amin' , 'Khalaj'))

@app.route('/add' ,  methods=['GET' , 'POST'])
def add():
    if request.method == "POST" :
        url = request.form['url']
        store_bookmarks(url)
        flash("Stored Bookmark '{}'".format(url))
        return redirect(url_for('index'))
    return render_template('add.html')
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html') , 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html') , 500

if __name__ == "__main__":
    app.run(debug=True)