from flask import Flask, render_template
app = Flask(__name__)

posts = [{'author':'peng','date':'May6','title':'first blog','content':'blog content1'},
{'author':'peng','date':'May6','title':'second blog','content':'blog content2'}
]
@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html',posts = posts) 

@app.route("/about")
def about():
	return render_template('about.html',title='about') 

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
