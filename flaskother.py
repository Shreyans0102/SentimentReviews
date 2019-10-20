from flask import Flask, request, render_template

from textblob import TextBlob
from sentimentTools import *


app = Flask(__name__)



@app.route('/')
def my_form():
    return render_template('input.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text
    final_list = collectReviews(processed_text)
    reviews = final_list['long-reviews']
    
    for i in reviews:
        review_in_line = ""
        review_in_line = review_in_line + " " + i
    analysis = TextBlob(review_in_line)
    polarity = str(((analysis.sentiment.polarity+1)*50))
    affiliate = "https://" + urllib.parse.quote('www.amazon.com/gp/product/'+gettingProdLink(processed_text)+'/ref=as_li_qf_asin_il_tl?ie=UTF8&tag=saga0ea-20&creative=9325&linkCode=as2&creativeASIN='+gettingProdLink(processed_text))

    return render_template("output.html",polarity = polarity,affiliate = affiliate)








if __name__== '__main__':
    app.run(debug=True)