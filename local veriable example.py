 hacker = "me"
 def local_variable_example():
    hacker = "you"
    print("The local variable is %s") % (hacker)
 local_variable_example()
 print("The global variable is %s") % (hacker)