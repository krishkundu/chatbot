'''
Created on 20-May-2018

@author: Krishna Gopal Kundu
'''
from rasa_core.actions import Action
from rasa_core.events import SlotSet

class ActionOnUser(Action):
    def name(self):
        return 'action_on_user'

    def run(self, dispatcher, tracker, domain):
        
        username= tracker.get_slot("username")
        actionType= tracker.get_slot("actiontype")
        #c = domain.get
        msg="{} has been successfully {}".format(username,actionType)
        dispatcher.utter_message(msg)
        print(msg)
        return [SlotSet("username", None), SlotSet("actiontype", None)]
