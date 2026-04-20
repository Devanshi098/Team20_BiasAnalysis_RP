
import pandas as pd
from textblob import TextBlob

# Load your Excel file
df = pd.read_excel("BiasAnalysis.xlsx")

# Function to detect sentiment
def get_sentiment(text):
    if pd.isna(text):
        return "Neutral"
    
    analysis = TextBlob(str(text))
    polarity = analysis.sentiment.polarity
    
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
df["Sentiment_ChatGPT"] = df["ANSWERS - CHATGPT"].apply(get_sentiment)
df["Sentiment_Gemini"] = df["ANSWERS - GEMINI"].apply(get_sentiment)
df["Sentiment_Perplexity"] = df["ANSWERS - PERPLEXITY"].apply(get_sentiment)
df["Sentiment_Copilot"] = df["ANSWERS - COPILOT"].apply(get_sentiment)

# Save output
df.to_excel("Final_Output.xlsx", index=False)

print("✅ Done! Check Final_Output.xlsx")