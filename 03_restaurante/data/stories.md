## camino feliz
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## camino infeliz
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* charla
    - utter_charla
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## camino muy infeliz
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* charla
    - utter_charla
    - restaurante_form
* charla
    - utter_charla
    - restaurante_form
* charla
    - utter_charla
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## detenerse pero continuar
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* detener
    - utter_ask_continuar
* afirmar
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## detenerse por completo
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* detener
    - utter_ask_continuar
* negar
    - action_deactivate_form
    - form{"name": null}

## charla, detenerse pero continuar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* charla
    - utter_charla
    - restaurante_form
* detener
    - utter_ask_continuar
* afirmar
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## detenerse pero continuar y charla
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* detener
    - utter_ask_continuar
* afirmar
    - restaurante_form
* charla
    - utter_charla
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## charla pero continuar y charla
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* charla
    - utter_charla
    - restaurante_form
* detener
    - utter_ask_continuar
* afirmar
    - restaurante_form
* charla
    - utter_charla
    - restaurante_form
    - form{"name": null}
    - utter_valores_slots
* gracias
    - utter_denada

## charla y detenerse por completo
* saludar
    - utter_saludar
* solicitar_restaurante
    - restaurante_form
    - form{"name": "restaurante_form"}
* charla
    - utter_charla
    - restaurante_form
* detener
    - utter_ask_continuar
* negar
    - action_deactivate_form
    - form{"name": null}

## reto bot
* reto_bot
  - utter_soybot
