# Import Classes
from chatterbot import ChatBot 
from chatterbot.trainers import ListTrainer
# Create and Train the Chatbot
my_bot = ChatBot(name='PyBot', read_onsly=True, logic_adapter=[
                 'chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])
small_talk = ['hi there', 'hi', 'how do you do', 'how are you',
              'I am cool', 'I\'m fine', 'glad to hear that']
math_talk1 = ['pythagorean theorem', 'a square plus b square equal c square']
math_talk2 = ['law of cosine', 'c**2=a**2+b**2-2*a*b*cos(gamma)']
list_trainer = ListTrainer(my_bot)
for item in (small_talk, math_talk1, math_talk2):
    list_trainer.train(item)
# Communicate with the Python Chatbot
print(my_bot.get_response("hi"))
print(my_bot.get_response("how are you"))
print(my_bot.get_response("pythagorean theorem"))
