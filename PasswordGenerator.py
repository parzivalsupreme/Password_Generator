import random

#Main Code
uppercaseLetter1=chr(random.randint(65,90)) 
uppercaseLetter2=chr(random.randint(65,90))
uppercaseLetter3=chr(random.randint(65,90))
uppercaseLetter4=chr(random.randint(65,90))
lowercaseletter1=chr(random.randint(97,122))
lowercaseletter2=chr(random.randint(97,122))
lowercaseletter3=chr(random.randint(97,122))
lowercaseletter4=chr(random.randint(97,122))
symbols=chr(random.randint(33,152))
integers=chr(random.randint(48,57))

#Generating all random elements by combining all variables to produce random passwords
password = uppercaseLetter1 + uppercaseLetter2 + uppercaseLetter3 + uppercaseLetter4 + lowercaseletter1 + lowercaseletter2 + lowercaseletter3 + lowercaseletter4 + symbols + integers

print(password)