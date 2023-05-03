# Quizz app
This is a Python-based quiz application that asks users a series of true/false questions and provides feedback on their answers. 
The app is designed to be simple and easy to use, with a user-friendly interface and straightforward functionality.
The question for the app are fetched with and API from the following page: https://opentdb.com/api_config.php.

![quizz.gif](..%2F..%2FOneDrive%2FRadna%20povr%9Aina%2Fquizz.gif)


I specified the parameters to use 10 questions of any category and set the type to be True/False.
You can go to this link and customize the questions to be of any number and choose between many categories such as: Sports, History, Computer Science etc.
For example:

![image](https://user-images.githubusercontent.com/108518278/235871765-c11340b9-e501-4db6-b17a-5ddc1dd781f8.png)

Once you're satisfied with your choice hit the "Generate API URL" button and copy the link you see:
![image](https://user-images.githubusercontent.com/108518278/235872149-d83db7dc-d71f-4d23-814e-997c7ad01a01.png)
Go the app files and open _data.py_ .In the line: 

`response = requests.get(url="https://opentdb.com/api.php?", params=ps)` 

paste the link that you copied instead of the existing _url_ attribute and that's it.