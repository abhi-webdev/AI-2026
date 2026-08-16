import tiktoken

enc = tiktoken.encoding_for_model("gpt-4o")
text = "My name is Abhimanyu"

token = enc.encode(text)
print("token: ", token)

decodeToken = enc.decode([5444, 1308, 382, 3483, 35563, 147555])

print(decodeToken)
