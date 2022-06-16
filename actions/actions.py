# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

from random import randrange
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted, ActionExecuted, EventType

class ActionSessionStart(Action):
    WELCOME_MESSAGES = ["Salut, ma bucur ca ai venit la interviu",
                        "Salutare, bine ai venit la acest training pentru interviuri",
                        "Buna ziua, vine ai venit la training-ul nostru"]

    def name(self) -> Text:
        return "action_session_start"
    
    def run(self, dispatcher: CollectingDispatcher,
                    tracker: Tracker,
                    domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        events = [SessionStarted(), ActionExecuted("action_listen")]
        rand_response_idx = randrange(len(ActionSessionStart.WELCOME_MESSAGES))
        dispatcher.utter_message(text=ActionSessionStart.WELCOME_MESSAGES[rand_response_idx])

        return events