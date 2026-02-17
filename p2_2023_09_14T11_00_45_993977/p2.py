# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.15.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [code] deletable=false editable=false
# import and initialize otter
import otter
grader = otter.Notebook("p2.ipynb")

# + editable=false
import public_tests

# +
# PLEASE FILL IN THE DETAILS
# enter none if you don't have a project partner
# you will have to add your partner as a group member on Gradescope even after you fill this

# project: p2
# submitter: 903 014 0256
# partner: none
# hours: 8:50 to 9:40AM

# + [markdown] deletable=false editable=false
# # Project 2: Operators, expressions, and variables

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
# In this project you will demonstrate your ability to:
#
# - use arithmetic operators, including the floor division operator,
# - call the type function on an expression,
# - use logical operators such as `and`, `or`, and `not`,
# - use comparison operators,
# - store values and results of expressions into variables.
# -

# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `public_tests.py`. If you are curious about how we test your code, you can explore this file, and specifically the value of the variable `expected_json` (at line *62* of the file), to understand the expected answers to the questions. It is okay if you do not understand how this file works for now. We promise that you will be able to understand everything going on in that file by the end of this semester.
#
# In the meantime, after answering each question (say Question 1), you can test your answer directly on the notebook by running the cell below that question which says (in the case of Question 1) `grader.check("q1")`. If you have answered the question **correctly**, you will see the following:
#
# ![correct.PNG](attachment:correct.PNG)

# Instead, if you make a **semantic error**, you might see an error message similar to the one below:
#
# ![semantic_error.PNG](attachment:semantic_error.PNG)
#
# You can ignore the first few lines of this message. You need to focus on the very last line here. That is the line that begins with <b style="color:red">ERROR:</b>. This message will tell you what is wrong with your code so that you can hopefully fix it.

# On the other hand, if you make any **syntax or runtime errors**, you might see an error message similar to the one below:
#
# ![syntax_error.PNG](attachment:syntax_error.PNG)
#
# Try figuring out by yourself, what this error message is telling you. As the course progresses, you will learn how to read the Traceback from your error messages. For now, try to avoid making syntax errors, and if you are unable to fix your code, attend office hours and have a TA or Peer Mentor look at your code.

# ## Submission and Grading:
#
# After you finish answering all the questions, just click on `Kernel` -> `Restart & Run All` instead of running the last couple of cells. This will ensure that all your cells are run fresh, and that your notebook is saved before it is exported for submission.
#
# After you finish this project, you will have to submit it via [Gradescope](https://www.gradescope.com/), just as you did for [P1](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/tree/main/p1). The Gradescope autograder will run some additional **hidden tests**, and your final grade will be based off those tests. These hidden tests will verify that your submission satisfies the requirements of the [rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/tree/main/p2/rubric.md), and will make deductions according to the rubric.
#
# If you completed the project with a **partner**, make sure to add their name by clicking "Add Group Member" in Gradescope when uploading the P2 zip file. It is **not** enough if you include this information in this notebook. You **must** also add them on Gradescope.
#
# <div><img src="attachment:add_group_member.png" width="800"/></div>
#
# **Remember to check Gradescope twenty to thirty minutes after you make your submission.** That is roughly how long the Gradescope autograder will take to grade your submission, and the score that you see displayed on Gradescope after the tests run will be your **final project score**. If you lose points for any reason, you may fix the errors in your notebook and resubmit. If you are unsure why you are losing points in a project, please contact a TA or Peer Mentor.

# + [markdown] deletable=false editable=false
# ## Project questions:

# +
# This line is a comment because it starts with a pound sign (#). That 
# means Python ignores it. A comment is just for a human reading the
# code. This project involves 20 small problems to give you practice
# with operators, types, boolean logic, and variables assignment. 
# We'll give you directions on what to do for each problem.

# + [markdown] deletable=false editable=false
# **Question 1:** What does the expression `44 * 5` evaluate to?

# +
course_num = 44 * 5 # we did this one for you

course_num

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** What does the expression `350 - 31` evaluate to?

# +
# replace the ... with the correct expression, similar to the answer for Question 1.
# INCORRECT ANSWER: grad_course_num = 319 --> this is considered HARDCODING.
grad_course_num = 350 - 31

grad_course_num

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** If you have 2023 eggs, and can put 12 eggs in one carton, how many cartons can you fill completely? Write the appropriate expression to answer this question.
# **Hint**: Use the floor division (`//`) operator to answer this.

# +
# replace the ... with the correct expression, similar to the answer for Question 1.
# INCORRECT ANSWER: num_cartons = 168 --> this is considered HARDCODING.
num_cartons = 2023 // 12

num_cartons

# + deletable=false editable=false
grader.check("q3")

# + [markdown] deletable=false editable=false
# **Question 4:** What does `type` of `22 * 10` evaluate to?

# +
data_type = type(22 * 10) # we did this one for you

data_type

# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** What does `type` of `220 // 9` evaluate to?

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# INCORRECT ANSWER: data_type = int --> this is considered HARDCODING.
data_type = type(220 // 9)

data_type

# + deletable=false editable=false
grader.check("q5")

# + [markdown] deletable=false editable=false
# **Question 6:** What does `type` of `2200 / 10` evaluate to?

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# INCORRECT ANSWER: data_type = float --> this is considered HARDCODING.
data_type = type(2200 / 10)

data_type

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** What does `type` of `"220"` evaluate to? Note the **quotes**.

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# INCORRECT ANSWER: data_type = str --> this is considered HARDCODING.
data_type = type("220")

data_type

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Question 8:** What does `type` of `True` evaluate to?

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# INCORRECT ANSWER: data_type = bool --> this is considered HARDCODING.
data_type = type(True)

data_type

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** What does `type` of `"True"` evaluate to? Note the **quotes**.

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# DO NOT HARCODE the final type value.
# see questions 4 through 8 for examples of HARDCODING.
data_type = type("True")

data_type

# + deletable=false editable=false
grader.check("q9")

# + [markdown] deletable=false editable=false
# **Question 10:** What does `type` of `319 > 220` evaluate to?

# +
# replace the ... with the correct answer, similar to the answer for Question 4.
# DO NOT HARDCODE the final type value.
# see questions 4 through 8 for examples of HARDCODING.
data_type = type(319 > 220)

data_type

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Question 11:** Fix the expression `":-(" * 3 + ":-)" * 5`, to display *2 sad smileys* ":-(" and *20 happy smileys* ":-)".

# +
# replace the ... with the correct expression
# INCORRECT ANSWER (see below): 
# smileys = ':-(:-(:-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-):-)' --> this is considered HARDCODING.
smileys = (":-(" * 2) + (":-)" * 20) # fix this expression

smileys

# + deletable=false editable=false
grader.check("q11")

# + [markdown] deletable=false editable=false
# **Question 12:** Fix the expression `20 + 23` to use string concatenation to display `"2023"`. Note the **quotes**.

# +
# replace the ... with the correct expression
# INCORRECT ANSWER: curr_year = "2023" --> this is considered HARDCODING.

curr_year = "20" + "23" # fix this expression

curr_year

# + deletable=false editable=false
grader.check("q12")

# + [markdown] deletable=false editable=false
# **Question 13:** What is the *volume* of a cube with a side length of 6? You **must** use the variable `cube_side` in your solution.
#
# **Hint**: Use the exponent (\*\*) operator to answer this. 

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THIS VARIABLE AS IT IS
cube_side = 6

# +
# replace the ... with the correct expression. We expect you to use the above variable.
# INCORRECT ANSWER: cube_volume = 216 --> this is considered HARDCODING.
cube_volume = cube_side**3

cube_volume

# + deletable=false editable=false
grader.check("q13")

# + [markdown] deletable=false editable=false
# **Question 14:** What is the *volume* of a cylinder with a **height** of *3* and **radius** of *19*? You **must** define, initialize, and use the variables `cylinder_height` and `cylinder_radius` in your solution. You **must** use the variable `pi` in your solution.

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THIS VARIABLE AS IT IS
pi = 3.14

# +
# replace the ... with the correct expression. We expect you to use the variable `pi` defined above.
# we expect you to define, initalize, and use the variables `cylinder_height` and `cylinder_radius`.
# INCORRECT ANSWER: cylinder_volume = 3400.62 --> this is considered HARDCODING.

# create the required variables here
pi = 3.14
cylinder_height = 3
cylinder_radius = 19
cylinder_volume = pi * cylinder_radius ** 2 *cylinder_height

cylinder_volume

# + deletable=false editable=false
grader.check("q14")

# + [markdown] deletable=false editable=false
# ### Boolean Word Problems
#
# We're now going to do a few word problems. The most important skill you're going to learn in this class is translating English sentences to code. This will be good practice!
#
# Here are simple example translations between English phrases and comparison operators:
#
# "x is at most y" or "x is no more than y" &rarr; `x <= y`  
# "x is less than y" or "x is below y" or "x is under y" &rarr; `x < y`  
# "x is at least y" &rarr; `x >= y`  
# "x is more than y" or "x is above y" &rarr; `x > y`  
# "x is equal to y" &rarr; `x == y`  
# "y is within the range of x and z" or "y is in between x and z" &rarr; `x <= y <= z`
#
# You can use the above translations as verification for your q15 and q16 solutions.

# + [markdown] deletable=false editable=false
# **Question 15:** Suppose, the *safe operation weight limit* for a trailer is *3000 lbs*. Grace's trailer weighs *2000 lbs*. To safely operate the trailer, Grace needs to ensure that her trailer weight is *at most* the operation weight limit. How can Grace figure out if she can safely operate her truck? You **must not** change the variables' values.
#
# **Hint**: Use the appropriate comparison operator.

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THESE VARIABLES AS THEY ARE
TRAILER_LIMIT = 3000 # constants are typically stored in variable names with all capital case letters
trailer_weight = 2000
# -

# replace the ... with the correct expression
# we expect you to use the above variables
# INCORRECT ANSWER: safe_operation = True --> this is considered HARDCODING.
TRAILER_LIMIT = 3000 # constants are typically stored in variable names with all capital case letters
trailer_weight = 2000
safe_operation = trailer_weight <= TRAILER_LIMIT
safe_operation

# + deletable=false editable=false
grader.check("q15")

# + [markdown] deletable=false editable=false
# **Question 16:** To safely pull a trailer of weight 2000 lbs, Rahul's truck should weigh between 1000 and 3000 lbs. How can Rahul figure out if his truck is heavy enough to operate the trailer? You **must not** change the variables' values.
#
# **Hint**: Use the appropriate comparison operator.

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THESE VARIABLES AS THEY ARE
LOWER_LIMIT = 1000 # constants are typically stored in variable names with all capital case letters
UPPER_LIMIT = 3000 # constants are typically stored in variable names with all capital case letters
truck_weight = 1500

# +
# replace the ... with the correct expression
# we expect you to use the above variables.
# INCORRECT ANSWER: safe_operation = True --> this is considered HARDCODING.
LOWER_LIMIT = 1000 # constants are typically stored in variable names with all capital case letters
UPPER_LIMIT = 3000 # constants are typically stored in variable names with all capital case letters
truck_weight = 1500
safe_operation = LOWER_LIMIT <= truck_weight <= UPPER_LIMIT

safe_operation

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** Carlos wants to go trick-or-treating. To do so he must either make a costume *or* buy a costume. Also, he must walk around *and* have chocolates at home. Given the below variable initializations, Carlos currently isn't successful with trick-or-treating. Change exactly *one variable's initial value* to help Carlos go trick-or-treating. You **must not** change the expression.
#
# ```python
# make_costume = False
# buy_costume = True
#
# walk_around = False
# have_chocolates = True
#
# success = (make_costume or buy_costume) and (walk_around and have_chocolates)
# ```

# +
# change EXACTLY ONE variable's initial value to help Carlos go trick-or-treating
make_costume = False
buy_costume = True

walk_around = True
have_chocolates = True


# + deletable=false editable=false
# DO NOT EDIT THIS CELL, JUST RUN THIS CELL TO TEST YOUR VARIABLES
success = (make_costume or buy_costume) and (walk_around and have_chocolates)

success

# + deletable=false editable=false
grader.check("q17")

# + [markdown] deletable=false editable=false
# **Question 18:** Angel wants to buy either a bright and long shirt or a short and dark shirt. Currently, they are getting `True` for *success*, even though they have only found a long and dark shirt. Fix the Boolean expression to help them make a correct shirt selection. You **must not** change the values of the variables.
#
# ```python
# short = False
# dark = True
#
# success = (dark and not short) or (short and dark)
# ```

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THESE VARIABLES AS THEY ARE
short = False
dark = True

# +
# fix the below Boolean expression to help Angel make a correct shirt selection
short = False
dark = True
success = (dark and short) or (not short and not dark) 

success

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** *red*, *green*, and *blue* are the primary colors. How can we correct the expression `color == "red" or "green" or "blue"` to correctly verify whether `color` is a primary color? You **must not** change the color variable's value.
#
# **Hint**: In Lab-P2, there was a section on "Correct way to write boolean expressions". Now would be a good time to go back and refresh that.

# + deletable=false editable=false
# DO NOT EDIT THIS CELL, KEEP THIS VARIABLE AS IT IS
color = "blue"

# +
# INCORRECT ANSWER: primary_color = True --> this is considered HARDCODING.
primary_color = color == "red" or color == "green" or color == "blue" # fix this expression

primary_color

# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** Students *Alice*, *Bob*, *Chang*, and *Divya* have exam scores of 31, 35, 34, and 35. The expression `alice_score + bob_score + chang_score + divya_score / 4` produces incorrect student average. How can we fix this expression to compute the correct average score? You **must** define, initialize, and use the score variables mentioned in the incorrect expression.
#
# **Hint**: To override default operator order precedence, parentheses can be used, similar to PEMDAS.

# +
# create the required variables here
alice_score = 31
bob_score = 35
chang_score = 34
divya_score = 35

# we expect you to define, initialize, and use the score variables mentioned in the original expression
# INCORRECT ANSWER: average_score = 33.75 --> this is considered HARDCODING.
average_score = (alice_score + bob_score + chang_score + divya_score) / 4 # fix this expression

average_score

# + deletable=false editable=false
grader.check("q20")

# + deletable=false editable=false
grader.check("general_deductions")

# + deletable=false editable=false
grader.check("summary")

# + [markdown] deletable=false editable=false
# ## Submission
# It is recommended that at this stage, you Restart and Run all Cells in your notebook.
# That will automatically save your work and generate a zip file for you to submit.
#
# **SUBMISSION INSTRUCTIONS**:
# 1. **Upload** the zipfile to Gradescope.
# 2. If you completed the project with a **partner**, make sure to **add their name** by clicking "Add Group Member"
# in Gradescope when uploading the zip file.
# 3. Check **Gradescope** results as soon as the auto-grader execution gets completed.
# 4. Your **final score** for this project is the score that you see on **Gradescope**.
# 5. You are **allowed** to resubmit on Gradescope as many times as you want to.
# 6. **Contact** a TA/PM if you lose any points on Gradescope for any **unclear reasons**.

# + [code] deletable=false editable=false
# running this cell will create a new save checkpoint for your notebook
from IPython.display import display, Javascript
display(Javascript('IPython.notebook.save_checkpoint();'))

# + [code] deletable=false editable=false
# !jupytext --to py p2.ipynb

# + [code] deletable=false editable=false
public_tests.check_file_size("p2.ipynb")
grader.export(pdf=False, run_tests=False, files=["p2.py"])

# + [markdown] deletable=false editable=false
#  
