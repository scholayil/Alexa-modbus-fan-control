
import logging

from random import randint

from flask import Flask, render_template

from flask_ask import Ask, statement, question, session

import ifan_interface


app = Flask(__name__)

ask = Ask(app, "/")

#logging.getLogger("flask_ask").setLevel(logging.INFO)
logging.getLogger("flask_ask").setLevel(logging.DEBUG)


def process_response(resp):
    if resp == 0:
        msg = render_template('set')
    else:
        msg = render_template('noresponse')
    return question(msg)


@ask.launch
def launch():
    welcome_msg = render_template('welcome')
    return question(welcome_msg)


@ask.intent("AMAZON.CancelIntent")
@ask.intent("AMAZON.StopIntent")
def ends():
    end_msg = render_template('cancel')
    return statement(end_msg)
@ask.intent("AMAZON.HelpIntent")
def helps():
    msg = render_template('help')
    return question(msg)


@ask.intent("INTENT_IFAN_GetSiteID")
def get_site_id_from_modbus():
    site_id = ifan_interface.get_site_id()
    speech_output = "Your fan site id is " + str(site_id)
    return question(speech_output)


@ask.intent("INTENT_IFAN_Start")
def set_state_start_on_modbus():
    response = ifan_interface.set_start_stop(1)
    return process_response(response)

@ask.intent("INTENT_IFAN_Stop")
def set_state_stop_on_modbus():
    response = ifan_interface.set_start_stop(0)
    return process_response(response)


        
@ask.intent("INTENT_IFAN_PushAirDown")
def set_direction_on_modbus():
    response = ifan_interface.set_direction(1)
    return process_response(response)


@ask.intent("INTENT_IFAN_PushAirUp")
def set_direction_on_modbus():
    response = ifan_interface.set_direction(0)
    return process_response(response)


@ask.intent("INTENT_IFAN_MaxSpeed")
def set_max_speed_on_modbus():
    response = ifan_interface.set_speed(10)
    return process_response(response)


@ask.intent("INTENT_IFAN_MinSpeed")
def set_min_speed_on_modbus():
    response = ifan_interface.set_speed(1)
    return process_response(response)


@ask.intent("INTENT_IFAN_SpeedUp")
def inc_speed_on_modbus():
    response = ifan_interface.inc_dec_speed(1)
    return process_response(response)

@ask.intent("INTENT_IFAN_SpeedDown")
def dec_speed_on_modbus():
    response = ifan_interface.inc_dec_speed(0)
    return process_response(response)




@ask.intent("INTENT_IFAN_Status")
def get_status_on_modbus():
    response = ifan_interface.get_status()
    return process_response(response)


@ask.intent("{}")
def dave():
    msg =  render_template('mainframe')
    return question(msg)




if __name__ == '__main__':

    app.run(debug=True)




    

