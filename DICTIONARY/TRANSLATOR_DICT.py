
# Vocabulary source
# English to French dictionary

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

French_to_English = {
    "manger": "to eat",
    "pain": "bread",
    "voiture": "car",
    "ouvrir": "open",
    "ordinateur": "computer"
}

Bulgarian_to_French = {
    "как": "comment",  # kak
    "техники": "techniques",    #tekhniki
    "текст": "texte",    # tekst
    "документ": "document" # dokument
}

French_to_bulgarian = {
    "entrer": "влизам",  #vlizam
    "service": "влизам",  # obsluzhvane
    "language": "език",    # ezik  
    "ouvrir": "отворен"    # otvoren
}

user_word = input("Enter a random word: ").lower()       # gathering inputs from the user and convert them in lower character
if user_word in English_to_French:                       # Condition whether the word choice of the user is in the dictionary
    translation = English_to_French.get(user_word)       # Execute the translation of the user's word
    for word in English_to_French:                       # using the temporary variable "word" to loop through the dictionary        
        English_to_French.get(word) 
    if translation:                                             # Does the user's word exist in the dictionary?        
        print(translation)                                      # if YES, print this line or display the translation of the word
elif user_word in French_to_English:
    translation = French_to_English.get(user_word)
    for word in French_to_English:                              # SAME AS ABOVE
        French_to_English.get(word) 
    if translation:                                                   
        print(translation)                                       
elif user_word in Bulgarian_to_French:
    translation = Bulgarian_to_French.get(user_word)
    for word in Bulgarian_to_French:                             
        Bulgarian_to_French.get(word)                            # SAME AS ABOVE
    if translation:                                                    
        print(translation)                                  
elif user_word in French_to_bulgarian:
    translation = French_to_bulgarian.get(user_word)
    for word in French_to_bulgarian:                            # SAME AS ABOVE
        French_to_bulgarian.get(word) 
    if translation:                                                   
        print(translation)                                      
else:
    print(f"the word {user_word} is not in my memory")         # If none of the above is true, then display this message 






























