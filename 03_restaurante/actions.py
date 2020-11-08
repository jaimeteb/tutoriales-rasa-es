from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class RestaurantForm(FormAction):
    """Example of a custom form action"""

    def name(self) -> Text:
        """Unique identifier of the form"""

        return "restaurante_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["cocina", "numero_personas", "asiento_exterior", "preferencias", "comentarios"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "cocina": self.from_entity(entity="cocina", not_intent="chitchat"),
            "numero_personas": [
                self.from_entity(
                    entity="number", intent=["informar", "solicitar_restaurante"]
                ),
            ],
            "asiento_exterior": [
                self.from_entity(entity="asiento"),
                self.from_intent(intent="afirmar", value=True),
                self.from_intent(intent="negar", value=False),
            ],
            "preferencias": [
                self.from_intent(intent="negar", value="Sin preferencias adicionales"),
                self.from_text(not_intent="afirmar"),
            ],
            "comentarios": [self.from_entity(entity="comentarios"), self.from_text()],
        }

    # USED FOR DOCS: do not rename without updating in docs
    @staticmethod
    def cocina_db() -> List[Text]:
        """Database of supported cuisines"""

        return [
            "caribeña",
            "china",
            "francesa",
            "griega",
            "india",
            "italiana",
            "mexicana",
        ]

    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    # USED FOR DOCS: do not rename without updating in docs
    def validate_cocina(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate cuisine value."""

        if value.lower() in self.cocina_db():
            # validation succeeded, set the value of the "cocina" slot to value
            return {"cocina": value}
        else:
            dispatcher.utter_message(template="utter_cocina_equivocada")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"cocina": None}

    def validate_numero_personas(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate numero_personas value."""

        if self.is_int(value) and int(value) > 0:
            return {"numero_personas": value}
        else:
            dispatcher.utter_message(template="utter_numero_personas_equivocada")
            # validation failed, set slot to None
            return {"numero_personas": None}

    def validate_asiento_exterior(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validate asiento_exterior value."""

        if isinstance(value, str):
            if "out" in value:
                # convert "out..." to True
                return {"asiento_exterior": True}
            elif "in" in value:
                # convert "in..." to False
                return {"asiento_exterior": False}
            else:
                dispatcher.utter_message(template="utter_asiento_exterior_equivocado")
                # validation failed, set slot to None
                return {"asiento_exterior": None}

        else:
            # affirm/deny was picked up as T/F
            return {"asiento_exterior": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_submit")
        return []
