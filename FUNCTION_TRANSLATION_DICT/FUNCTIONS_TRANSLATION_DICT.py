
def larousse(translate_english):
    if user_word in translate_english:                      
        translation = translate_english.get(user_word)    
        for word in translate_english:                     
            translate_english.get(word) 
        if translation:                                                   
            print(translation) 

def oxford(translate_bulgarian):
    if user_word in translate_bulgarian:
        translation = translate_bulgarian.get(user_word)
        for word in translate_bulgarian:                             
            translate_bulgarian.get(word)                            
        if translation:                                                    
            print(translation)   

def webster(translate_french):
    if user_word in translate_french:
        translation = translate_french.get(user_word)
        for word in translate_french:                              
            translate_french.get(word) 
        if translation:                                                   
            print(translation)  

def thesauraus(french_translation):
    if user_word in french_translation:
        translation = french_translation.get(user_word)
        for word in french_translation:                          
            french_translation.get(word) 
        if translation:                                                   
            print(translation)  

English_to_French = {
    "why":"pourquoi",
    "goodbye": "Au revoir",
    "good morning": "bonjour",
    "to know": "savoir",
    "if": "si",
    "you": ["tu", "vous", "toi"],   
    "person": "personne",
    "prune": "plum"
    }

Bulgarian_to_French = {
    "как": "comment",  # kak
    "техники": "techniques",    #tekhniki
    "текст": "texte",    # tekst
    "документ": "document" # dokument
}

French_to_English = {
    "manger": "to eat",
    "pain": "bread",
    "voiture": "car",
    "ouvrir": "open",
    "ordinateur": "computer"
}
French_to_Bulgarian = {
    "entrer": "влизам",  #vlizam
    "service": "обслужване",  # obsluzhvane
    "language": "език",    # ezik  
    "lancer": "хвърлям"    # khvŭrlyam
}

user_word = input("Enter a random word: ").lower() 

if user_word in English_to_French:
    larousse(English_to_French)
elif user_word in Bulgarian_to_French:
    oxford(Bulgarian_to_French)
elif user_word in French_to_English:
    webster(French_to_English)
elif user_word in French_to_Bulgarian:
    thesauraus(French_to_Bulgarian)
else:
    print(f"the word {user_word} is not in my memory")








    







