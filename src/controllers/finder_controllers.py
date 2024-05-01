import requests
from bs4 import BeautifulSoup
from flask import render_template, request, redirect

def get_answer():
    answer = None
    if request.method == "POST":
        subject = request.form['subject']

        if subject:
            search_url = "https://en.wikipedia.org/wiki/"
            header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

            subject_url = f'{search_url}{subject}'

            requisiton = requests.get(subject_url, headers=header)
            html_result = BeautifulSoup(requisiton.text, "html.parser")

            result_paragraphs = html_result.find_all('p')

            for content in result_paragraphs:
                if len(content.get_text()) > 10:
                    answer = content.get_text()
                
                if len(content.get_text()) > 500:
                    break
        
    return render_template('finder.html', answer=answer)