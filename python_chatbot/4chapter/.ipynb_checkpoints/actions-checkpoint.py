from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetTodaysHoroscope(Action):
    
    def name(self):
        return "get_todays_horoscope"
    
    def run(self, dispatcher, tracker, domain):
        '''
        type: (Dispatcher, DialogueStateTracker, Domain) -> List(Event)
        '''
        
        user_horoscope_sign = tracker.get_slot('horoscope_sign')
        base_url = "http://horoscope-api.herokuapp.com/horoscope/{day}/{sign}"
        url = base_url.format(**{'day':"today", 'sign':user_horoscope_sign})
        res = requests.get(url)
        todays_horoscope = res.json()['horoscope']
        response = f"You today's horoscope:\n{todays_horoscope}"
        
        dispatcher.utter_message(response)
        return [SlotSet("horoscope_sign", user_horoscope_sign)]
    
class SubscribeUser(Action):
    def name(self):
        return "subscribe_user"
    
    def run(self, dispatcher, tracker, domain):
        '''
        type: (Dispatcher, DialogueStateTracker, Domain) -> List(Event)
        '''
        
        subscribe = tracker.get_slot('subscribe')
        
        print(subscribe)
        
        if subscribe == "True":
            response_ = "You're successfully subscribed"
        elif subscribe == "False":
            response_ = "You're successfully unsubscribed"
        else :
            response_ = "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
            
        dispatcher.utter_message(response_)
        return [SlotSet("subscribe", subscribe)]