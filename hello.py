import os
import requests

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("[!] API KEY mancante")
    exit()

domanda = input("Fammi una domanda: ")

response = requests.post(
    "https://api.groq.com/openai/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    },
    json={
        "model": "llama-3.3-70b-versatile",
        "messages": [
            {
                "role": "system",
                "content": "Sei un assistente esperto di programmazione"
            },
            {
                "role": "user",
                "content": domanda
            }
        ]
    }
)

if response.status_code != 200:
    print("Errore:", response.text)
    exit()

data = response.json()

risposta = data["choices"][0]["message"]["content"]

print("\nRisposta AI:\n")
print(risposta)