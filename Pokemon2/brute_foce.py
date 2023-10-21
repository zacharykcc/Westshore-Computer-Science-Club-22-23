import os

for count in range(9999):
    pokemon = os.popen("python3 poke_battle.py "+str(count))
    pokemon_output = pokemon.read()
    with open("output.txt", "w") as f:
        f.write(pokemon_output, "\n")
    print("Ran "+ str(count) + "times")
    
