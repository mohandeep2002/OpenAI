from django.shortcuts import render
import requests

def generate_response(request):
  
    if request.method == 'POST':  
      url = "https://api.openai.com/v1/engines/text-davinci-002/completions"

      prompt = request.POST['input']
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
      # print(response) just for pushing
      
      generated_response = response["choices"][0]["text"]

      return render(request, 'generated_response.html', {
          'generated_response': generated_response,
          'res': response
          })
    else :
      return render(request, 'generated_response.html')