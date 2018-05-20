from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

from eva_core import Eva

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
	#####################################################################################
	# __bot = ChatBot('PLM BOT', 														#
	# 				#read_only=True,													#
	# 				logic_adapters=[													#
	# 					"chatterbot.logic.BestMatch",									#
	# 					"chatterbot.logic.MathematicalEvaluation",						#
	# 					"chatterbot.logic.LowConfidenceAdapter"							#
	# 				],																	#
	# 				input_adapter='chatterbot.input.VariableInputTypeAdapter',			#
	# 				output_adapter='chatterbot.output.OutputAdapter'					#
	#																					#
	# 	)																				#
	#####################################################################################
	__bot = ChatBot('PLM BOT', 
					#read_only=True,
					filters=["chatterbot.filters.RepetitiveResponseFilter"],
					preprocessors=[
									'chatterbot.preprocessors.clean_whitespace',
									'chatterbot.preprocessors.unescape_html',
									'chatterbot.preprocessors.convert_to_ascii'
								],
					logic_adapters=[
						{
							"import_path": "chatterbot.logic.BestMatch",
							"statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
							"response_selection_method": "chatterbot.response_selection.get_first_response"
						},
						{
							"import_path": "chatterbot.logic.MathematicalEvaluation",
						},
						{
							'import_path': 'chatterbot.logic.SpecificResponseAdapter',
							'input_text': 'Help me!',
							'output_text': 'Ok, here is a link: http://chatterbot.rtfd.org'
						},
						{
							'import_path': 'chatterbot.logic.LowConfidenceAdapter',
							'threshold': 0.65,
							'default_response': 'I am sorry, but I do not understand.'
						}

					],
					input_adapter='chatterbot.input.VariableInputTypeAdapter',
					output_adapter='chatterbot.output.OutputAdapter'

		)
	__instance = None

	def __init__(self, name):
		print("Init Method is called")

		self.__bot = ChatBot('PLM BOT', 
					#read_only=True,
					filters=["chatterbot.filters.RepetitiveResponseFilter"],
					logic_adapters=[
						{
							"import_path": "chatterbot.logic.BestMatch",
							"statement_comparison_function": "chatterbot.comparisons.levenshtein_distance",
							"response_selection_method": "chatterbot.response_selection.get_first_response"
						},
						{
							"import_path": "chatterbot.logic.MathematicalEvaluation",
						},
						{
							'import_path': 'chatterbot.logic.SpecificResponseAdapter',
							'input_text': 'Help me!',
							'output_text': 'Ok, here is a link: https://www.tcs.com'
						},
						{
							'import_path': 'chatterbot.logic.LowConfidenceAdapter',
							'threshold': 0.65,
							'default_response': 'I am sorry, but I do not understand.'
						}
						

					],
					input_adapter='chatterbot.input.VariableInputTypeAdapter',
					output_adapter='chatterbot.output.OutputAdapter'

		)
		#self.__bot.set_trainer(ListTrainer)
		#self.__bot.train(conversation)
		self.__bot.set_trainer(ChatterBotCorpusTrainer)
		#Now train with corporus
		# Train based on the english corpus
		#self.__bot.train("chatterbot.corpus.english")
		# Train based on english greetings corpus
		self.__bot.train("chatterbot.corpus.english.greetings")
		# Train based on the english conversations corpus
		#self.__bot.train("chatterbot.corpus.english.conversations")
		# Now we can export the data to a file
		#self.__bot.trainer.export_for_training('./chat_op_sample.json')
		#Train on custom dataset which is also a corpus
		self.__bot.train(
			"./train_data/enovia_train.yml",
			"./train_data/bot_profile.yml",
		)



	@classmethod    
	def generate_response(self,request):
		return self.__bot.get_response(request)
		pass

#plm_chat_bot = ModelChatBot('PLM BOT')
plm_chat_bot = Eva()
def get_chat_resonse(re_txt,id):
	plm_chat_bot.handle_request(re_txt, sender_id=id)


