teksti = "Monty Python"
kieli = teksti[6:12]

#Python 3.13.7 (tags/v3.13.7:bcee1c3, Aug 14 2025, 14:15:11) [MSC v.1944 64 bit (AMD64)] on win32
#Type "help", "copyright", "credits" or "license" for more information.
#>>> str (42)
#'42'
#>>> kirjain 2 = teksti[6]
#  File "<python-input-1>", line 1
#    kirjain 2 = teksti[6]
#            ^
#SyntaxError: invalid syntax
#>>> kirjain2 = teksti[6]
#Traceback (most recent call last):
#  File "<python-input-2>", line 1, in <module>
#    kirjain2 = teksti[6]
#               ^^^^^^
#NameError: name 'teksti' is not defined
#>>>
#>>> teksti = Monty Python
#  File "<python-input-4>", line 1
#    teksti = Monty Python
#                   ^^^^^^
#SyntaxError: invalid syntax
#>>> teksti = 'Monty Python'
#>>> kirjain2 = teksti[6]
#>>> kirjain2
#'P'
#>>> kieli = teksti [6:12]
#>>> kieli
#'Python'
#>>> print(kieli)
#Python
#>>> f'Paras ohjelmointikieli on {kieli}'
#'Paras ohjelmointikieli on Python'
#>>>
