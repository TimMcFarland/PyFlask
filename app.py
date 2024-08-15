from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

background_images = [
    "https://images.unsplash.com/photo-1602661287394-ccf02e1a0893?q=80&w=2940&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1519125323398-675f0ddb6308?auto=format&fit=crop&w=1350&q=80",
    "https://images.unsplash.com/photo-1495954484750-af469f2f9be5?auto=format&fit=crop&w=1350&q=80"
]

@app.route('/')
def index():
    # Define multiple items, each as a dictionary
    group1 = {'Group':'JBP', 'Carrier':'Highmark', 'CMK':'252', 'Vision':'Davis', 'Dental':'UCCI', 'MedRates':'-11.50'}
    group2 = {'Group':'Ninja', 'Carrier':'BlueCross', 'CMK':'300', 'Vision':'VSP', 'Dental':'Delta', 'MedRates':'5.00'}

    # Combine them into a list
    alphabet = [group1, group2]

    words = "Hello, Flask Server!"
    background_image = random.choice(background_images)

    # Pass the list of dictionaries directly to the template
    return render_template('index.html', words=words, background_image=background_image, alphabet=alphabet)

@app.route('/Prev')
def previous():
    # Define multiple items, each as a dictionary
    group1 = {'Group':'JBP', 'Carrier':'Highmark', 'CMK':'252', 'Vision':'Davis', 'Dental':'UCCI', 'MedRates':'-11.50'}
    group2 = {'Group':'Ninja', 'Carrier':'BlueCross', 'CMK':'300', 'Vision':'VSP', 'Dental':'Delta', 'MedRates':'5.00'}

    # Combine them into a list
    alphabet = [group1, group2]

    words = "Previous Word"
    background_image = random.choice(background_images)
    return render_template('index.html', words=words, background_image=background_image, alphabet=alphabet)

@app.route('/Next')
def next():
    # Define multiple items, each as a dictionary
    group1 = {'Group':'JBP', 'Carrier':'Highmark', 'CMK':'252', 'Vision':'Davis', 'Dental':'UCCI', 'MedRates':'-11.50'}
    group2 = {'Group':'Ninja', 'Carrier':'BlueCross', 'CMK':'300', 'Vision':'VSP', 'Dental':'Delta', 'MedRates':'5.00'}

    # Combine them into a list
    alphabet = [group1, group2]

    words = "Next Word"
    background_image = random.choice(background_images)
    return render_template('index.html', words=words, background_image=background_image, alphabet=alphabet)

if __name__ == '__main__':
    app.run(debug=True)