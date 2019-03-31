from flask import Flask, redirect, render_template, request, url_for
from helpers import query, paginate
import json
from search import querysearch

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.route('/')
def index():
    return render_template('home.html')


@app.route('/search/', methods=['GET', 'POST'])
def search():

    index_dir = 'C:/Users/leonv/Documents/development/Master/Information_retrieval/clean_INDEX.json'
    with open(index_dir) as f:
        index = json.load(f)

    titles_dir = 'C:/Users/leonv/Documents/development/Master/Information_retrieval/travelsearch/index_titles.json'
    with open(titles_dir) as f:
        titles = json.load(f)

    # request the forms from the page
    search_query = request.values.get('query')

    if not query:
        return render_template('home.html')

    # check radio buttons for theme filters
    filters = request.values.getlist('check')
    print(filters)

    if 'food' in filters:
        food = True
    else:
        food = False


    if 'culture' in filters:
        culture = True
    else:
        culture = False

    if 'transport' in filters:
        transport = True
    else:
        transport = False

    print(food, culture, transport)

    continent = request.values.get('continent')
    print(continent)

    # results=[]
    results = querysearch(index, titles, query=search_query, food=food, culture=culture, transport=transport, continent=continent)
    print(results[:11])

    # error handler if user does not fill in query
    if not search_query or not results:
        render_template('home.html')

    # split list in list of lists based on the results per page
    # paginate_results = paginate(results, per_page, page)

    return render_template('search.html', query=search_query, results=results, title=search_query)


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/submit',methods=['GET', 'POST'])
def submit():

    evaluation_results = []

    # loop over all radio button names and store their values is a list
    for i in range(1,11):
        evaluation_results.append(request.values.get(str(i)))

    # write the evaluation list to file
    with open('evaluations.txt', 'a+') as f:
        f.writelines("%s" % i for i in evaluation_results)
        f.write("\n")

    return render_template('submit.html', title="Submitted form")


if __name__ == '__main__':
    app.run(debug=True)
