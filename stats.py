def numberofWords(filepath):
    with open(filepath) as f:
        filecontent = f.read()
    

    return len(filecontent.split())


freq = {}
def charnumbers(filepath): 
  
    with open(filepath) as f:
        filecontent = f.read()
    for c in filecontent.lower():
        if c in freq:
            freq[c] +=1
        else:
            freq[c] = 1

    return freq
def dictPrint():
    for i, v in freq.items():
        if str(i).isalpha():
            print(f"{i}:",v)



