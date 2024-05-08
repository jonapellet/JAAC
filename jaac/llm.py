import openai

def simple_completion(api_key, model, system_prompt, user_prompt):

    base_url = "https://openrouter.ai/api/v1"

    client = openai.Client(
        base_url=base_url,
        api_key=api_key
    )

    messages = [
        {
            "role": "system",
            "content": system_prompt,
        },
        {
            "role": "user",
            "content": user_prompt,
        },
    ]

    completion = client.chat.completions.create(
        model=model,
        messages=messages,
    )

    return completion.choices[0].message.content

