import random 

subjects = [
    "Chaiwala",
    "Engineering student",
    "Bollywood actor",
    "Indian mom",
    "Rickshaw driver",
    "Politician’s son",
    "Cricket fan",
    "Tuition teacher",
    "Baba with WiFi",
    "Zomato delivery guy",
    "NRI cousin", 
    "Sarcastic uncle", 
    "Software engineer (WFH)", 
    "Local wedding DJ", 
    "Aunty who offers free advice", 
    "Influencer reviewing street food", 
    "Tired CA student", 
    "Sasta Spiderman", 
    "The colony's best gossip", 
    "A retired government employee" 
]

actions = [
    "declares strike against",
    "gets viral for dancing with",
    "mistakenly proposes to",
    "starts startup with",
    "argues on WhatsApp about",
    "challenges for lassi drinking contest",
    "launches app to replace",
    "blames Mercury retrograde for",
    "writes emotional post about",
    "gets caught taking selfie with",
    "accidentally sends meme to", 
    "develops a secret handshake with", 
    "performs a flash mob dedicated to", 
    "buys a lifetime supply of", 
    "tries to pay with a broken UPI QR code for", 
    "starts a neighborhood turf war over", 
    "claims invention rights to", 
    "attempts a complex yoga pose on top of", 
    "finds life philosophy in" 
]

objects = [ 
    "Delhi Metro gate",
    "coconut vendor",
    "traffic police",
    "government server",
    "Ambani’s dog",
    "IPL trophy",
    "Baba ka ashram",
    "India Gate",
    "canteen samosa",
    "Railway announcement speaker",
    "the society's faulty elevator", 
    "a perfectly round roti", 
    "the neighbor's prize-winning mango tree", 
    "a forgotten remote control", 
    "the office water cooler", 
    "a single tube of fairness cream", 
    "a lost pair of spectacles", 
    "the last slice of pizza", 
    "a perpetually ringing landline phone" 
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    object = random.choice(objects)
    
    print(f'🚨 BREAKING NEWS 🚨 {subject.upper()} {action} {object.upper()}<<<\n')
    
    user_input = input('do you want to continue?(yes/no) :').strip().lower()
    if user_input == "no":
        break
    
print('\n Thanks for using FAKE HEADLINE GENERATOR . Have a great day')