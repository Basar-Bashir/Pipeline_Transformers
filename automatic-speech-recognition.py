from transformers import pipeline

pipeline = pipeline(task ="automatic-speech-recognition", model ="openai/whisper-tiny")
output = pipeline(inputs ="https://huggingface.co/datasets/Narsil/asr_dummy/resolve/main/mlk.flac", return_timestamps="word", language="en")
print(output)