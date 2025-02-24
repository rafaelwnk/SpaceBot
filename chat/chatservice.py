from bot.ai_bot import AIBot

class ChatService:
    def __init__(self):
        self.history_messages = []
        self.bot = AIBot()

    def handle_message(self, user_message):

        bot_response = self.bot.invoke(self.history_messages, user_message)

        self.history_messages.append({"role": "user", "message": user_message})
        self.history_messages.append({"role": "bot", "message": bot_response})

        if len(self.history_messages) > 20: 
            self.history_messages.pop(0)

        return bot_response, self.history_messages[-10:] 
