import pyttsx3

# Initialize the text-to-speech engine
engine=pyttsx3.init()

# Set properties like voice and speed (optional)
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate',150)

print("Welcome to the Robo speaker created by DAKSH LAKHI")

def robo_speaker():
    while True:
        input_user=input("Type to say something or write 'exit' to quit: ")
        if(input_user.lower()=="exit"):
            print("Robo Speaker: Goodbye!")
            engine.say("Goodbye")
            engine.runAndWait()
            break
        else:
            print("Robo Speaker: ",input_user)
            engine.say(input_user)
            engine.runAndWait()



if __name__ == "__main__":
    robo_speaker()