from django.shortcuts import render
import requests

def generate_response(request):
    url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

    prompt = "Hi this is mohandeep"
    payload = {
      "prompt": prompt,
      "max_tokens": 128,
      "n": 1,
      "stop": None,
      "temperature": 0.5,
    }
    headers = {
      "Content-Type": "application/json",
      "Authorization": "Bearer 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"
    }
    response = requests.post(url, json=payload, headers=headers).json()
    # print(response)
    generated_response = response["choices"][0]["text"]

    return render(request, 'generated_response.html', {
        'generated_response': generated_response,
        'res': response
        })
