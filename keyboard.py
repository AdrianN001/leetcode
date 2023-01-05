#return all the word that can be written in 1 keyboard row (like "wet")

def findWords( words: list ) -> list: 
    keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    res = []

    for szo in words: 
        for row in keyboard_rows: 
            
            for karakter in szo.lower(): 

                if karakter not in row: 
                    break
            else: 
                res.append(szo)
                break
    return res

print( findWords( ["Hello","Alaska","Dad","Peace"] ) )
