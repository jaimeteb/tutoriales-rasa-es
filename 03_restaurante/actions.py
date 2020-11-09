from typing import Dict, Text, Any, List, Union, Optional

from rasa_sdk import Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction


class RestaurantForm(FormAction):
    """Ejemplo de una acción de tipo form"""

    def name(self) -> Text:
        """Nombre de la form"""

        return "restaurante_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """Lista de los slots que se tienen que llenar para la form"""

        return ["cocina", "numero_personas", "asiento_exterior", "preferencias", "comentarios"]

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """Un diccionario que relaciona los slots requeridos con
            - una entidad extraída
            - pares intent-valor
            - un mensaje completo
            o una lista de estos, donde la primer coincidencia se conserva"""

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

    @staticmethod
    def cocina_db() -> List[Text]:
        """Base de datos de tipos de cocina soportados"""

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
        """Probar si un texto es un entero"""

        try:
            int(string)
            return True
        except ValueError:
            return False

    def validate_cocina(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validación de los valores de cocina"""

        if value.lower() in self.cocina_db():
            # validación exitosa, se guarda el valor de "cocina"
            return {"cocina": value}
        else:
            dispatcher.utter_message(template="utter_cocina_equivocada")
            # validación fallida, se devuelve el valor None, lo cual
            # hará que se vuelva a preguntar por el valor
            return {"cocina": None}

    def validate_numero_personas(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validación de numero de personas"""

        if self.is_int(value) and int(value) > 0:
            return {"numero_personas": value}
        else:
            dispatcher.utter_message(template="utter_numero_personas_equivocada")
            # validación fallida, se devuelve el valor None
            return {"numero_personas": None}

    def validate_asiento_exterior(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
        """Validación de asiento exterior"""

        if isinstance(value, str):
            if "fuera" in value:
                # convertir "fuera..." a True
                return {"asiento_exterior": True}
            elif "dentro" in value:
                # convertir "dentro..." a False
                return {"asiento_exterior": False}
            else:
                dispatcher.utter_message(template="utter_asiento_exterior_equivocado")
                # validación fallida, se devuelve el valor None
                return {"asiento_exterior": None}

        else:
            # afirmar/negar se convierte en True/False
            return {"asiento_exterior": value}

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Definir lo que se hace cuando se han llenado
        todos los slots requeridos"""

        dispatcher.utter_message(template="utter_submit")
        return []
