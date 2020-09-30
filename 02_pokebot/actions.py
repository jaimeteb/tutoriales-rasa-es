from rasa_sdk import Action, Tracker
from rasa_sdk.forms import FormAction
from rasa_sdk.events import SlotSet, UserUtteranceReverted, AllSlotsReset, Restarted
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List, Union, Optional

# from datetime import datetime
# from redis import Redis
# from time import sleep

# import unidecode
import requests
# import logging
# import random
# import json
# import os
# import re

class ActionBuscarPokemon(Action):
    def name(self):
        return "action_buscar_pokemon"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        nombre_pokemon = tracker.get_slot("nombre_pokemon")
        numero_pokemon = tracker.get_slot("numero_pokemon")

        dispatcher.utter_message(template="utter_info_pokemon")
        return [AllSlotsReset()]
