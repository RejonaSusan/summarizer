# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("text2text-generation", model="Graverman/t5-code-summary")

res = pipe(
"""

""", max_new_tokens=50 )

print(res[0]['generated_text'])