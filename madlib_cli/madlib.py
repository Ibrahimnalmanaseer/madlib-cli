import re

def welcome():

    '''
    :print: game's welcome message 
    
    '''
    print( 
         
    '''
    
    ###               Welcome to Mad libs game                  ###
    ***  Mad libs is a funny game , place your words in a story ***
    ***       Please answer the questions and press Enter       ***     
              
    ''')



def user_input_dark():
    '''
    :return: tuple of user inputs 

    '''

    adj_1 = input("Adjective ==> ")
    adj_2 = input("Adjective ==> ")
    noun = input("Noun ==> ")
    return(adj_1,adj_2,noun)



def user_input_story():

    '''
    :return: tuple of user inputs 

    '''

    adj_1 = input("Adjective ==> ")
    adj_2 = input("Adjective ==> ")
    first_name_1 = input("First Name ==> ")
    past_verb = input("Past Tense Verb==> ")
    first_name_1 = input("First Name ==> ")
    adj_3 = input("Adjective ==> ")
    adj_4 = input("Adjective ==> ")
    plural_noun_1 = input("Plural Noun ==> ")
    large_animal = input("Large Animal ==> ")
    small_animal = input("Small Animal ==> ")
    girl_name = input("Girl Name ==> ")
    adj_5 = input("Adjective ==> ")
    plural_noun_2 = input("Plural Noun ==> ")
    adj_6 = input("Adjective ==> ")
    plural_noun_3 = input("Plural Noun ==> ")
    number_1 = input("Number from 1 - 50 ==> ")
    first_name_2 = input("First Name ==> ")
    number_2 = input("Number 1 - 50 ==> ")
    plural_noun_4 = input("Plural Noun ==> ")
    number_3 = input("Number 1 - 50 ==> ")
    plural_noun_5 = input("Plural Noun ==> ")
  



    return(adj_1,adj_2,first_name_1,past_verb,first_name_1,adj_3,adj_4,plural_noun_1,large_animal,small_animal,girl_name,adj_5,plural_noun_2,adj_6,plural_noun_3,number_1,first_name_2,number_2,plural_noun_4,number_3,plural_noun_5)

def read_template(path):
    '''
    :param file path
    :return : file content    
    
    '''

    with open(path) as file:

            content=file.read()
            return content

    
def parse_template(content):

    '''
    :param string 
    :return : string stripped of values that inside curly brackets
    :return : tuple of stripped values
    
    '''
    stripped=re.sub("\{.*?\}","{}",content)
    parts = re.findall('{(.+?)}',content)
   
    return [stripped,tuple(parts)]




def merge(stripped,value):

    '''
    :param string with empty curly brackets
    :param tuple
    :return : merge tuple items inside a string
    
    '''

    data=stripped.format(*value)

    return data


def write_response(paragraph):
    
    
    '''
    :param string
   
    :return : create and write in file, print file content
    
    '''



    with open('./assets/response.txt','w') as file:

        file.write(paragraph)
    with open('./assets/response.txt','r') as f:
        print (f'\n*********************************************\n {f.read()}')



welcome()

write_response(merge(parse_template(read_template('./assets/story.txt'))[0],user_input_story()))