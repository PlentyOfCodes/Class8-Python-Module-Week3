'''
Assignment 4
Create a user interface that generates a random password with the given user input
such as length, number of lowercase letters and uppercase letters 
and adding special characters(!,?, .,etc.)

'''
import random
import string

def input_taking (str="password"):
     while True:
        lenght=input(f'Please write lenght of your {str} you want to generate.\n')
        lenght_upper=input(f'Please write number of contained uppercase characters.\n')
        lenght_lower=input(f'Please write number of contained lowecase characters.\n') 
        #special_character=input(f'Please write True or False wheather you want special character or not.\n')

        if lenght.isdigit() and lenght_upper.isdigit() and lenght_lower.isdigit() and lenght_lower+lenght_upper<=lenght:
            if int(lenght_lower)+int(lenght_upper)<int(lenght):
                str=f'You have {int(lenght)-int(lenght_upper)-int(lenght_lower)} places left do you want special characters in you password? For yes type y, for no press enter.\n'
                SC_input=input(str)
                if SC_input.strip().lower()=='y':
                 return lenght, lenght_upper, lenght_lower,True
                else:
                    return lenght, lenght_upper, lenght_lower,False
            else:
                return lenght, lenght_upper, lenght_lower,False

        else:
            print("Wrong input, please try again")


def password_generator():

    lenght, lenght_upper, lenght_lower, boolvalue=input_taking()
    lenght, lenght_upper, lenght_lower=int(lenght), int(lenght_upper), int(lenght_lower)

    print(lenght, lenght_upper, lenght_lower,boolvalue)
    lowerletters = list(random.choice(string.ascii_lowercase) for i in range(lenght_upper))
    upperletters = list(random.choice(string.ascii_uppercase) for i in range(lenght_upper))
    if boolvalue:
        special_char= list(random.choice("!”#$%&'()*+,-./:;<=>?@[\]^_`{|}~.") for i in range(1))
        digit_char=list(random.choice("0123456789") for i in range(lenght-lenght_lower-lenght_upper-1))
    else:
        special_char=[]
        digit_char=list(random.choice("0123456789") for i in range(lenght-lenght_lower-lenght_upper))
    
    sample_list = list(lowerletters + upperletters+ special_char+ digit_char)
    random.shuffle(sample_list)
    password = ''.join(sample_list)
    print(password)


             
        

'''
    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    print('Random string with', letters_count, 'letters', 'and', digits_count, 'digits', 'is:', final_string)
'''
    



password_generator()