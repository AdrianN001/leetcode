def word_pattern( s1: str, s2: str ) -> bool: 

    def create_pattern( words: list[str]) -> list[int]: 

        res = [ words.index(x) for x in words ] 

        return res 
    
    return create_pattern( [ x for x in s1 ] ) == create_pattern( s2.split(" ")) 


def main( ) -> None: 

    print(word_pattern("abba", "dog cat cat fish" )) 

main()
