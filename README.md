# Quizz app
This is a Python-based quiz application that asks users a series of true/false questions and provides feedback on their answers. 
The app is designed to be simple and easy to use, with a user-friendly interface and straightforward functionality.
The question for the app are fetched using the API from the following page: _https://opentdb.com/api_config.php_.

![](https://imgur.com/z9xHYLd.gif)

Once the player answers all 10 questions the game stops:

![image](https://user-images.githubusercontent.com/108518278/235893700-23b0021e-168d-4447-a16e-d895847b9938.png)

## Installation

To install the app, follow these steps:

1. Clone the repository to your local machine using the command:
`git clone https://github.com/harisbikovic/quizz-app.git`

2. Install the required dependencies using the command:
`pip install -r requirements.txt`

3. Run the app by running the main.py file using the command:
`python main.py`

## Customization

I specified the parameters to use 10 questions of any category and set the type to be True/False.
You can go to this link and customize the questions to be of any number and choose between many categories such as: Sports, History, Computer Science etc.
For example:

![image](https://user-images.githubusercontent.com/108518278/235871765-c11340b9-e501-4db6-b17a-5ddc1dd781f8.png)

Once you're satisfied with your choice hit the "Generate API URL" button and copy the link you see:
![image](https://user-images.githubusercontent.com/108518278/235872149-d83db7dc-d71f-4d23-814e-997c7ad01a01.png)
Go the app files and open _data.py_ .In the line: 

`response = requests.get(url="https://opentdb.com/api.php?", params=ps)` 

paste the link that you copied instead of the existing _url_ attribute and that's it.
