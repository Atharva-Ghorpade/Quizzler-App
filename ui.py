from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler App")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.label = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white")
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white", highlightthickness=1)
        self.question_text = self.canvas.create_text(150, 125, text="Hello", fill=THEME_COLOR,
                                                     font=("Ariel", 20, "italic"), width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.true_img = PhotoImage(file="images/true.png")
        self.true = Button(image=self.true_img, highlightthickness=0, command=self.true_pressed)
        self.true.grid(column=0, row=2)

        self.false_img = PhotoImage(file="images/false.png")
        self.false = Button(image=self.false_img, highlightthickness=0, command=self.false_pressed)
        self.false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,
                                   text=f"No questions left!\n"
                                        f"You got {self.quiz.score} correct answers out of 10 questions!"
                                   )
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("true"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
