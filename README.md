# JBN-team1-mastermind

## IEC2023 project

| Team Members |
| :---: |
| Brandon Ho |
| Noah Toma |
| Jonathan Hua |

### Design Process
The first step in our design process was analyzing the problem. The main problem we are attempting to solve is comparing the code with the user input. The user will have ten tries and after each attempt, they will recieve a black score and white score. To do so, we would have to compare each character of an array and see if there is any matching character. If there were two of the same characters, increment white by 1. If there were in the same position as well, it will increment black by 1.

### Assessing Resources
After understanding the problem, we assessed the resources that we are able to use. We had the option of doing HTML/CSS/JS or Python and utilizing TKinter. We chose to use Python as the language as we were more comfortable with the syntax. Although we lacked experience with GUIs, we were able to use TKinter to help us create a simple GUI for our game. Some resources were used to assist us in building our code such as tutorialspoint and pypi.org. As well we took some images from wikipedia.org to use in our report.

### Implementation
How we implemented our solution was first working on the logic side of the program. A dictionary was created to keep track of the black and white score. The code is randomly generated and a user will be able to input a value to guess. The code and the values are put into an array and each element is compared to one another. If there is matching char & in position, user will recieve a black point. If there is a matching char but not in position, user recieves a white point. There is a counter for attempts, where if the user passes 10 tries, there will be an output letting the player know they have lost and reveal the code.  Once we got the program running on the logic side, we tried implementing the GUI. Using TKinter, we were able to generate a GUI where the user is able to input a string and when the button is pressed, it would do the comparison and output the white and black values.

### Test Cases
For test cases, we tried covering all possible outcomes. The first one is 1 2 3 4 which is the correct code. The second test case is all correct but 1 so there is 3 black and 1 white. The third case is 4 3 2 1 where the output should be black=0 and white=4. Test case 4 is where none of the digits match which should output black = 0 and white=0.

### Future Improvements
If we had more time, we would further develop the GUI to make it more visually appealing. As well, we would add the option to change difficulty where easy mode would only require guessing 4 characters and hard mode is where the user would have to guess 6 digits. Lastly, we would improve on the design patterns and architecture of the program.As an example, we would structure the code into different classes.
