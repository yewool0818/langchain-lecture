from openai import OpenAI
client = OpenAI()

prompt = "흥미로운 이야기가 있어."
response_low_topP = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=0.2,
  max_tokens=256,
  top_p=0.1,
  frequency_penalty=0,
  presence_penalty=0
)
response_high_topP = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=0.2,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(f"#낮은 TopP => {response_low_topP.choices[0].text}")
print('====================================================')
print(f"#높은 TopP => {response_high_topP.choices[0].text}")