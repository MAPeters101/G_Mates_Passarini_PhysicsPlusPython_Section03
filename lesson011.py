# In the following text, the temperature is given in Fahrenheits.  Write code
# that replaces all instances of the temperature in Fahrenheit and the unit
# itself by Celsius temperatures and units.  The formula to convert Fahrenheit
# to Celsius is a s follows:
# C = (F-32) * 5/9

def fahrenheit_to_celsius(f):
    return (f-32) * 5/9

message = "The temperature recorded today was 91 degrees Fahrenheit.  Yesterday, the temperature registered was 80 degrees Fahrenheit, which was a big change!"

new_message = message.replace("Fahrenheit", "Celsius")

words = new_message.split(' ')
#print(words)
for index, word in enumerate(words):
    if word.isnumeric():
        #print(word)
        value = fahrenheit_to_celsius(float(word))
        #print(value)
        words[index] = f"{value:.2f}"
#print(words)
new_message = " ".join(words)
print(new_message)
