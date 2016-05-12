from flask import Flask
from flask import render_template
from flask import abort
import csv
app = Flask(__name__)

def get_csv():
    csv_path = './static/la-riots-deaths.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

# @app.route('/')
# def homepage():
#     the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

#     return """
#     <h1>Hello HEROKU world</h1>
#     <p>It is currently {time}.</p>

#     <img src="http://loremflickr.com/600/400">
#     """.format(time=the_time)

@app.route("/")
def index():
    template = 'index.html'
    object_list = get_csv()
    return render_template(template, object_list=object_list)

@app.route('/<row_id>/')
def detail(row_id):
    template = 'detail.html'
    object_list = get_csv()
    for row in object_list:
        if row['id'] == row_id:
            return render_template(template, object=row)
    abort(404)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

    #I've added this comment ahhhh