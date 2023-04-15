import openai

API_KEY = "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"
openai.api_key = API_KEY

while True:
    model_engine = "text-davinci-003"
    prompt = input ("Enter new prompt: ")
    if "exit" in prompt or "quit" in prompt:
        break
    completion = openai.Completion.create(
        engine = model_engine,
        prompt = prompt,
        max_tokens = 200,
        n = 1,
        stop = None,
        temperature = 0.5
    )
    response = completion.choices[0].text
    print(response)