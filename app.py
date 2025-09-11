from flask import Flask,render_template,request,redirect,url_for
import streamlit as st


app=Flask(__name__)


@app.route("/")
def welcome():
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)