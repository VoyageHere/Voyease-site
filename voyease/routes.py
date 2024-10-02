from flask import render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

from . import app, mail

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/privacy_policy')
def privacy_policy():
    return render_template('privacy_policy.html')

@app.route('/customer_tnc')
def customer_tnc():
    return render_template('customers_tnc.html')

@app.route('/guide_and_buddy_tnc')
def guide_and_buddy_tnc():
    return render_template('customers_tnc.html')

@app.route('/submit-query', methods=['POST'])
def submit_query():
    if request.method == "POST":
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')

        # Compose email
        msg = Message("New Contact Us Query",
                      sender="myapptourguide@gmail.com",
                      recipients=["support@voyease.in"])  # Replace with recipient's email
        msg.body = f"""
        New contact us query:

        Name: {name}
        Email: {email}
        Message: {message}
        """
        
        # Send email
        try:
            mail.send(msg)
            flash("Your message has been sent successfully!", "success")
        except Exception as e:
            flash("There was an error sending your message. Please try again later.", "danger")
            print(f"Error: {e}")

        return redirect(url_for('homepage'))