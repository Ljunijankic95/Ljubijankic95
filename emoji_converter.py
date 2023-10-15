# First, the code without a function
message = input("> ")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😒"
}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

# The same functionality using a function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😒"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output

message = input("> ")
print(emoji_converter(message))