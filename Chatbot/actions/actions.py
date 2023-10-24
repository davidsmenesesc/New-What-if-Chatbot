from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import os
import time

class ActionShowModels(Action):

    def name(self) -> Text:
        return "action_show_models"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # code to fetch models from /inputs folder and store in 'models' list
        models = os.listdir('inputs/')
        print(models)

        # Create a numbered list of models
        numbered_models = {i+1: model for i, model in enumerate(models)}
        print(numbered_models)

        # Send the numbered list to the user
        for number, model in numbered_models.items():
            dispatcher.utter_message(text=f"{number}: {model}")
            # Add a small delay
            time.sleep(0.5)

        #dispatcher.utter_message(response="utter_ask_model")
        dispatcher.utter_message(text="Please choose a model from the list above by entering its number.")

        # Save the numbered_models dictionary into a slot for later use
        return [SlotSet("numbered_models", numbered_models)]