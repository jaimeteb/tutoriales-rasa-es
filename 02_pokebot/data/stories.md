## buscar pokemon por nombre 1
* buscar_pokemon
  - utter_ask_pokemon
* buscar_pokemon{"nombre_pokemon": "Ivysaur"}
  - action_buscar_pokemon

## buscar pokemon por número 1
* buscar_pokemon
  - utter_ask_pokemon
* buscar_pokemon{"numero_pokemon": "41"}
  - action_buscar_pokemon

## buscar pokemon por nombre 2
* buscar_pokemon{"nombre_pokemon": "Ivysaur"}
  - action_buscar_pokemon

## buscar pokemon por número 2
* buscar_pokemon{"numero_pokemon": "41"}
  - action_buscar_pokemon

## saludo
* saludo
  - utter_saludo
  - utter_ask_pokemon

## start
* start
  - utter_saludo
  - utter_ask_pokemon
