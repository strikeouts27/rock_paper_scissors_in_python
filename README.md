# rock_paper_scissors_in_python
Rock Paper Scissors
strikeouts27
OP
 — Today at 1:11 AM
I am trying to get my python rock paper scissors game but I hit a snare. When the computer is supposed to determine what move to do it uses math.random and math.floor to calculate a number from 1-3. The if statements are supposed to evaluate the variable and activate code based on it but it will not do it. What can I do about it?

https://paste.pythondiscord.com/YE7A
Python
 pinned 
a message
 to this channel. See all 
pinned messages
.
 — Today at 1:11 AM
Python
BOT
 — Today at 1:11 AM
@strikeouts27

Python help channel opened
Remember to:
• Ask your Python question, not if you can ask or if there's an expert who can help.
• Show a code sample as text (rather than a screenshot) and the error message, if you've got one.
• Explain what you expect to happen and what actually happens.

:warning: Do not pip install anything that isn't related to your question, especially if asked to over DMs.
Closes after a period of inactivity, or when you send !close.
LX -> nxbxdy — Today at 1:15 AM
math.random does not exist. There is the random module tho.
you could then use random.randint(1, 3)
strikeouts27
OP
 — Today at 1:16 AM
duly noted making correction
LX -> nxbxdy — Today at 1:16 AM
and for randrange, the default start and step are 0 and 1, so would've been random.randrange(3) better, which chooses from 0, 1, 2
and does not require rounding in any way... :)
really there is a better way still
what you want to do is choose something random from "Rock", "Paper", "Scissors"
strikeouts27
OP
 — Today at 1:18 AM
you can do that!?
LX -> nxbxdy — Today at 1:18 AM
so there is the random.choice function.
import random
moves = ("rock", "paper", "scissors")
computer_move = random.choice(moves)
strikeouts27
OP
 — Today at 1:19 AM
that is way better.
how would the code activate though?
LX -> nxbxdy — Today at 1:20 AM
that isn't really a meaningful phrase
Fashoomp — Today at 1:20 AM
activate?
LX -> nxbxdy — Today at 1:20 AM
Fashoomp's turn
👋
Fashoomp — Today at 1:20 AM
👋
lol I can take a backseat 🙂
strikeouts27
OP
 — Today at 1:21 AM
My code has it where the computer determines a number from 1,2,3 and stores it in a variable. and than.... thats it.....

the code will not go through the if statements
Fashoomp — Today at 1:22 AM
well looking at how the functions are set up, your judge_outcome is trying to access variables that don't exist in that function
you also shouldn't be using & for your and comparisons
there's actually quite a lot wrong here
I highly advise only writing a little bit of code at a time and then testing, otherwise you end up with something like this where it's honestly better to throw it out and start over
strikeouts27
OP
 — Today at 1:23 AM
I was testing as I was going along. but it seems I wrote too many lines
Well I will try to do it over again using different techniques
Fashoomp — Today at 1:24 AM
def player_choice():
    player_choice = input(
be very careful with your variable names
you named your function player_choice and then immediately created a variable with the same name
Also make sure you're ultimately returning these choices so that main() is able to access these values and pass them along
strikeouts27
OP
 — Today at 1:26 AM
so whats the difference between storing something in a variable for access and using return?
Is there any part of this that I should salvage?
Fashoomp — Today at 1:27 AM
return is the result of calling a function
you need to return the value from the function so that you can then later store it in a variable
korty.codes — Today at 1:28 AM
!return-gif to the rescue, whoever created this is a legend ^^ I love it so much
Python
BOT
 — Today at 1:28 AM
Print and return
Here's a handy animation demonstrating how print and return differ in behavior.

See also: /tag return
Print and return
Fashoomp — Today at 1:28 AM
def get_player_choice():
    while True:
        choice = input("Rock paper scissors. Make a choice r/p/s")
        if choice.lower() in ('r', 'p', 's'):
            return choice
here's an example of what your function would look like to ask the player for their choice
it will repeatedly ask the user for input until they enter either r, p, or s 
then once successful, it returns that value, which means when calling the function, we can store their choice
def get_player_choice():
    while True:
        choice = input("Rock paper scissors. Make a choice r/p/s")
        if choice.lower() in ('r', 'p', 's'):
            return choice


player_choice = get_player_choice()
here on the last line, we know that player_choice will always be equal to either "r", "p", or "s"
strikeouts27
OP
 — Today at 1:31 AM
So by calling the function it goes through the process of asking the user for their choice and than returns or holds onto that value via the return function. Than later on we have a variable that will hold that return value whenever the get_player_choice function is called.
And that is a more efficent way of writing this code than if and elif statements
Fashoomp — Today at 1:32 AM
return does not hold onto any values
it returns it
strikeouts27
OP
 — Today at 1:32 AM
I suppose a part of improving is attempting  to write programs by myself, checking the documentaiton for other techniques, making changes, and than soliciting feedback for code reviews.
Fashoomp — Today at 1:32 AM
yeah, you learn by doing
strikeouts27
OP
 — Today at 1:33 AM
whats the difference between returning and holding? I mean it seems to be the same thing right? returning it is holding onto the calcualted result is it not?
Fashoomp — Today at 1:33 AM
you'll still need if/elif to ultimately compare the results for the gameplay 
korty.codes — Today at 1:33 AM
return transfers the variable(s) from inside the function, to outside the function.
Fashoomp — Today at 1:34 AM
"returning" is the function saying "I have finished running and have arrived at this value". What you ultimately do with that value is up to you (but it's often then stored as a variable because what's the point of calculating a value if you don't plan on using it)
strikeouts27
OP
 — Today at 1:34 AM
So return is the outcome of the function and it um.... is its value each time the function is called.... its not held or anything its just .... is
and other functions can access that return value
Fashoomp — Today at 1:35 AM
yes, it's calculated when the function is called
def foo():
    return 5

result = foo()
as far as this last line is concerned, it might as well say result = 5
foo() has a value of 5
def foo():
    return 5

foo()
strikeouts27
OP
 — Today at 1:35 AM
*begins to see the truth
Fashoomp — Today at 1:36 AM
if I did this, then it's still returning the 5, but I'm not doing anything with it
!e
5
Python
BOT
 — Today at 1:36 AM
@Fashoomp :warning: Your 3.12 eval job has completed with return code 0.

[No output]
Fashoomp — Today at 1:36 AM
it's not an error, but it isn't doing anything useful either
strikeouts27
OP
 — Today at 1:37 AM
Okay so I need to go back and re write my program with the code suggested and also more changes
Fashoomp — Today at 1:37 AM
Yes, and test, test, test as you go
if you hit an error, don't write more code until you've worked out that error
don't dig yourself out of a problem
strikeouts27
OP
 — Today at 1:40 AM
I will be back in one hour!
strikeouts27
OP
 — Today at 2:10 AM
so I am in a while loop
and it is running the get_player_choice function twice
I only need it to run once
Fashoomp — Today at 2:10 AM
The loop exists in the get_player_choice function to get the appropriate input, which means you no longer need a while loop outside the function to get the choice
strikeouts27
OP
 — Today at 2:11 AM
https://paste.pythondiscord.com/HYVQ
So delete teh while loop
Fashoomp — Today at 2:11 AM
did you mean to share the full thing?
No, the loop inside that function is correct
strikeouts27
OP
 — Today at 2:11 AM
https://paste.pythondiscord.com/N3HA
it seems to run twice when called
I need it to run once
without the while loop it would never activate
but its also the cause of it going again
I suppose I could put a stopping condition on it such as increment player moves from 0->1
Fashoomp — Today at 2:13 AM
can you share the full thing? What you shared absolutely would not behave like you're describing
strikeouts27
OP
 — Today at 2:14 AM
https://paste.pythondiscord.com/7TVA
Fashoomp — Today at 2:14 AM
yeah, because you're literally calling it twice
line 17
line 28
you can delete the one on line 17
but you need to store the returned value on line 28
line 17 should be on 28
def main():
    introduction()
    player_choice = get_player_choice()
strikeouts27
OP
 — Today at 2:16 AM
https://paste.pythondiscord.com/VDDA
Fashoomp — Today at 2:16 AM
you aren't returning anything from your computer choice function
you really shouldn't have any code that isn't inside a function
other than calling main, which you're calling twice for some reason
Image
strikeouts27
OP
 — Today at 2:17 AM
I have removed line 29
okay so the reason it was looping twice was because the code inside of my main function was telling it to loop twice
Fashoomp — Today at 2:19 AM
it wasn't looping twice
you were calling it twice
Fashoomp — Today at 2:19 AM
No, not at all
your main function is "what should happen when you run this program"
it's responsible for calling your other functions that "get the ball rolling" so to speak
strikeouts27
OP
 — Today at 2:21 AM
https://paste.pythondiscord.com/MUAA
so it seems in my main function a variable is getting its value defined
player_choice to be specific
Fashoomp — Today at 2:24 AM
you're still not returning anything from computer choice
and you still have code outside functions
def determine_outcome():
    

moves = ("rock", "paper", "scissors")
computer_move = random.choice(moves)

def main():
    introduction()
    player_choice = get_player_choice()
    computer_choice()
this will error
you cannot define a function and not have a block of code under it
strikeouts27
OP
 — Today at 2:25 AM
a return value has been placed on computer choice
https://paste.pythondiscord.com/5MQA
I have made some updates
Fashoomp — Today at 2:28 AM
you've made some mistakes
main should not be indented
don't worry about the loop of your game just yet
it's much easier to figure out "one round of play" and then worry about the looping functionality later
strikeouts27
OP
 — Today at 2:29 AM
now the code will not run at all. it seems main is hung up on indentation.
and that is because of my determine_outcome function
Fashoomp — Today at 2:30 AM
yes
also now that computer_choice is returning, make sure you're assigning a variable to the function call
strikeouts27
OP
 — Today at 2:30 AM
So the determine_outcome function is where I use if statements to evaluate the player and computer choice and determine a winner
Fashoomp — Today at 2:30 AM
Yes, which means you should make that function have two parameters
that way it can read in the values determined earlier
strikeouts27
OP
 — Today at 2:32 AM
https://paste.pythondiscord.com/HIJA
okay so now I need to use if statements to determine the player choice vs the computer choice.
thinking
my inclination is to do if elif statements but whenever I do so during my code review everyone says there is a more efficent way
strikeouts27
OP
 — Today at 2:41 AM
https://paste.pythondiscord.com/7EHQ
should I do the same for this or maybe try using a while loop instead of if statements
Would I make another if statement for all the outcomes?
Fashoomp — Today at 2:46 AM
For determining the outcome, I would start by checking to see if the player and computer chose the same option (a tie). That will cut down on how many more comparisons you need to make later 
Which also means I would modify the get functions to make sure they return similar data
right now the player is r, p, s, but the cpu is rock, paper, scissors
this would be a whole lot easier if they were both using the same moves
strikeouts27
OP
 — Today at 3:03 AM
https://paste.pythondiscord.com/HWIQ
Fashoomp — Today at 3:05 AM
What happened to your main function?
strikeouts27
OP
 — Today at 3:05 AM
trying to figure that out myself
the get_player_choice and get_computer_choice function are not activating
Fashoomp — Today at 3:05 AM
because you removed your main function that was calling them
