text = "Football is the most popular sport. It unites billions of fans worldwide. This beautiful game showcases raw talent. Professional players train relentlessly for glory. Passionate supporters fill massive stadiums. Tournaments like the World Cup bring people together. The sport is a massive global industry. It creates international football legends. Football is a true way of life. It teaches teamwork and fair play."
words = text.split()
print(f"numbers of words is : {len(words)} ") # to count the number of words in the text 

letters_only = len(text.replace(" ","").replace(".","")) # to count the number of letters in the text by removing spaces and periods
print(f"number of letters is : {letters_only}") 

sentences_only = text.replace(" ","").count(".") # to count the number of sentences in the text by counting the periods
print(f"number of sentences is : {sentences_only}")
