#Zero shot classification task
from transformers import pipeline

# #Pipeline object
classifier = pipeline("zero-shot-classification")

#To see how much % input text is in the defined label.
res = classifier(
    "Prayut failed as a Thailand Prime minister",
    candidate_labels=["food", "politics"],
)

res2 = classifier(
    "Taco is super delicious",
    candidate_labels=["food", "politics"],
)

print(res)
print(res2)