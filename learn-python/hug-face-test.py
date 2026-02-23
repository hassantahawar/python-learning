from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="distilgpt2"  # lightweight model
)

output = generator(
    "Explain AI in simple words:",
    max_length=100
)

print(output[0]["generated_text"])
