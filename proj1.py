from flask import Flask , redirect , url_for , render_template , request ,session
from datetime import timedelta

shop = {'Saree': 1000 ,'Gown' : 2000 , 'Bangles' : 3000 , 'Shoes' : 4000}
quantity = {}
total = {}
user_name = { "joyel" : "qwerty" , "eldho" : "1234" }

app=Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes = 5)


@app.route("/")
def home():
    return f"<h1>WELCOME TO ONLINE SHOPING<h1>"


@app.route("/login" , methods = ["POST" , "GET"])
def login():
    flag = 0
    if  request.method == "POST" :
        session.permanent = True
        login_name = request.form["name"]
        login_password = request.form["password"]
        for key , value in user_name.items() :
             if key == login_name and value == login_password :
                session["login_name"] = login_name
                return redirect(url_for("cart"))
                flag = 1
                break
        if flag == 0 :
            return f"<h5> INVALID USERNAME OR PASSWORD <h5>"
        
    else:
        if "login_name" in session:
            return redirect(url_for("cart"))
        return render_template("login1.html")


@app.route("/cart" , methods = ["POST" , "GET"])
def cart():
    grand_total = 0
    if "login_name" in session:
        login_name = session["login_name"]
        if  request.method == "POST":
            for key in shop:
                quantity[key] = int(request.form[key])
                total[key] = shop[key] * quantity[key]
                grand_total +=  total[key]
            return render_template("paybill.html" , total = total , quantity = quantity , shop = shop , grand_total = grand_total , login_name = login_name)
        else:
            return render_template("pro1.html", shop=shop , login_name = login_name)
    else:
            return redirect(url_for("login"))



@app.route("/logout") 
def logout():
    session.pop("login_name", None)
    return redirect(url_for("login"))  


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug = True)
