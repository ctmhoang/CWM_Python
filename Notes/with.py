try:
  with open("with.py") as f: #Can open multiply file by  add open statements with colons
    print("File opened.")
  age = int(input("Age: "))
  except:
    print("Not a valid value")
  else:
    print("Run successfully")
    
    #Close the file implicitly 
