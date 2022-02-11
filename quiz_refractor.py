""" A quiz program. Program will generate quiz based on topic choosen from dictionary and calculate 
users score """


def display_score(topic, total_score):   # can you think of a more specifc function name? score could be confused with the numeric score for a quiz 
    #printing my subject and scores
    print(f"Your total score on {topic} questions is {total_score} out of " + str(len(ques_dict[topic])))

    if total_score == len(ques_dict[topic]):
        #print if all answers are right
        print("Great job you answered all questions correctly!")

def asking_questions(topic):  # use Python conventions for variable and function names 
    #creating variable to keep track on score
    total_score = 0

    # for t in ques_dict[topic]:  # full names are better than single letters. What is t ? 
    #     #printing out question
    #     print(t)
    #     #getting user input
    #     answer = input("Enter your answer:")
    #     #checking answer input with stored answers 
    #     #upper function will convert users input to uppercase
        
    #     if answer.upper() == ques_dict[topic][t].upper():
    #         print("Correct!")
    #         #add point to score
    #         total_score +=1
    #     else:
    #         print("Sorry, the answer is " +  ques_dict[topic][t] + ".")

    questions = ques_dict[topic]    # read the questions and store in a variable 
    for question in questions:  # to make the loop header simpler 
        print(question)
        answer = input("Enter your answer:")
        #checking answer input with stored answers 
        #upper function will convert users input to uppercase
        
        correct_answer = questions[question]  # another variable makes the intent clearer
        if answer.upper() == correct_answer.upper():  # and this statement simpler 
            print("Correct!")
            #add point to score
            total_score +=1
        else:
            print("Sorry, the answer is " +  correct_answer + ".")
    #return user scor
    return total_score

def main():
    print("A quiz program.")
    #loop through topics
    while True:
        print("Topics")
        #getting topics form my dictionry
        for t in ques_dict:  # full names are better than single letters. What is t ? topic? 
            print('\'' + t + '\'')
    #grab input topic from the user
        topic = input("Please choose a topic or type break to exit:")
        # user will type break to quit program
        if topic == "break":
            break
        #if input not valid topic
        elif topic not in ques_dict:
            # what if there was another topic? The second part of this message wouldn't make sense 
            print("That is not a valid topic. Please choose between art and space topics.")

        else:
            #if topic is valid call# askQuestion function and pass topic as paramter
            total_score = asking_questions(topic)
            #calling score function
            display_score(topic, total_score)
            
#create dictionary

ques_dict = {
        "art":
        {"Who painted the Mona Lisa?": "Leonardo Da Vinci",
        "What precious stone is used to make the artist\'s pigment ultramarine?": "Lapiz lazuli",
        "Anish Kapoor\'s bean-shaped Cloud Gate scuplture is a landmark of which city?": "Chicago",

        },
        "space":
        {"Which planet is closest to the sun?": "Mercury",
        "Which planet spins in the opposite direction to all the others in the solar system?": "Venus",
        "How many moons does Mars have?": "2",
        }

}
# call my main function
main()


