from transformers import pipeline

pipe = pipeline("text-classification")

output = pipe("Hi im me")
print(output)