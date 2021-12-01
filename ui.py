from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_data: QuizBrain):
        self.quiz = quiz_data
        self.window = Tk()
        self.window.title("Quizler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.quiz_canvas = Canvas(width=300, height=250, bg='white')
        self.quiz_score = Label(text=f"Score: {self.quiz.score}", fg='white', bg=THEME_COLOR)
        self.quiz_score.grid(row=0, column=1)
        self.quiz_canvas_text = self.quiz_canvas.create_text(
            150, 100,
            text="Quiz Text",
            font=('Ariel', 16, 'italic'),
            fill=THEME_COLOR,
            width=280
        )
        self.quiz_canvas.grid(row=1, column=0, columnspan=2, pady=20)
        true_button_image = PhotoImage(file='./images/true.png')
        self.true_button = Button(image=true_button_image, command=self.answer_true, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        false_button_image = PhotoImage(file='./images/false.png')
        self.false_button = Button(image=false_button_image, command=self.answer_false, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.quiz_canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.quiz_canvas.itemconfigure(self.quiz_canvas_text, text=q_text)
        else:
            self.quiz_canvas.itemconfigure(self.quiz_canvas_text, text=f"That's all folks!\n"
                                                                       f"Final Score: {self.quiz.score}")
            self.false_button.config(state='disabled')
            self.true_button.config(state='disabled')

    def answer_true(self):
        self.give_feedback(self.quiz.check_answer('True'))

    def answer_false(self):
        self.give_feedback(self.quiz.check_answer('False'))

    def give_feedback(self, is_right):
        if is_right:
            self.quiz_canvas.config(bg='green')
            self.quiz_score.config(text=f"Score: {self.quiz.score}")
        else:
            self.quiz_canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
