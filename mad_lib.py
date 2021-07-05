# MadLib game
\
activity_1 = input("What is your favorite activity?: ")
name = input("What is your name?: ")
verb_1 = input("Give me a verb please: ")
favorite_relative = input("Name of favorite relative: ")
favorite_channel = input("Name of favorite tv channel: ")
emotion = input("Enter a past tense emotion: ")
profession = input("What is your current profession?: ")
high_school_crush = input("Who was your high school crush?: ")
item = input("Enter a thing/object: ")

\
MadLib = f"Breaking News!! We interrupt your {activity_1} to tell you that \
{name} has been spotted {verb_1} at the local zoo. There is video footage \
captured by {favorite_relative} and submitted to {favorite_channel}. We \
are {emotion} by their actions. The {profession} almost got \
involved but {high_school_crush} ran out in front and gave them {item}. \
Some how this calmed the {profession} down and {name} was let go!"

print(MadLib)
