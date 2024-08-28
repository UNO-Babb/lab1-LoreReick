#FirstProgram.py
#Name: Lore Reick
#Date: 8/28/24
#Assignment:

def main():
  print("Madlib")
  import time
  #Ask user for words
  time.sleep(1)
  print("hello! Lets play Madlib! Give me six words to start.")
  noun1 = input(1)
  noun2 = input(2)
  noun3 = input(3)
  noun4 = input(4)
  noun5 = input(5)
  noun6 = input(6)
  time.sleep(1)
  #Print the story with the user supplied words.
  print("I enjoy my family's", noun1)
  print("But sometimes, my family does", noun2)
  print("And let me tell you, my brother", noun3)
  print("But don't worry, my mother does calm my brother down with", noun4)
  print("The dog hates it when", noun5)
  print("And we are one big happy", noun6)
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
