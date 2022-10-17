#Sentiment analysis task
from transformers import pipeline

#create a pipeline object
#inside the pipeline object is task
classifier = pipeline("sentiment-analysis");

#Apply classifier and put data into it
res = classifier("What is this?")

print(res)