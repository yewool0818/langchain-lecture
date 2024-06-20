from openai import OpenAI
client = OpenAI()

prompt = "나는 출근할 때"
response_low_temp = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=0,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)
response_high_temp = client.completions.create(
  model="gpt-3.5-turbo-instruct",
  prompt=prompt,
  temperature=0.8,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)

print(f"#낮은 Temperature => {response_low_temp.choices[0].text}")
print('====================================================')
print(f"#높은 Temperature => {response_high_temp.choices[0].text}")