for _ in range(int(input())):
 a,b=map(int,input().split())
 l=list(map(int,input().split()))
 ans=0
 for i in l:
  if i>b:
   ans=ans+1
 print(f'get shot --> {ans}')


#Explanation

'''
for _ in range(int(input())):
This line reads a single line of input, which represents the number of test cases T, and converts it to an integer. The range() function then creates an iterable that will be looped over T times. The _ is used as a placeholder for the loop variable since we don't need its value.

a, b = map(int, input().split())
This line reads a line of input that contains the values of a and b separated by a space. The map(int, input().split()) function splits the input line into individual values, converts them to integers, and assigns them to the variables a and b respectively

l = list(map(int, input().split()))
This line reads another line of input that contains the heights of the players separated by spaces. It follows the same logic as the previous line, but instead of assigning the values to variables, it creates a list called l containing the integer values.
python

for i in l:
    if i > b:
        ans = ans + 1
This block iterates through each height in the list l. For each height, it checks if it is greater than b. If the condition is true, it means the player needs to get shot, and the ans variable is incremented by 1.

print(f'get shot --> {ans}')
This line print output
'''