# In the following text, the temperature is given in Fahrenheits.  Write code
# that replaces all instances of the temperature in Fahrenheit and the unit
# itself by Celsius temperatures and units.  The formula to convert Fahrenheit
# to Celsius is a s follows:
# C = (F-32) * 5/9

text = """The temperature recorded today was 91 degrees Fahrenheit.  
Yesterday, the temperature registered was 80 degrees Fahrenheit, which was a big change!"""

tF1 = 91
tF2 = 80
C1 = (tF1-32) * 5/9
C2 = (tF2-32) * 5/9

text1 = text.replace('Fahrenheit', 'Celsius')
text2 = text1.replace('91',str(C1))
text3 = text2.replace('80',str(C2))

print(text3)