import openai

api_key = "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"
openai.api_key = api_key

try:
    with open('symptoms_data.txt', 'r') as file:
        prompt = file.read()

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150  
    )

    diagnosis = response["choices"][0]["message"]["content"].strip()

    with open('diagnosis.txt', 'w') as output_file:
        output_file.write(diagnosis)

    print("Diagnosis saved to diagnosis.txt")

except FileNotFoundError:
    print("Error: dog_characteristics.txt not found.")
except openai.error.APIError as e:
    print("OpenAI API Error:", e)
except Exception as e:
    print("An unexpected error occurred:", e)
