from puppycompanyblog.models import BlogPost
from flask import Flask, render_template,url_for,redirect,Blueprint,request
import stripe
public_key="pk_test_TYooMQauvdEDq54NiTphI7jx"   #form this link-https://stripe.com/docs/legacy-checkout/flask   ....user guide-https://stripe.com/docs
stripe.api_key="sk_test_4eC39HqLyjWDarjtT1zdp7dc"

core=Blueprint('core',__name__)

@core.route('/')
def index():
    page=request.args.get('page',1,type=int)  #cycle through user post
    blog_posts=BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=5)
    return render_template("index.html",blog_posts=blog_posts)

@core.route('/donation')
def donation():
    return render_template("donation.html",public_key=public_key)

@core.route('/info')
def info():
    return render_template("info.html")

@core.route("/thankyou")
def thankyou():
    return render_template("thankyou.html")

@core.route("/payment",methods=['POST'])
def payment():
    customer=stripe.Customer.create(email=request.form['stripeEmail'],source=request.form['stripeToken'])
    charge=stripe.Charge.create(customer=customer.id,amount=1999,currency='usd',description='Donation')

    return redirect(url_for("core.thankyou"))
