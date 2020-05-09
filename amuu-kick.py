print ("""
Working.
@muuT3ra$$uu-kick-me-plz
#FuckAllEverything. 
by Tripl_color vk.com/Tripl_color""")
import vk_requests
import time
myid = "Твой айди"
myid2 = "Айди мульта"
cid = str(input('Айди беседы = '))

tokencom = 'токен мульта'


api = vk_requests.create_api(service_token=tokencom)  
print(api.messages.addChatUser(chat_id= cid, user_id= myid2))

api = vk_requests.create_api(service_token=tokencom)  
print(api.messages.addChatUser(chat_id= cid, user_id= myid))

api = vk_requests.create_api(service_token=tokencom)  
print(api.messages.removeChatUser(chat_id= cid, user_id= myid2))

