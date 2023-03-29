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
        #print(response)  #如果需要打印出返回内容
        return response.choices[0].message.content
    except Exception as exc:
        if apikey =="":
            url = 'https://platform.openai.com/account/api-keys/'
            webbrowser.open(url)
            return  "您没有配置apikey，请在OpenAI网站注册获取！"
        else:
            #print(exc)  #如果需要打印出故障原因
            return "会话失败，请检查网络或限额配置！"

if __name__ == '__main__':
    print("欢迎使用 ChatGPT 3.5") 
    print("如果您想退出，请输入'quit'") #提示想终止聊天时输入"quit"
    print("") 
    print("请输入您的问题吧！")
    print("") 
      
    turns = [] #设置一个list变量，turn指对话时的话轮
    
    while True: #能够连续提问  
        question = input("我：")
        if len(question.strip()) == 0: #如果输入为空，提醒输入问题
            print("内容是空的，请重新输入。")
        elif question == "quit":  #如果输入为"quit"，程序终止
            print("\nAI：下次见了!")
            break
        else:
            if len(turns) <= 10 :
                turns +=  [{"role": "user", "content": question}]     
                answer = openai_reply(turns)
                print("AI：" + answer)
                turns +=  [{"role": "system", "content": answer}]
            else:
                print("AI：我不想再讨论这个问题了，请重新提问！")
                turns = []