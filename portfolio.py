from flask import Flask, render_template, request

portfolio = Flask(__name__)

@portfolio.route('/')
def index():
    return render_template('index.html')

@portfolio.route('/about')
def about():
    return render_template('about.html')

@portfolio.route('/')
def skill():
    return render_template('skill.html')

@portfolio.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return "Thank you for the message!"
    return render_template('contact.html')

if __name__== '__main__':
    portfolio.run(debug=True)