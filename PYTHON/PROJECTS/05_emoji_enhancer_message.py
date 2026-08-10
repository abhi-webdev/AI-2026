

message_info = {
    "love" : "💖",
    "code" : "💻",
    "tea" : "🍵",
    "music" : "🎵",
    "video" : "📺"
}

user_message = input("Enter your messages: ")

updated_message = []

for message in user_message.split() :
    cleaned = message.lower().strip(".,?!")
    new_info = message_info.get(cleaned, "")

    if new_info :
        updated_message.append(f"{message} {new_info}")
    else :
        updated_message.append(f"{message}")


enhanced_message = " ".join(updated_message)
print("\n Enhanced Word")
print(enhanced_message)
