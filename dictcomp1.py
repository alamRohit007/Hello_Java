#dictionary comprehension
#square ={1:1, 2:4, 3:9 , 4:16,5:25}

# square ={num:num**2 for num in range(1,11)}
# print(square[2])

# square={f"Square of {num} is":num**2 for num in range(1,11)}
# print(square)

#if you want to print things in different lines
# square={f"Square of {num} is":num**2 for num in range(1,11)}
# for k,v in square.items():
#     print(k,v)
    
#Harshit --> if you want to country how much times the letter is present in string using dictionary comprehension
string="Rohit alam"
#dictionary mein two baar key same nahe hogi iski vjha say huma fayda hoga kyuki character 1 bar he dekhayega ya
word_count={char:string.count(char) for char in string}
print(word_count)
