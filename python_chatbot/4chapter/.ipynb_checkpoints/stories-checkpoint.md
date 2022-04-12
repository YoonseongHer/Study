## Generated Story -5910613723556367086
* greeting
    - utter_greet
* get_horoscope
    - utter_ask_horoscope_sign
* get_horoscope{"horoscope_sign": "Capricorn"}
    - slot{"horoscope_sign": "Capricorn"}
    - get_todays_horoscope
    - slot{"horoscope_sign": "Capricorn"}
    - utter_subscribe
* subscription
    - subscribe_user
    - action_default_fallback
    - rewind

