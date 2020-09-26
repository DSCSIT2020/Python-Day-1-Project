email = input("Enter your email address: ")
username = email[:email.index("@")]
domain = email[email.index("@")+1:]
print("Username: {}\nDomain: {}".format(username,domain))