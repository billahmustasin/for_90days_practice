def convert_upper(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs).upper()
    return wrapper

@convert_upper
def show_word(word,word2,word3,{"arg1":"name"}):
    return word

print(show_word("shuvo"))

def remove_punctuations(func):
    def wrapper():
        return func().replace(","," ")
    return wrapper

@remove_punctuations
def take_sentence():
    sent = input("enter a sentence")
    return sent

print(take_sentence())