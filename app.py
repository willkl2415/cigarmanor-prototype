from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/rewards')
def rewards():
    with open('rewards_data.json') as f:
        data = json.load(f)
    return render_template('rewards.html', data=data)

@app.route('/scan', methods=['GET', 'POST'])
def scan():
    if request.method == 'POST':
        code = request.form['qr_code']
        return redirect(url_for('rewards'))
    return render_template('scan.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/events')
def events():
    return render_template('events.html')

if __name__ == '__main__':
    app.run(debug=True)
