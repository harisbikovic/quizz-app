from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizzInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title = "Quizz"
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas_text = self.canvas.create_text(150, 125, text="Some text",
        fill="black", # x=150, y=125
        font=("Arial", 20, "italic"), width=280) #width=280 makes text fit into canvas
        self.canvas.grid(column=0, row=1, columnspan=2,pady=50)

        right_img = PhotoImage(file="./images/true.png")
        self.correct_button = Button(image=right_img, highlightthickness=0,
                                     border=0, command=self.true_pressed)
        self.correct_button.grid(column=0, row=2)
        wrong_img = PhotoImage(file="./images/false.png")
        self.uncorrect_button = Button(image=wrong_img, highlightthickness=0,
                                     border=0, padx=10, pady=20, command=self.false_pressed)
        self.uncorrect_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="You answered all the questions!")
            self.correct_button.config(state="disabled")
            self.uncorrect_button.config(state="disabled")

    def true_pressed(self):
        is_right=self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right=self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        timer = self.window.after(1000, self.get_next_question)

