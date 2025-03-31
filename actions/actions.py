# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict

### Ngl, I could potentially have the same action server for two bots, and just write two alternate functions -> and one chatbot calls 
### ActionCalculatePostageHigh (for high anthro) and the other have ...Low (for low anthro)
### Can't have the same action server for all 4 because of the ValidatePostageForm class -> and even if I could work around it, I think I will have separate 
### servers just for correctness and debugging ease
class ActionCalculatePostage(Action):
    def name(self) -> Text:
        return "action_calculate_postage"
    
    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        postage_size = tracker.get_slot("postage_size")
        first_class = tracker.get_slot("first_class")

        post_cost = 0

        match postage_size:
            case "Small":
                post_cost = 4.85 if first_class else 3.25
            case "Medium":
                post_cost = 5.60 if first_class else 4.85
            case "Large":
                post_cost = 7.20 if first_class else 6.50
        
        cost_message = f"Perfect! So just to summarise, you have a {postage_size} parcel that you wish to send using {'1st' if first_class else '2nd'} Class Postage. \n\n The total cost would be £{post_cost:.2f}"

        dispatcher.utter_message(cost_message)
        return []

class ActionCalculatePostageLow(Action):
    def name(self) -> Text:
        return "action_calculate_postage_low"
    
    def run(self, dispatcher: CollectingDispatcher, tracker, domain):
        postage_size = tracker.get_slot("postage_size")
        first_class = tracker.get_slot("first_class")

        post_cost = 0

        match postage_size:
            case "Small":
                post_cost = 4.85 if first_class else 3.25
            case "Medium":
                post_cost = 5.60 if first_class else 4.85
            case "Large":
                post_cost = 7.20 if first_class else 6.50
        
        cost_message = f"Summary: A {postage_size} parcel to be sent with {'1st' if first_class else '2nd'} Class Postage. \n\n Total cost: £{post_cost:.2f}"

        dispatcher.utter_message(cost_message)
        return []