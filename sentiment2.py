from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

# Substitua 'your_key' e 'your_endpoint' com suas próprias credenciais
endpoint = "https://sentimentalazure.cognitiveservices.azure.com/"
key = "14b6fbbfc1e9401998e090e3d3a779f6"

credential = AzureKeyCredential(key)
text_analytics_client = TextAnalyticsClient(endpoint=endpoint, credential=credential)

documents = [
    "I really enjoy the taste of this food!",
    "I'm so frustrated with this product.",
    "This movie was fantastic."
]

response = text_analytics_client.analyze_sentiment(documents=documents)

for idx, doc in enumerate(response):
    print("Document:", documents[idx])
    print("Overall sentiment:", doc.sentiment)
    print()
