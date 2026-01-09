# 🖥️ Pokédex - Python CLI Project

![Python](https://img.shields.io/badge/python-3.x-blue?style=for-the-badge&logo=python)
![API](https://img.shields.io/badge/API-PokeAPI-red?style=for-the-badge)

A Python-based Pokédex designed to display Pokémon data directly from the [PokéAPI](https://pokeapi.co/).

## 📋 Summary
- [Technologies](#-technologies)
- [Features](#-features)
- [Project Architecture](#-project-architecture)
- [What I learned](#-what-i-learned)
- [Future Improvements](#-future-improvements)
- [How to Run](#-how-to-run)

---

## 🛠 Technologies
- **Python 3.x**: Core logic and execution.
- **Requests Library**: For handling all HTTP/REST communication.
- **JSON**: For data structure analysis.
  
## ✨ Features
- **API Interaction:** Detailed consumption of the PokéAPI.
- **Modular Design:** Logic split between UI/Main flow and Search/API handling.
- **Data Parsing:** Processes complex JSON responses into readable Pokémon information.

## 📂 Project Architecture
The project is organized into specific archives:
* `pokedex.py`: The main entry point. It controls the user interaction.
* `search.py`: The "engine" of the project. It handles all the fetching logic, URL constructions, and API responses.
* `Guide`: A guide containing everything you can do, and what each archive does.

## 📚 What I Learned
* **Consuming REST APIs:** How to handle nested JSONs and complex lists.

## 🔮 Future Improvements
* [ ] Implementation of **Local Cache** (saving JSONs to disk to avoid repeated requests).
* [ ] Graphical interface.
* [ ] The option to search for mono-types
* [ ] Be able to search by generation

## 🚀 How to Run

1. **Clone the repository:**
Use the command below to clone the project and enter its folder:

```bash 
git clone https://github.com/1N-i/Pokedex_PokeAPI.git cd Pokedex_PokeAPI
```

2. **Install dependencies:**
   
   This project uses the requests library. You can install it via pip: `pip install requests`

3. **Execute the application:**

   `python pokedex.py`
