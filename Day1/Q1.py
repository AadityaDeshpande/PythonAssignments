import re

def ValidateMail(str1):

    pattern = '^[a-zA-Z]+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

    if(re.search(pattern,str1)):
        print(str1," ==>>  is valid")
    else:
        print(str1," ==>>  is not valid")

    
def main():
    try:
        myfile=open("Emails.txt")

        while(True):
            line = myfile.readline()

            if(line == ""):
                break

            line = line.rstrip()

            ValidateMail(line)

    except IOError as e:
        print("Caught an exception ",e)

    finally:
        myfile.close()

if __name__ == '__main__':
    main()
    
