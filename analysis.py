import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download Vader Lexicon for sentiment analysis
nltk.download('vader_lexicon')

# Initialize the VADER sentiment analyzer
sid = SentimentIntensityAnalyzer()

def analyze_sentiment(sentences):
    # Analyze sentiments for each sentence
    for sentence in sentences:
        print(sentence)
        # Get the sentiment score
        sentiment_score = sid.polarity_scores(sentence)
        # Print the sentiment score
        print(sentiment_score)
        # Determine overall sentiment
        if sentiment_score['compound'] >= 0.05:
            print('Overall sentiment: Positive')
        elif sentiment_score['compound'] <= -0.05:
            print('Overall sentiment: Negative')
        else:
            print('Overall sentiment: Neutral')
        print()

if _name_ == "_main_":
    # Prompt user for input
    sentences = []
    print("Enter sentences for sentiment analysis (type 'quit' to finish):")
    while True:
        sentence = input("Enter a sentence: ")
        if sentence.lower() == 'quit':
            break
        sentences.append(sentence)
    
    analyze_sentiment(sentences)
    
