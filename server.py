from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    user_name = request.args.get("userName", "unknown")
    return render_template('main.html', user=user_name)

guests = ["Daniel"]
@app.route("/guest_list", methods=["GET"])
def guest_get():
    global guests
    return render_template("guests.html", guests=guests)

@app.route("/guest_list", methods=["POST"])
def guest_post():
    global guests

    guest = request.form.get('guest', 'nobody')
    guests.append(guest)

    return render_template("guests.html", guests=guests)