import re



def read_template():

    print ('Welcome to madlib game')

# It was a {Adjective} and {Adjective} {Noun}.

# I the {Adjective} and {Adjective} {A First Name} have {Past Tense Verb} {A First Name}'s {Adjective} sister and plan to steal her {Adjective} {Plural Noun}!

# What are a {Large Animal} and backpacking {Small Animal} to do? Before you can help {A Girl's Name}, you'll have to collect the {Adjective} {Plural Noun} and {Adjective} {Plural Noun} that open up the {Number 1-50} worlds connected to A {First Name}'s Lair. There are {Number} {Plural Noun} and {Number} {Plural Noun} in the game, along with hundreds of other goodies for you to find.

def user_input_dark():


    adj_1 = input("Adjective ==> ")
    adj_2 = input("Adjective ==> ")
    noun = input("Noun ==> ")
    return(adj_1,adj_2,noun)


def user_input_story():


    adj_1 = input("Adjective ==> ")
    adj_2 = input("Adjective ==> ")
    first_name_1 = input("First Name ==> ")
    past_verb = input("Past Tense Verb==> ")
    first_name_1 = input("First Name ==> ")
    adj_3 = input("Adjective ==> ")
    adj_4 = input("Adjective ==> ")
    plural_noun = input("Plural Noun ==> ")
    
def read_template(path):

    if path == False:

        print('not found ')

    try:
        with open(path) as file:

            content=file.read()
            return content

    except FileNotFoundError:

        return 'file not found'

# read_template('./assets/dark_and_stormy_night_template.txt')





def parse_template(content):

   
    stripped=re.sub("\{.*?\}","{}",content)
    parts = re.findall('{(.+?)}',content)
   
    return [stripped,tuple(parts)]

# parse_template("It was a {Adjective} and {Adjective} {Noun}.")

# print(parse_template(read_template('./assets/dark_and_stormy_night_template.txt'))[0])


def merge(stripped,value):

    data=stripped.format(*value)

    return data

merge(parse_template(read_template('./dark_and_stormy_night_template.txt'))[0],user_input_dark())