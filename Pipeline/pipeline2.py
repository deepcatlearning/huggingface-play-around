#Text generation task
from transformers import pipeline

#Create a pipeline object (generator)
generator = pipeline("text-generation", model="distilgpt2")

#generator(data, max_length, sequences)
res = generator(
    "Will deepcatlearing be able to",
    max_length=25,
    num_return_sequences=5,
)

print(res)