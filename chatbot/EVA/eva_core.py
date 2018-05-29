'''
Created on 20-May-2018

@author: Krishna Gopal Kundu
'''

import os

#NLU Imports
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.training_data import load_data #remember this
from rasa_nlu.components import ComponentBuilder
from rasa_nlu.model import Trainer
from rasa_nlu import config


#Core imports
from rasa_core.channels.console import ConsoleInputChannel
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_core.agent import Agent
from rasa_core.policies.memoization import MemoizationPolicy
from rasa_core.policies.keras_policy import KerasPolicy


'''Train the NLU Model and return the model directory where
   trained nlu is persisted
'''
def train_nlu_mode( 
                   nlu_train_file="/nlu_train_data/testData.json",
                   nlu_config_file="/nlu_model/config_spacy.yml",
                   nlu_persist_dir="/nlu_model",
                   nlu_model_name="evanlu"):
    
    # will cache components between pipelines (where possible)
    builder = ComponentBuilder(use_cache=True)
    
    training_data = load_data(add_cur_dir(nlu_train_file))
    #trainer = Trainer(RasaNLUModelConfig(add_cur_dir(nlu_config_file)), builder)
    trainer = Trainer(config.load(add_cur_dir(nlu_config_file)), builder)
    
    trainer.train(training_data)
    
    model_directory = trainer.persist(add_cur_dir(nlu_persist_dir), fixed_model_name=nlu_model_name)
    return model_directory
    pass


'''
Utility method 
'''
def add_cur_dir(loc):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return dir_path + loc
    pass

'''
   Train the core bot agent
'''
def get_nlu_agent(
                     interpreter,
                     domain_file="domain/data/domain.yml",
                     model_path="domain/dialogue",
                     training_data_file="domain/data/stories.md",
                     mode="OFFLINE"):

    if os.path.exists(add_cur_dir("/"+model_path)):
        print("Loading Agent")
        agent = Agent.load(add_cur_dir("/"+model_path), interpreter=interpreter)
        return agent
    else:
        print("Training Agent")
        agent = Agent(add_cur_dir("/"+domain_file), policies=[MemoizationPolicy(max_history=3),KerasPolicy()],
                                            interpreter=interpreter
                                            )
        training_data = agent.load_data(add_cur_dir("/"+training_data_file))
        if mode == "OFFLINE":
            agent.train(
                    training_data,
                    #augmentation_factor = 50,
                    #max_history = 4, feature disabled
                    epochs = 100,
                    batch_size = 20,
                    validation_split = 0.2
            )
        
        else:
            agent.train_online(training_data,
                             ConsoleInputChannel(),
                             #augmentation_factor = 50,
                             #max_history = 4,
                             epochs = 100,
                             batch_size = 50,
                             validation_split = 0.2
                            )
        
        agent.persist(model_path)
        return agent
    pass

def get_nlu_interpreter(nlu_persist_dir="/nlu_model",
                        nlu_model_name="evanlu",
                        ):
    nlu_dir = nlu_persist_dir + "/default/"+nlu_model_name
    
    if(os.path.exists(add_cur_dir(nlu_dir))):
        print("Loading Interpreter")
        return    RasaNLUInterpreter(add_cur_dir(nlu_dir))
    else:
        model = train_nlu_mode()
        print("Training Interpreter")
        print("nlu model dir :"+model)
        #self.nlu_interpreter = Interpreter.load(model, builder)
        return RasaNLUInterpreter(model)
    
    pass

class Eva(object):
    
    nlu_interpreter = get_nlu_interpreter()
    nlu_agent = get_nlu_agent(nlu_interpreter, mode="OFFLINE")

    '''
        Wrapper method to interact with EVA
    '''
    @classmethod
    def handle_request(self, req_text, sender_id):
        return self.nlu_agent.handle_message(req_text, sender_id=sender_id)
        pass

    '''
        Initialize EVA 
            - initializes the NLU Interpreter 
            - loads the bot dialogue module
            - ready state to be tested
    '''
    def __init__(self,nlu_interpreter=None,  mode="OFFLINE"):
        '''
        Constructor
        '''
        pass
    pass