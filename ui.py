from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
   def __init__(self, quiz_brain: QuizBrain):
      self.quiz = quiz_brain

      self.window = Tk()
      self.window.title("Quizzler")
      self.window.config(padx = 20, pady = 20, bg= THEME_COLOR)

      self.score_text = Label(text=f"score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
      self.score_text.grid(column=2, row=1)

      self.canvas = Canvas(height=250, width=300)
      self.question_text = self.canvas.create_text(
         150,
         125,
         width=280,
         text=f"rfdghjklhgv",
         fill=THEME_COLOR,
         font=("Arial", 20, "italic")
      )
      self.canvas.grid(column=1, row=2, columnspan=2, pady=50)

      right_img = PhotoImage(file="./images/true.png")
      wrong_img = PhotoImage(file="./images/false.png")
      self.right_button = Button(image=right_img, highlightthickness=0, command=self.is_right)
      self.wrong_button = Button(image=wrong_img, highlightthickness=0, command=self.is_wrong)
      self.right_button.grid(column=1, row=3)
      self.wrong_button.grid(column=2, row=3)

      self.get_next_question()

      self.window.mainloop()

   def get_next_question(self):
      self.canvas.config(bg="white")
      if self.quiz.still_has_questions():
         q_text = self.quiz.next_question()
         self.canvas.itemconfig(self.question_text, text=q_text)
      else:
         self.canvas.itemconfig(self.question_text, text = ("You've reached the end of the quiz! "
                                                           f"Your score was {self.quiz.score}/10"))
         self.right_button.config(state="disabled")
         self.wrong_button.config(state="disabled")
   def is_right(self):
      is_right = self.quiz.check_answer("True")
      self.give_feedback(is_right)

   def is_wrong(self):
      is_right = self.quiz.check_answer("False")
      self.give_feedback(is_right)


   def give_feedback(self, is_right):
      if is_right:
         self.canvas.config(bg="green")
         self.score_text.config(text=f"Score: {self.quiz.score}")

      else:
         self.canvas.config(bg="red")
      self.window.after(1000, self.get_next_question)


