from flask import Flask,render_template,url_for


app = Flask(__name__)

@app.route('/')
def projects():
    return render_template("custom1.html")

@app.route('/about1')
def about():
    return render_template("about.html")
@app.route('/team1')
def team():
    return render_template("ourteam.html")    
@app.route('/work1')
def working():
    return render_template("works.html")
@app.route('/analyst')
def analysing():
	
	return render_template("analyse.html")



	
@app.route('/out')
def outs():
	return render_template("output.html")

if __name__ == '__main__':
	app.run(debug=True)
