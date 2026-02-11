from transformers import pipeline

pipeline = pipeline(task="text-generation", model="gpt2")
prompt = "how to make pasta? "
output = pipeline(prompt)
print(output[0]['generated_text'])
