from flask import Flask,render_template, request
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.downloader.download('vadar_lexicon')

app = Flask(__name__)

@app.route('/', methods= ['GET','POST'])
def main():
    if request.method =="POST":
        input = request.form.get("input")
        sid = SentimentIntensityAnalyzer()
        score = sid.polarity_scores(input)
        if score["neg"] != 0:
            return render_template('home.html', message="Negative😞😞")
        else:
            return render_template('home.html', message="Positive😄😄")
    return render_template('home.html')


if __name__=="__main__":
    app.run(debug=True)