#https://leetcode.com/problems/zigzag-conversion/

def convert( s: str, numRows: int) -> str: 
 
    if numRows == 1 or numRows >= len(s): return s

    collumns = [[] for _ in range( numRows )]

    # Vertical positon of the word
    current_index = -1

    increasing = True
    

    for character in s: 
        current_index = current_index + ( 1 if increasing else -1)

        if current_index == numRows:
            increasing = False
            current_index -= 2
            collumns[current_index].append(character)
        elif current_index == -1:
            increasing = True
            current_index += 2
            collumns[current_index].append(character)
        else: 
            collumns[current_index].append(character)

    res = ""
    for row in collumns:
        res += "".join(row)
    return res




res = convert("PAYPALISHIRING",3)
print(res)