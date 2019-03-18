from flask import Flask, redirect, render_template, request, url_for
from helpers import query, paginate

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search', methods=['GET', 'POST'])
def search():

    query = request.form.get('query')

    results = [
    {'title':'This is result 1', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'https://www.w3schools.com/tags/att_form_action.asp'},
    {'title':'This is result 2', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 3', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 4', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 5', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 6', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 7', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 8', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 9', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'},
    {'title':'This is result 10', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'}
    ]

    page = request.args.get('page', 1, type=int)
    paginate_results = paginate(results, 1, page)
    print(paginate_results)

    return render_template('search.html', query=query, results=paginate_results, title=query, page=1)



@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
