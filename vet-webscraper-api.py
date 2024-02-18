import openai
import requests
from bs4 import BeautifulSoup

def find_vets_near_me(location):
    search_query = "vets near " + location.replace(" ", "+") + "with phone number and address"
    search_url = f"https://www.google.com/search?q={search_query}"
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(search_url, headers=headers)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    vet_divs = soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd')
    
    vets = []
    for vet_div in vet_divs:
        vet_info = vet_div.text.split(" - ")
        vet_name = vet_info[0]
        vet_details = vet_info[1] if len(vet_info) > 1 else ""
        vets.append((vet_name, vet_details))
    
    return vets


api_key = "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"
openai.api_key = api_key

location = "Des Moines"  
vets_near_me = find_vets_near_me(location)
vets_string = "only get the hospital names with phone number and address and format it Hospital, Phone Number, and Address in separate lines. Check the whole array element for it"

print("Vets near you")
for vet in vets_near_me:
    vets_string += str(vet) + "\n"


response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  
    messages=[{"role": "user", "content": vets_string}],
    max_tokens=150  
)

if 'choices' in response and len(response['choices']) > 0:
    completion = response['choices'][0]['message']['content']
    with open('completion.txt', 'w') as file:
        file.write(completion)