def convertInputString():
    rawInput = input("\nPor favor ingrese palabra, frase u oracion \npara verificar si es un palindromo: ") 
    rawString = rawInput.lower() 
    rawList = list(rawString) 
    return rawList

def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    return dirtyList 

def runPalindromeCheck(straightList):
    reversedList = straightList[::-1] 
    if reversedList == straightList: 
        return "El texto ingresado es un Palindromo!" 
    else: 
        return "El texto ingresado no es un palindromo." 

def main(): 
    print("\nVerificador de palindromos") 
    originalList = convertInputString()  
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

main() 