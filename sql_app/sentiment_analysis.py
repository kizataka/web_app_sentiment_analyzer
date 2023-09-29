from transformers import pipeline

nlp = pipeline('sentiment-analysis')

def analyze_sentiment(text):
    result = nlp(text)
    sentiment = result[0]['label']
    score = result[0]['score']

    return {
        'sentiment': sentiment,
        'sentiment_score': score
    }