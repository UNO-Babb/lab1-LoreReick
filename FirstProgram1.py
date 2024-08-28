#FirstProgram.py
#Name: Lore Reick
#Date: 8/28/24
#Assignment: Asking for the name of a person and their birthday

def main():
  import time
  print("First Program")
  time.sleep(1)
  #Say hello!
  print("Hello!")
  time.sleep(1)
  #Ask for the user's name
  name = input("What is your name?")
  #Use the user's name in the program.
  print("Good to meet you", name)
  time.sleep(1)
  #Ask the user for their age.
  age = input("Out of curiosity, how old must you be?")
  #Tell the user what year they were born in.
  age = int(age)
  birthYear = 2024 - age
  print("so you were born in", birthYear)
  #Assume that they have not had their birthday yet this year.


#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
