#Note: The openai-python library support for Azure OpenAI is in preview.
import os
def financialliteracy(inputtext):
  import openai
  openai.api_type = "azure"
  openai.api_base = "https://euwdsrg00noai1.openai.azure.com/"
  openai.api_version = "2023-09-15-preview"
  openai.api_key = "Yourkey"

  response = openai.Completion.create(
    engine="contractautomation",
    prompt=inputtext,
    temperature=1,
    max_tokens=1937,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    best_of=1,
    stop=None)

  # print(response['choices'][0]['text'])
  return response['choices'][0]['text']
