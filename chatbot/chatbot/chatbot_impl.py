from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer


conversation = [
"Hello",
"Hi there!",
"How are you doing?",
"I'm doing great.",
"That is good to hear",
"Thank you.",
"You're welcome."
]



class ModelChatBot:
    __bot = ChatBot('PLM BOT')
    def __init__(self, name):
        self.__bot = ChatBot(name)
        self.__bot.set_trainer(ListTrainer)
        self.__bot.train(conversation)
    @classmethod    
    def generate_response(self,request):
        return self.__bot.get_response(request)
    pass


