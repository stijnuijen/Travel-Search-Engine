from flask import Flask, redirect, render_template, request, url_for
from helpers import query

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/search', methods=['GET', 'POST'])
def search():

    if request.method == 'POST':

        query = request.form.get('query')

        if not query:
            return render_template('home.html')

        results = [{'title':'This is result 1', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'url':'https://www.w3schools.com/tags/att_form_action.asp'},{'title':'This is result 2', 'text':'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.', 'url':'http://flask.pocoo.org/docs/1.0/quickstart/#routing'}]

        page = request.args.get('page', 1, type=int)
        results_per_page = 1
        paginate_results = [results[i * results_per_page:(i + 1) * results_per_page] for i in range((len(results) + results_per_page - 1) // results_per_page)][page-1]

        return render_template('search.html', query=query, results=paginate_results, title=query)

    else:
        return redirect('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

if __name__ == '__main__':
    app.run(debug=True)
