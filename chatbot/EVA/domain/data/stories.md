## story_greet
* intent_greet
 - utter_greet

## story_bye
* intent_bye
 - utter_goodbye

## story_user_issue 001
* intent_user_issue
 - utter_ask_more_info

## story_user_issue 001
* intent_thanks
 - utter_thanks

## story_user_issue 062
* intent_user_issue{"actiontype": "deactivate"}
 - slot{"actiontype":"deactivate"}
 - utter_ask_username

## story_user_issue 042
* intent_user_issue{"actiontype": "activate"}
 - slot{"actiontype":"activate"}
 - utter_ask_username

## story_user_issue 032
* intent_user_issue{"username" :"647229"}
 - slot{"username": "647229"}
 - utter_ask_actiontype

## story_user_issue 022
* intent_user_issue{"username" :"65889922"}
 - slot{"username": "65889922"}
 - utter_ask_actiontype

## story_user_issue 012
* intent_user_issue{"username" :"8745662"}
 - slot{"username": "8745662"}
 - utter_ask_actiontype

## story_user_issue 101
* intent_user_issue{"actiontype": "activate","username": "72727819"}
 - slot{"username": "72727819", "actiontype":"activate"}
 - utter_ask_confirm
* intent_affirm
 - utter_on_it
 - action_on_user

## story_user_issue 102
* intent_user_issue{"actiontype": "activate","username": "2213332"}
 - slot{"username": "2213332", "actiontype":"activate"}
 - utter_ask_confirm
* intent_affirm
 - utter_on_it
 - action_on_user

## Generated Story -2820410962187969097
* intent_greet
 - utter_greet
* intent_user_issue{"actiontype": "activate"}
 - slot{"actiontype": "activate"}
 - utter_ask_username
* intent_greet{"username": "9393939"}
 - slot{"username": "9393939"}
 - utter_ask_confirm
* intent_affirm
 - utter_on_it
 - action_on_user
 - slot{"username": null}
 - slot{"actiontype": null}
* intent_bye
 - utter_goodbye
 - export

## Generated Story -4247133225434372286
* intent_greet
 - utter_greet
* intent_user_issue
 - utter_ask_more_info
* intent_user_issue{"username": "645677"}
 - slot{"username": "645677"}
 - utter_ask_actiontype
* intent_user_issue{"actiontype": "enabled"}
 - slot{"actiontype": "enabled"}
 - utter_ask_confirm
* intent_affirm
 - utter_on_it
 - action_on_user
 - slot{"username": null}
 - slot{"actiontype": null}
* intent_thanks
    - utter_thanks
* intent_bye
    - utter_goodbye
    - export
