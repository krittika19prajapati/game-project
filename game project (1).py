#!/usr/bin/env python
# coding: utf-8

# In[5]:


print('Welcome to the World Geography Quiz Game')
answer=input('Are you ready to play the Quiz ? (yes/no) :')
score=0
total_questions=6

if answer.lower()=='yes':
    answer=input('Question 1: What is the smallest country in the world??')
    if answer.lower()=='vatican city':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')


    answer=input('Question 2: Which continent is the largest? ')
    if answer.lower()=='asia':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')

    answer=input('Question 3: Which of the Seven Wonders is located in Egypt ?')
    if answer.lower()=='pyramids of giza':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        
    answer=input('Question 4: Which desert is the largest in the world ? ')
    if answer.lower()=='sahara':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')
        
    answer=input('Question 5: Which city in India would you find the Taj Mahal in ? ')
    if answer.lower()=='agra':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')  
    
    answer=input('Question 6: What is the name of the world’s longest river ? ')
    if answer.lower()=='nile':
        score += 1
        print('correct')
    else:
        print('Wrong Answer :(')    
    
        

print('Thankyou for Playing this small quiz game, you attempted',score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('BYE! Have a Nice Day <3')


# In[ ]:




