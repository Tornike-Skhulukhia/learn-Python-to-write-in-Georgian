def geoP(text):
    '''
        Function converts English letters to corresponding Georgian letters, as we type on QWERTY keyboard.
        
        Example of usage:
        
            geoP("Senc SegiZlia!") --> შენც შეგიძლია!
            
    '''
    
    #Define dictionary to store information
    geoLettersDict = {}
    #Georgian letters as we type them
    geoLetters = "a b g d e v z T i k l m n o p J r s t u f q R y S C c Z w W x j h".split(" ")

    #Assign each letter to corresponding georgian letter
    for index,letter in enumerate(geoLetters):
        geoLettersDict[letter] = chr(4304 + index)

    #Result
    returnText = ""
    
    for i in text: #Check each character
        if i in geoLettersDict: #If it is from letters defined before in geoLetters
            returnText += (geoLettersDict[i])   #Add corresponding Georgian letter to final result
            
        else:   #Otherwise, add character directly
            returnText += i
            
    return returnText


def geoA():
    '''
        Returns all Georgian alphabet letters as one string.
    '''
    
    geoLetters = "a b g d e v z T i k l m n o p J r s t u f q R y S C c Z w W x j h".split(" ")
    return( geoP("".join(geoLetters)) )


def geoV():
    '''
        Function to return vowels from Georgian alphabet as one string.
    '''
    vowels = "aeiou"
    
    return( geoP(vowels) )


def geoC():
    
    '''
        Function to return consonants from Georgian alphabet as one string.
    '''
    
    geoLetters = "b g d v z T k l m n p J r s t f q R y S C c Z w W x j h".split(" ")

    return( geoP("".join(geoLetters)) )


