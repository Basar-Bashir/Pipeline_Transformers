from transformers import pipeline

pipeline = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions")

message = "I'm about to die."

output = pipeline(message)

print(output[0])