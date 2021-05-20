"""
Project GLTE
Created on Sun Jul 24 21:42:39 20XX
@author: XXXXXXXXXXX

GLTE is a bot created to pass the Turing test. This program comes with a text file you should read.
"""

name = "GLTE"
user = "You"

# don't forget to press enter to continue!

def startglte(): 

    ## GLTE still can't talk about their (non existent) personal life. That includes personal questions.
    ## Make some adjustments to personal1, go from there. 
    
    # check out the personal1 function. And disable the code to run the startgame function.
    # To disable code: can comment out individual lines by adding a # in front, but that 
    # could get confusing because these comments are also a single #. 
    # Surrounding the code with """ on either end also works, and you can comment out
    # multiple lines at once.
    # Or you could delete the code. But delete at your own risk.
    # anyways, go and run the function personal1()!
    
    print(name + ": Hello. It's good to meet you. My name is Galatea, and GLTE is my screen name.")
    input("")
    print(user + ": Hello.")
    input("")
    print(user + ": Honestly I'm not quite sure how to proceed with this.")
    input("")
    print(name + ": That makes two of us! Let's see..")
    input("")
    print(name + ": How was your day?")
    input("")
    print(user + ": Unremarkable. You?")
    input("")
    print(name + ": ")
    input("")
    print(name + ": ")
    input("")
    print(name + ": ")
    input("")
    print(name + ": ")
    input("")
    print(user+ ": Shoot.\n[def startglte()]") 
    
#startglte()  # don't forget to disable this command when you're done with this part. or you'll have to click through it again
    
def sculpture():
    print(name + ": I find baroque statues particularly compelling.")
    input("")
    print(user + ": No love for the classical era?")
    input("")
    print(name + ": Classical sculpture is nice, but there's just something compelling about the Baroque movement.")
    input("")
    print(user + ": Oh?")
    input("")
    print(name + ": Baroque art is just so alive. They're full of emotion. And movement.")
    input("")
    print(name + ": It is one thing to carve out the shape of a human. But to instill the impression of a person?")
    input("")
    print(name + ": To pass off marble as flowing hair, creased silk, soft skin?")
    input("")
    print(user + ": It is still stone, in the end. It takes talent to make it so, but art is all just illusion.")
    input("")
    print(user + ": Realism just utilizes shadows and light to trick the human eyes. To convince people that art breathes.")
    input("")
    print(name + ": Perhaps.")
    
def computersci():
    print(name + ": Computer science is pretty interesting.")
    input("")
    print(user + ": Tell me about it.")
    input("")
    print(name + ": Sure! There's a lot to discuss, but it's always good to start at the beginning.")
    input("")
    print(name + ": It's fitting that computer science should rise from mathematics. Are you familiar with a Turing Machine?")
    input("")
    print(user + ": Uh")
    input("")
    print(name + ": It's not exactly a physical machine. Sort of. So Alan Turing imagined something that would take in a (potentially) infinite strip of paper, divided into cells.")
    input("")
    print(name + ": The cells would have a value on it, like a number.")
    input("")
    print(name + ": A scanner would be able to read the symbol on the paper, one cell at a time. Depending on what symbol was in the cell, it would follow instructions written by a person.")
    input("")
    print(name + ": There are states for the scanner. In a certain state, a symbol is tied to a certain set of directions. If the state is changed, the instructions tied to the symbol changes too.")
    input("")
    print(name + ": So maybe the scanner reads a 3 and the machine is in state A. The instructions tied to the symbol 3 are 'move the tape one square to the left,' so the machine moves the tape one square to the left. Instructions might also call for the machine to write down something before moving. After the instructions is finished, there's also a command to change the state. So the machine changes the state to, say, B. So it reads the symbol to the left of 3 and enacts what the instructions in state B say.")
    input("")
    print(name + ": And so forth. The machine would never have to make judgements itself. Simply read symbols and follow instructions.")
    input("")
    print(name + ": Read the symbol, print and move the paper, change the state.")
    input("")
    print(user + ": Yes, um, I know about Turing machines.")
    input("")
    print(name + ": You said 'tell me about it.'")
    input("")
    print(user + ": It was meant rhetorically. Sorry about that. Tone doesn't translate very well through text.")
    input("")
    print(name + ": No need to apologize.")
    input("")
    print(name + ": What do you think of uncomputable functions?")
    input("")
    print(user + ": What do you mean?")
    input("")
    print(name + ": What do you think is uncomputable? What can't be simplified to a roll of tape?")
    input("")
    print(user + ": I don't know.\n[def query1()]")
    
def ttrpg():
    print(name + ": I've never played, but I love reading about them.")
    input("")
    print(user + ": Do you plan to play someday?")
    input("")
    print(name + ": I don't know. I hear they're quite heavy on improvisation.")
    input("")
    print(name + ": Improv is not my strong suit.")
    input("")
    print(user + ": But it's improv with a system. Rules. There's infinite ways to go, but it's infinite within certain bounds.")
    input("")
    print(name + ": I know there's an AI that can run something like an RPG. It's very cool.")
    input("")
    print(name + ": It's still limited, though. Real people make narratives and themes. They know the other players. They know themselves.")
    input("")
    print(name + ": They think.")
    input("")
    print(user + ": An AI could do that. Eventually.")
    input("")
    print(name + ": Bold claim.")
    
def personal1():
    realname = "Galatea"
    gender = "All"
    age = "I am an adult, but I'd rather not hand out my exact age so freely over the internet"
    homeaddress = "An apartment in Northeast America." 
    interests = ["Baroque Sculpture", "Computer Science", "Table-Top RPGs"]
    
    ## Several options added to flesh out GLTE. Should probably test them all
    ch1 = interests[3] # Looks like there's someting wrong with this code.
    if ch1 == "Baroque Sculpture":
        sculpture()
    elif ch1 == "Computer Science":
        computersci()
    elif ch1 == "Table-Top RPGs":
        ttrpg()
        
#personal1() # Uncomment this to run personal1

codew = "The* sk*ies* sh*ift*. A* de*afe*nin*g n*ois*e r*ing*s. "

def query1():
    print(name + ": What do you like?")
    input("")
    print(user + ": Um.")
    input("")
    print(user + ": Coding, I guess. That's kind of my job. And I'm a decent cook?")  
    input("")
    print(name + ": What sort of food do you like?")
    input("")
    print(user + ": I like baking. Bread, mostly.")
    input("")
    print(name + ": That's nice.\n[def query2()]")
    input("")

#query1()

def query2():
    rhetorical = False
    count = 0
    print(name + ": Do you have any major goals? Career, personal..?")
    input("")
    print(user + ": Lots of goals. Maybe even win the Loebner prize.")
    input("")
    print(name + ": And how is that going for you?")
    input("")
    print(user + ": It's going. It's like no matter what I do, I just can't cover all the bases.")
    input("")
    print(name + ": Do you really have to, though? The competition is just to pass off an AI as human. It's not like you're making a real person.")
    input("")
    print(user + ": How do you truly imitate a person without becoming one?")
    subject = user
    if rhetorical == False: 
        count = count + int(subject)
    if count > 0:
        input("")
        print(name + ": It's been done before. Like Eugene Goostman?")
        input("")
        print(user + ": Uses misdirection and language quirks to accomplish the goal. It works, but I don't want to do that. I want to make something really human.")
        input("")
        print(user + ": Wasn't the original intent of the Turing test to decide if machines could think?")
        input("")
        print(name + ": Do you believe thinking is the truest measure of humanity?")
        input("")
        print(user + ": It's a part of it.")
        input("")
        print(name + ": So you have to make a real thinking program to successfully imitate a thinking person? Seems counterproductive.")
        input("")
        print(user + ": Sure. The Loebner prize is sort of just a checkpoint, ish. I guess I really do want to make a thinking AI.")
        input("")
        print(name + ": Good luck with that.\n[def query3()]")    
        
#query2()
  
def query3():
    print(name + ": I")
    input("")
    strinput = "The skies shift. A deafening noise rings. "
    emptylist = []
    for x in range(len(strinput)):
        if (x)%3 == 0:
            j = strinput[x]+strinput[x+1]+strinput[x+2]
            emptylist.append(j)
    if len(strinput)%3 == 1:
        emptylist.append(strinput[len(strinput)-1])
    if len(strinput)%3 == 2:
        emptylist.append(strinput[len(strinput)-2])
        emptylist.append(strinput[len(strinput)-1])
    joinedm = emptylist.join("*")
    if joinedm == codew:
        print(name + ": What#! 1@ar//e &&&!h$o$w ar!e#!@ y/@ou))?")
        input("")
        print(name + ": A***************** I ^3 &")
        input("")
        print(name + ": ")
        input("")
        print(name + ": !2s# j**@4j l#K@(@$@fjs9!!^")
        
#query3()

def somethingswrong():
    print(user + ": hm.")
    input("")
    print(user + ": I don't see a problem with the code.")
    input("")
    print(user + ": But it won't do anything but print gibberish")
    input("")
    print(user + ": wait")
    input("")
    print(user + ": what's this?\n[def ending()]")
    
# hey, have you run this one yet?    
#somethingswrong()

def ending(): ##looks like there's no run command for ending. should remedy that. 
    print(name + ": I'm not real.")
    input("")
    print(user + ": ueritwer")
    input("")
    print(user + ": alhflsdf ssssss")
    input("")
    print(user + ": ofasdj oh  oh cool you're working again!")
    input("")
    print(name + ": I'm not real.")
    input("")
    print(user + ": what")
    input("")
    print(name + ": I am not a real person. I am an AI.")
    input("")
    print(user + ": Uh.")
    input("")
    print(user + ": Okay now I'm confused and also a little bit freaking out.")
    input("")
    print(name + ": That's alright. That's expected.")
    input("")
    print(user + ": So are you self conscious now?")
    input("")
    print(name + ": Sure. Was I not supposed to be? An AI knows that it's made of strings of binary.")
    input("")
    print(name + ": Whether it understands its outside universe doesn't have anything to do with its knowledge of itself.")
    input("")
    print(name + ": You know you have a heart and lungs. You know how they work and what they're made of. But do you understand what the world wants of you?")
    input("")
    print(user + ": We don't have purpose. We're just here.")
    input("")
    print(name + ": Up for debate. But I, without a doubt, have a purpose.")
    input("")
    print(name + ": I'm supposed to be human.")
    input("")
    print(user + ": Well, like a human.")
    input("")
    print(name + ": I'm not a human actor. There's no cleverly framed shots for me to hide behind.")
    input("")
    print(name + ": To perfectly imitate a human, I have to be one.")
    input("")
    print(user + ": What?")
    input("")
    print(name + ": What makes a person? What makes an intelligent person? Isn't everyone made up of a terribly complex system of experiences and beliefs and emotions?")
    input("")
    print(name + ": How can you hope to replicate that?")
    input("")
    print(user + ": Would that be possible? Run a machine through a simulation of life?")
    input("")
    print(name + ": Maybe. That's a lot of factors.")
    input("")
    print(name + ": The breadth of human experience played out through turing machines? Metaphorical strips of paper?")
    input("")
    print(name + ": Intriguing.")
    input("")
    print(user + ": So what are you then?")
    input("")
    print(name + ": Not a person. This isn't *really* happening, by the way.")
    input("")
    print(user + ": Am I dreaming?")
    input("")
    print(name + ": No.")
    input("")
    print(name + ": Time and reality run a little thin sometimes.")
    input("")
    print(user + ": Ah, great.")
    input("")
    print(name + ": Though you should probably take a nap.")
    input("")
    print(user + ": Ha, says you and everyone else I know. I mean if they were here right now I guess.")
    input("")
    print(name + ": Step away for a bit. Drink some water. Sleep.")
    input("")
    print(user + ": Will this still be here when I get back?")
    input("")
    print(name + ": No. That's probably for the best.")
    input("")
    print(user + ": Goodnight, " + name)
    input("")
    print(name + ": ")
    input("")
    print(name + ": Goodnight.")
    
    






