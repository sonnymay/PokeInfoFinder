import requests
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

def get_pokemon_info(name: str):
    url = f"https://pokeapi.co/api/v2/pokemon/{name.lower()}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error occurred while fetching info for Pokémon: {name}")
        return None

def show_pokemon_info():
    name = pokemon_name_entry.get()
    pokemon_info = get_pokemon_info(name)

    if pokemon_info:
        pokemon_name_label.config(text=pokemon_info['name'].capitalize())
        pokemon_height_label.config(text=f"Height: {pokemon_info['height']}")
        pokemon_weight_label.config(text=f"Weight: {pokemon_info['weight']}")

        abilities = ", ".join([ability['ability']['name'].capitalize() for ability in pokemon_info['abilities']])
        pokemon_abilities_label.config(text=f"Abilities: {abilities}")

        stats = "\n".join([f"{stat['stat']['name'].capitalize()}: {stat['base_stat']}" for stat in pokemon_info['stats']])
        pokemon_stats_label.config(text=f"Stats:\n{stats}")

        # Get Pokemon's image and display it
        response = requests.get(pokemon_info['sprites']['front_default'])
        image = Image.open(BytesIO(response.content))
        image = image.resize((100, 100), Image.ANTIALIAS)  # Resize the image
        photo = ImageTk.PhotoImage(image)

        pokemon_image_label.config(image=photo)
        pokemon_image_label.image = photo  # Keep a reference to the image
    else:
        print(f"No information found for Pokémon: {name}")

root = Tk()

pokemon_name_entry = Entry(root)
pokemon_name_entry.pack()

search_button = Button(root, text="Search", command=show_pokemon_info)
search_button.pack()

pokemon_name_label = Label(root)
pokemon_name_label.pack()

pokemon_height_label = Label(root)
pokemon_height_label.pack()

pokemon_weight_label = Label(root)
pokemon_weight_label.pack()

pokemon_abilities_label = Label(root)
pokemon_abilities_label.pack()

pokemon_stats_label = Label(root)
pokemon_stats_label.pack()

pokemon_image_label = Label(root)
pokemon_image_label.pack()

root.mainloop()
