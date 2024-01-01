# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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
import time

paper = ["blue", "Blue", "recycle", "Recycle"]
cardboard = ["blue", "Blue", "recycle", "Recycle"]
plastic = ["blue", "Blue", "recycle", "Recycle"]
polythene = ["orange", "non recycle", "Non Recycle"]


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
import requests


class ActionGetValue(Action):
    # answer = tracker.get_slot('answer')

    def name(self) -> Text:
        return "action_get_value"

    def run(self, dispatcher, tracker, domain):
        answer = tracker.get_slot('answer')
        value = requests.get(
            "http://127.0.0.1:8000/getdatas").json()
        print(value)
        if value == answer:
            # dispatcher.utter_message(value)
            dispatcher.utter_message(f"yes it is  a {answer},  what is the bin that {answer} trash put into")
            print("right")
            return [SlotSet('answer', value)]
        elif answer == "None":
            print(answer)
            dispatcher.utter_message(f"Can you please show the trash to the camera")
            print("None")
            return [SlotSet('answer', None)]

        else:
            print(answer)
            dispatcher.utter_message(f"it is not a {answer}  try again")
            print("wrong")
            return [SlotSet('answer', None)]

    # dispatcher.utter_message(value)


class ActionCheckBin(Action):
    def name(self) -> Text:
        return "action_check_bin"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        answer = tracker.get_slot('answer')
        bin = tracker.get_slot('bin')

        if answer == "paper":
            if bin in paper:
                set = requests.get("http://127.0.0.1:8000/setvids/2")
                dispatcher.utter_message(
                    f"you are right ,well done ,{answer}trash are {paper[2]}, and goes to {paper[0]} color bin")
                time.sleep(4)
                response = requests.get("http://127.0.0.1:8000/setdata/1")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', bin)]
            else:
                set = requests.get("http://127.0.0.1:8000/setvids/3")
                time.sleep(4)
                dispatcher.utter_message(
                    f"It is not {bin}, {answer} are {paper[2]},its goes to {paper[2]} bin {paper[0]} color one")
                set = requests.get("http://127.0.0.1:8000/setvids/2")
                response = requests.get("http://127.0.0.1:8000/setdata/1")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', paper[2])]
        elif answer == "cardboard":
            if bin in cardboard:
                set = requests.get("http://127.0.0.1:8000/setvids/2")
                dispatcher.utter_message(
                    f"you are right ,well done ,{answer}trash are {cardboard[2]}, and goes to {cardboard[0]} color bin")
                time.sleep(4)
                response = requests.get("http://127.0.0.1:8000/setdata/1")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', bin)]
            else:
                set = requests.get("http://127.0.0.1:8000/setvids/3")
                time.sleep(4)
                dispatcher.utter_message(
                    f"It is not {bin}, {answer} are {cardboard[2]},its goes to {cardboard[2]} bin {cardboard[0]} color one")
                response = requests.get("http://127.0.0.1:8000/setdata/1")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', cardboard[2])]
        elif answer == "polythene":
            if bin in polythene:
                set = requests.get("http://127.0.0.1:8000/setvids/1")
                dispatcher.utter_message(
                    f"you are right ,well done ,{answer}trash are {polythene[2]}, and goes to {polythene[0]} color bin")
                time.sleep(4)
                response = requests.get("http://127.0.0.1:8000/setdata/2")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', bin)]
            else:
                set = requests.get("http://127.0.0.1:8000/setvids/3")
                time.sleep(4)
                dispatcher.utter_message(
                    f"It is not {bin}, {answer} are {polythene[2]},its goes to {polythene[2]} bin {polythene[0]} color one")
                set = requests.get("http://127.0.0.1:8000/setvids/1")
                response = requests.get("http://127.0.0.1:8000/setdata/2")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', polythene[2])]
        elif answer == "plastic":
            if bin in plastic:
                set = requests.get("http://127.0.0.1:8000/setvids/2")
                dispatcher.utter_message(
                    f"you are right ,well done ,{answer}trash are {plastic[2]}, and goes to {plastic[0]}color bin")
                time.sleep(4)
                response = requests.get("http://127.0.0.1:8000/setdata/1")
                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', bin)]
            else:
                set = requests.get("http://127.0.0.1:8000/setvids/3")
                time.sleep(4)

                dispatcher.utter_message(
                    f"It is not {bin}, {answer} are {plastic[2]},its goes to {plastic[2]} bin {plastic[0]} color one")
                response = requests.get("http://127.0.0.1:8000/setdata/1")

                set = requests.get("http://127.0.0.1:8000/setvids/0")
                return [SlotSet('bin', plastic[2])]


class ActionTimeout(Action):
    def name(self) -> Text:
        return "action_timeout"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Send the response for timeout
        dispatcher.utter_message("Sorry, I didn't receive any answer. Can you please provide a response?")

        # Reset slots to start a new conversation
        return [AllSlotsReset()]


class ClearSlotsAction(Action):
    def name(self):
        return "action_clear_slots"

    def run(self, dispatcher, tracker, domain):
        return [SlotSet("answer", None), SlotSet("bin", None)]


class ActionRepeatRequest(Action):
    def name(self) -> Text:
        return "action_repeat_request"

    def run(
            self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_ask_rephrase")
        return []


class ActionFallback(Action):
    def name(self) -> Text:
        return "action_fallback"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Sorry, I didn't receive any answer. Can you please provide a response?")
        return []


class CustomAction(Action):
    def name(self) -> Text:
        return "action_custom_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        user_input = tracker.latest_message.get('text')

        if not user_input:
            # Handle empty user response
            response = "Sorry, I didn't receive any input. Can you please repeat?"
        else:
            # Handle other fallback cases
            response = "Sorry, I didn't understand. Can you please rephrase or provide more information?"

        dispatcher.utter_message(text=response)

        return []
