from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/')
def python():
	return render_template("form.html")
@app.route('/form',methods=["POST"])
def form():
	name = request.form["name"]
	en_no = request.form["enrollment_no"]
	e_mail= request.form["email"]
	return render_template("form1.html", name=name, en_no=enrollment_no , e_mail=email)
if __name__ == '__main__':
	app.run(port=5050,debug= True)
