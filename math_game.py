from random import randint

def read_txt(count):
    """ Checks if text file is empty, then compares the scores to determine highscore """
    file = "users.txt"
    reader = ""
    user_string= ""
    user_score = ""
    winning_message = ("************New Highscore***************\nTotal Points: "+ str(count))
    try:
        with open(file) as f_obj:
            filled = f_obj.read(1)
            if not filled:
                print winning_message 
                write_score(count)
            else:
                reader = f_obj.readline()
                for line in reader.rstrip():
                     if line.isdigit():
                        user_score += line
                     else:
                        user_string+=line
                if(int(count)>int(user_score)):
                    print winning_message
                    write_score(count)
                else:
                    print ("High Score to beat: "+filled.title()+ user_string+" with  "+str(user_score)+" point(s)." )   
    except IOError:
        print("Could not find file")

def write_score(new_score): # Change out the old and new in case it needs to be
    """" Takes the new high score and adds it with the user's name """
    no_digits = True
    file = 'users.txt'
    try:
        with open(file, "w") as f_obj:
            while no_digits == True:
                username = raw_input("\nName: ")
                for i in username:
                    if i.isdigit():
                        print("Please enter a name without digits")
                        no_digits = True
                    else:
                        no_digits = False
                            
            f_obj.write(username)
            f_obj.write(str(new_score))
    except IOError:
        print("Could not find "+ file)
    


def check_answer(value_1, value_2, answer):
    """ Will check if the user answer is correct 
            Returns True if correct, False if incorrect
    """
    correct = "\t\t   That's Correct\n"
    incorrect = "\n\t     Incorrect. Game Over"
    response = raw_input("  Which operand was used? ( * / + - ): ").strip()
    operands = ["+", "-", "/", "*"]
    if response in operands:
        if response =="+":
            div =value_1 + value_2
            if div == answer:
                print(correct)
                return True
            else:
                print(incorrect)
                return False
        if response =="-":
            div =value_1 - value_2
            if div == answer:
                print(correct)
                return True
            else:
                print(incorrect)
                return False
        if response =="*":
            div =value_1 * value_2
            if div == answer:
                print(correct)
                return True
            else:
                print(incorrect)
                return False
        if response =="/":
            div =value_1 / value_2
            if div == answer:
                print(correct)
                return True
            else:
                print(incorrect)
                return False
    else:
        print("\t  Please only enter (* / + -)")
        return False
    
def math_app():
    """ generates random numbers and (+,*,/,-) """
    print("\nPrepare to test your 3rd grade skills! ")
    count = 0
    validation = True
    while validation == True:
        first_value =float( randint(1, 20))
        second_value = float(randint(1, 20))
        chance = randint(0,3)
        
        possibility = [(first_value + second_value),(first_value - second_value),
                      (first_value / second_value),(first_value * second_value)]
        message ="\t\t"+ str(first_value)+" ___ "+str(second_value)+ " = "+str(possibility[chance])
        print(message)
        
        value_1 = float(first_value)
        value_2 = float(second_value)
        answer = float(possibility[chance])
        validation = check_answer(value_1, value_2, answer)
        count += 1
    count -=1
    print("\t      Point(s)\t\t\t"+str(count)) 
    read_txt(count)

#play_operands()

    