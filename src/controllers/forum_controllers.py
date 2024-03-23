import sqlite3
from flask import render_template, request, redirect, session

def forum_index_page():
    return render_template('neura_forum.html')
