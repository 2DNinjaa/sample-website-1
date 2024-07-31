from flask import Flask,redirect,url_for,render_template,session,flash,request,send_from_directory, redirect, jsonify, json, abort,make_response,send_file  #,make_response
app = Flask(__name__)

@app.route('/',methods=["POST","GET"])         #this is the home page
def home(): 
    return render_template("homepage.html",base="base.html")

@app.route('/works',methods=["POST","GET"])         #this is the home page
def pastExamples(): 
    return render_template("pastWorks.html",base="base.html")

@app.route('/services',methods=["POST","GET"])         #this is the home page
def service(): 
    return render_template("services.html",base="base.html")

@app.route('/about',methods=["POST","GET"])         #this is the home page
def about(): 
    return render_template("about.html",base="base.html")



@app.route('/contact',methods=["POST","GET"])         #this is the home page
def contactUs(): 
    return render_template("contact.html",base="base.html")

if __name__ == '__main__':
   app.run()