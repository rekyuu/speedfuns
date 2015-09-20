while True:
  tid = int(input("What is your TID? "))
  
  if tid < 55296:
    print("Not a valid TID. Reset!")
  elif tid >= 55296 or tid <= 55551:
    print("Valid TID! D8")
  elif tid >= 55552 or tid <= 55807:
    print("Valid TID! D9")
  elif tid >= 63488 or tid <= 63743:
    print("Valid TID! F8")
  elif tid >= 63744 or tid <= 63999:
    print("Valid TID! F9")