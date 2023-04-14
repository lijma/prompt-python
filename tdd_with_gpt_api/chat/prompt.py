from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import semantic_kernel as sk
from semantic_kernel.ai.open_ai import OpenAITextCompletion
import json
import os


@csrf_exempt
@require_POST
def prompt(request):
    # Get the request body as JSON
    # Check if request_data is provided
    if not request.body:
        return JsonResponse({'error': 'request_data is required'}, status=400)

    request_data = json.loads(request.body)
    prompt = request_data.get('prompt')

    # Check if prompt is provided
    if not prompt:
        return JsonResponse({'error': 'prompt is required'}, status=400)

    # Perform code completion using semantic-kernel-python
    kernel = sk.create_kernel()
    api_key = os.environ.get('OPENAI_API_KEY', '')
    org_id = os.environ.get('OPENAI_ORG_ID', '')
    kernel.config.add_text_backend("dv", OpenAITextCompletion("text-davinci-003", api_key, org_id))
    promptFun = kernel.create_semantic_function(prompt, max_tokens=3000)
    print('------------------------------start------------------------------') 
    content = promptFun()
    print('------prompt------------') 
    print(prompt)
    print('------anwser------------')
    print(content.result) 
    print('------------------------------end------------------------------') 
    # Create a CodeResponse object from the code response
    response_data = {'result': content.result}
    return JsonResponse(response_data)