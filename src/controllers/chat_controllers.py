import sqlite3
from flask import render_template, redirect, request, session

def mail_index_page():
    return render_template('inbox.html')

def send_message():
    return render_template('send_message.html')