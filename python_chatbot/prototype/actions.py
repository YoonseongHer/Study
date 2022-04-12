from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

class GetDiagnosis(Action):
    
    def name(self):
        return "get_diagnosis"
    
    def run(self, dispatcher, tracker, domain):
        '''
        type: (Dispatcher, DialogueStateTracker, Domain) -> List(Event)
        '''
        
        tg_num = int(tracker.get_slot('tg_num'))
        print(tg_num)
        
        if tg_num < 150 :
            response = "정상"
        elif tg_num <200 :
            response = "주의"
        else :
            response = "위험"
        
        dispatcher.utter_message(f"고객님의 현재 이상지질혈증 상태는 {response} 입니다.")
        return [SlotSet("tg_num", str(tg_num))]
    
# class SubscribeUser(Action):
#     def name(self):
#         return "subscribe_user"
    
#     def run(self, dispatcher, tracker, domain):
#         '''
#         type: (Dispatcher, DialogueStateTracker, Domain) -> List(Event)
#         '''
        
#         subscribe = tracker.get_slot('subscribe')
        
#         print(subscribe)
        
#         if subscribe == "True":
#             response_ = "You're successfully subscribed"
#         elif subscribe == "False":
#             response_ = "You're successfully unsubscribed"
#         else :
#             response_ = "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
            
#         dispatcher.utter_message(response_)
#         return [SlotSet("subscribe", subscribe)]