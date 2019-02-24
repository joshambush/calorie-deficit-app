from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)
@app.route("/")
def mainpage():
	return render_template("index.html")
	

@app.route('/', methods=['POST'])
def datapass():
	dailymeals = request.form["daily-meals"]
	age = request.form["user-age"]
	weight = request.form["user-weight"]
	heightft = request.form.get("user-ft")
	heightin = request.form.get("user-in")
	tableset = []
	for x in range(0,int(dailymeals)):
		tableset.append("<td></td>")
	return render_template("index.html", meals=dailymeals, age=age, weight=weight, heightft=heightft, heightin=heightin, tableset=tableset)
# datapass=pyvar
if __name__ == "__main__":
	app.run(debug=True)	
