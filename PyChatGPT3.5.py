import openai
import webbrowser

def openai_reply(content):
    try:
        apikey =""
        openai.api_key = apikey
        response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=content,
        temperature=0.5,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        )
        #print(response)  #If you need to print out the returned content
        return response.choices[0].message.content
    except Exception as exc:
        if apikey =="":
            url = 'https://platform.openai.com/account/api-keys/'
            webbrowser.open(url)
            return  "You have not configured API Key, please register on the OpenAI website to get it!"
        else:
            #print(exc)  #If it is necessary to print out the cause of the fault
            return "Session failed, please check the network or quota configuration!"

if __name__ == '__main__':
    print("Welcome to ChatGPT 3.5") 
    print("If you want to exit, please enter 'quit'") #Enter "quit" when prompted to terminate the chat
    print("Please enter your question!")
    
    turns = [] #Set a list variable, where turn refers to the turn of the conversation
    
    while True: #Ability to continuously ask questions
        question = input("\nMe：")
        if len(question.strip()) == 0: #If the input is blank, remind me of the input problem
            print("The content is empty, please re-enter.")
        elif question == "quit":  #If the input is "quit", the program terminates
            print("\nAI：Bye bye!")
            break
        else:
            if len(turns) <= 10 :
                turns +=  [{"role": "user", "content": question}]     
                answer = openai_reply(turns)
                print("\nAI：" + answer)
                turns +=  [{"role": "system", "content": answer}]
            else:
                print("\nAI：I don't want to discuss this issue anymore, please ask again!")
                turns = []