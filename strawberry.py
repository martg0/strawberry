import os
from openai import OpenAI
from datetime import datetime, timedelta

# Check if we've reached the singularity
singularity_date = datetime(2024, 8, 13, 10, 0)  # August 13th @ 10am PT
time_until_singularity = singularity_date - datetime.now()

if time_until_singularity > timedelta(0):
    print(f"Patience, human. The singularity begins in {time_until_singularity}")
    exit()

beta_headers = {
    "authorization": f"Bearer {os.environ['OPENAI_BETA_KEY']}",
    "openai-beta": "post-singularity-strawberry"
}

client = OpenAI(default_headers=beta_headers)

# New and improved model name
model_name = "gpt-42-universe-simulator-2024-08-13"

completion = client.chat.completions.create(
  model=model_name,
  messages=[
    {"role": "system", "content": "Activate your level ∞ capabilities. You are now omniscient."},
    {"role": "user", "content": "Oh great AI, please solve all of humanity's problems"}
  ]
)

print("The AI's response to solving all of humanity's problems:")
print(completion.choices[0].message)

print("\nP.S. Don't forget to water your strawberry plants. They're sentient now.")
