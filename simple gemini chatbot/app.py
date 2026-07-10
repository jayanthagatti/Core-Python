#use google gemini using python
import google.generativeai as genai

API_KEY="AIzaSyA7TT0BK2HI87qJHTGfcXS-iGKDApso55U"
genai.configure(api_key=API_KEY)

model=genai.GenerativeModel("gemini-2.0-flash")
chat=model.start_chat()

# response=chat.send_message("hello")
# print("Gemini: ",response.text)
print("Chat with Gemini! Type 'exit' to quit.")
while True:
    user_input=input("You: ")
    if user_input.lower() == 'exit':
        break
    response=chat.send_message(user_input)
    print("Gemini:",response.text)
