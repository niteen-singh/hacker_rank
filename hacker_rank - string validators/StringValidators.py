if __name__ == '__main__':
    s = input()
    is_true = False
    commands = [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]
    for command in commands:
        is_true=False
        for characters in s:
            if(command(characters)) == True:
               is_true = True
               print ("True")
               break
        if is_true == False:
            print("False")
