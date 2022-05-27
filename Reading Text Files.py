# Read text from a file, and count the occurrence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here 
    with open(r"C:\Users\oyeti\Documents\ZURI\Reading-Text-Files\Reading-Text-Files\story.txt") as file:

        # reading each line	
        for line in file:

	        # reading each word		
	        #for word in line.split():

		        # displaying the words		
	        print(line)
         
read_file_content(r"C:\Users\oyeti\Documents\ZURI\Reading-Text-Files\Reading-Text-Files\story.txt") 

        
def count_words():
# text = read_file_content(r"C:\Users\oyeti\Documents\ZURI\Reading-Text-Files\Reading-Text-Files\story.txt")
    # [assignment] Add your code here
    with open(r"C:\Users\oyeti\Documents\ZURI\Reading-Text-Files\Reading-Text-Files\story.txt") as f:
        words = f.read()
        word_count = {}
        for word in words.replace(',', ' ').split():
            word_count[word] = word_count.setdefault(word, 0) + 1
    print (word_count)

count_words()
    # return {"as": 10, "would": 20}