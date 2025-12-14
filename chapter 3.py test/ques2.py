letter = ''' Dear <|Name|>,
         You are selected!
         <|Date|>'''

print(letter.replace("<|Name|>", "Himanshu").replace("<|Date|", "23 april 2097"))
