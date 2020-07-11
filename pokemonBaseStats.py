import requests
import json
import sys

url = "https://pokemon-go1.p.rapidapi.com/pokemon_stats.json"

headers = {
    'x-rapidapi-host': "pokemon-go1.p.rapidapi.com",
    'x-rapidapi-key': "819a9115damsh766b3a16a6bcc8bp1c6be7jsn5b2e640e22ee"
    }

response = requests.get(url, headers=headers)
pokemonStats = json.loads(response.text)

for i in range(len(pokemonStats)):
    pokemonData = str(pokemonStats[i]).encode('utf-8')
    print(pokemonData)
     
def baseAttack():
    highestAttack = 0
    highestAttackPokemon = ""
    for i in range(len(pokemonStats)):
        if (pokemonStats[i]["base_attack"] > highestAttack):
            highestAttack = pokemonStats[i]["base_attack"]
            highestAttackPokemon = pokemonStats[i]["pokemon_name"]
    return "Highest attack: " + highestAttackPokemon + ": " + str(highestAttack)

def baseDefense():
    highestDefense = 0
    highestDefensePokemon = ""
    for i in range(len(pokemonStats)):
        if (pokemonStats[i]["base_defense"] > highestDefense):
            highestDefense = pokemonStats[i]["base_defense"]
            highestDefensePokemon = pokemonStats[i]["pokemon_name"]
    return "Highest defense: " + highestDefensePokemon + ": " + str(highestDefense)

def baseStamina():
    highestStamina = 0
    highestStaminaPokemon = ""
    for i in range(len(pokemonStats)):
        if (pokemonStats[i]["base_stamina"] > highestStamina):
            highestStamina = pokemonStats[i]["base_stamina"]
            highestStaminaPokemon = pokemonStats[i]["pokemon_name"]
    return "Highest Stamina: " + highestStaminaPokemon + ": " + str(highestStamina)

def averageAttack():
    total = 0
    for i in range(len(pokemonStats)):
        total += pokemonStats[i]["base_attack"]
    return "Average attack: "  + str(total/len(pokemonStats))

def averageDefense():
    total = 0
    for i in range(len(pokemonStats)):
        total += pokemonStats[i]["base_defense"]
    return "Average defense: "  + str(total/len(pokemonStats))

def averageStamina():
    total = 0
    for i in range(len(pokemonStats)):
        total += pokemonStats[i]["base_stamina"]
    return "Average stamina: "  + str(total/len(pokemonStats))
 
print(baseAttack())
print(averageAttack())
print(baseDefense())
print(averageDefense())
print(baseStamina())
print(averageStamina())
            
    
    