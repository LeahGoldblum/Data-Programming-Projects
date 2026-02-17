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
grader = otter.Notebook("p7.ipynb")

# + editable=false
import public_tests

# +
# PLEASE FILL IN THE DETAILS
# enter none if you don't have a project partner
# you will have to add your partner as a group member on Gradescope even after you fill this

# project: p7
# submitter: 9030140256
# partner: NETID2
# hours: 16

# + [markdown] deletable=false editable=false
# # Project 7: Soccer Stars

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project you will demonstrate how to:
#
# - Write programs to interpret data present in csv files,
# - Use lists and dictionaries effectively to manage data,

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `public_tests.py`. If you are curious about how we test your code, you can explore this file, and specifically the function `get_expected_json`, to understand the expected answers to the questions.

# + [markdown] deletable=false editable=false
# <h2 style="color:red">Warning (Note on Academic Misconduct):</h2>
#
# Under any circumstances, **no more than two students are allowed to work together on a project** as mentioned in the course policies. If your code is flagged by our code similarity detection tools, **both partners will be responsible** for sharing/copying the code, even if the code is shared/copied by one of the partners with/from other non-partner student(s). Note that each case of plagiarism will be reported to the Dean of Students with a zero grade on the project. **If you think that someone cannot be your project partner then don’t make that student your lab partner.**
#
# **<font color = "red">Project partners must submit only one copy of their project on Gradescope, but they must include the names of both partners.</font>**

# + [markdown] deletable=false editable=false
# ## Project Description:
#
# In this project, we will analyze data in [`soccer_stars.csv`](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/blob/main/p7/soccer_stars.csv). This dataset has some data on nearly 20,000 soccer stars who play in the top soccer leagues across the world. The statistics in this dataset are obained from the video game [FC'24](https://www.ea.com/games/ea-sports-fc/fc-24) (formerly the FIFA series) and was collected from the website [https://sofifa.com/](https://sofifa.com/). We will look at various statistics about your favorite players and teams, and identify their strengths and weaknesses.

# + [markdown] deletable=false editable=false
# ## Dataset:
#
# A small portion of the dataset `soccer_stars.csv` is reproduced here:
#
# ID|Name|Age|Nationality|Team|League|Value|Wage|Attacking|Movement|Defending|Goalkeeping|Overall rating|Position|Height|Preferred foot
# --|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--
# 239085|E. Haaland|22|Norway|Manchester City|Premier League (England)|€185M|€340K|78.6|83.6|38.0|10.4|91|ST|195cm|Left
# 231747|K. Mbappé|24|France|Paris Saint Germain|Ligue 1 (France)|€181.5M|€230K|83.0|92.4|30.7|8.4|91|ST|182cm|Right
# 192985|K. De Bruyne|32|Belgium|Manchester City|Premier League (England)|€103M|€350K|82.4|77.6|63.0|11.2|91|CM|181cm|Right
# 202126|H. Kane|29|England|FC Bayern München|Bundesliga (Germany)|€119.5M|€170K|88.0|74.0|43.3|10.8|90|ST|188cm|Right
# 192119|T. Courtois|31|Belgium|Real Madrid|La Liga (Spain)|€63M|€250K|17.2|58.0|18.0|86.6|90|GK|199cm|Left

# + [markdown] deletable=false editable=false
# The dataset contains the following information about each player:
# - `ID` : the **unique ID** used by FC'24 for identifying each player,
# - `Name` : the **name** of the player,
# - `Age` : the **age** of the player,
# - `Nationality` : the **national team** the player represents,
# - `Team` : the **football club** that the player represents,
# - `League`: the **football league** that the player's club is a part of,
# - `Value` : the **value** of the player in the transfer market (in **Euros**),
# - `Wage` : the **weekly wages** earned by the player as per their contract (in **Euros**),
# - `Attacking` : the **total attacking stats** of the player (out of **100.0**),
# - `Movement` : the **total movement stats** of the player (out of **100.0**),
# - `Defending` : the **total defending stats** of the player (out of **100.0**),
# - `Goalkeeping` : the **total goalkeeping stats** of the player (out of **100.0**),
# - `Overall rating` : the **overall rating** of the player (out of **100**),
# - `Position` : the player's **favored position** on the soccer field,
# - `Height` : the **height** of the player (in **centimeters**),
# - `Preferred foot` : the player's **favored foot**.
#
# **Please go through [Lab-P7](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/tree/main/lab-p7) before starting this project.** The lab introduces some useful techniques necessary for parsing the dataset and for answering questions in this project.

# + [markdown] deletable=false editable=false
# ## Project Requirements:
#
# You **may not** hardcode indices in your code unless specified in the question. If you are not sure what hardcoding is, here is a simple test you can use to determine whether you have hardcoded:
#
# *If we were to change the data (e.g. add more soccer players, remove some players, change their statistics, or swap some columns or rows), would your code still find the correct answer to the question as it is asked?*
#
# If your answer to that question is *No*, then you have likely hardcoded something. Please reach out to TAs/PMs during office hours to find out how you can **avoid hardcoding**.
#
# In general, all your functions and code must be **case sensitive** unless the function or question description **explicitly** says otherwise.
#
# **Store** your final answer for each question in the **variable specified for each question**. This step is important because Otter grades your work by comparing the value of this variable against the correct answer.
#
# For some of the questions, we'll ask you to write (then use) a function to compute the answer.  If you compute the answer **without** creating the function we ask you to write, the Gradescope autograder will **deduct** points, even if the way you did it produced the correct answer.
#
# #### Required Functions:
#
# - `format_euros`
# - `cell`
# - `average_stat_by_position`
# - `best_player_of_team_at_position`
# - `best_starting_players_of`
#
#
# In this project, you will also be required to define certain **data structures**. If you do not create these data structures exactly as specified, the Gradescope autograder will **deduct** points, even if the way you did it produced the correct answer.
#
# #### Required Data Structures:
#
# - `players` 
#     
# Students are only allowed to use Python commands and concepts that have been taught in the course prior to the release of P7. Therefore, **you should not use the pandas module**. The Gradescope autograder will **deduct** points otherwise.
#
# For more details on what will cause you to lose points during code review and specific requirements, please take a look at the [Grading rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/blob/main/p7/rubric.md).

# + [markdown] deletable=false editable=false
# ## Incremental Coding and Testing:
#
# You should always strive to do incremental coding. **Incremental coding enables you to avoid challenging bugs.** Always write a few lines of code and then test those lines of code, before proceeding to write further code. You can call the `print` function to test intermediate step outputs.
#
# We also recommend you do incremental testing: make sure to run the local tests as soon as you are done with a question. This will ensure that you haven't made a big mistake that might potentially impact the rest of your project solution. Please refrain from making multiple submissions on Gradescope for testing individual questions' answers. Instead use the local tests, to test your solution on your laptop.
#
# That said, it is **important** that you check the Gradescope test results as soon as you submit your project on Gradescope. Test results on Gradescope are typically available somewhere between 15 to 30 minutes after the submission.
#
# Also, remember to check with the [P7 rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/blob/main/p7/rubric.md) to verify that you will not be losing any points during manual review.

# + [markdown] deletable=false editable=false
# ## Project Questions and Functions:
# -

# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import csv


# + [markdown] deletable=false editable=false
# First, read the data stored in `soccer_stars.csv`. You **must** read the csv file and then get the header and rows (and store them into `csv_header` and `csv_rows` variables). You will **lose points** if you use any other names to store these variables.
#
# **Note**: It is recommended that you just copy/paste the code from your Lab-P7 notebook. However, instead of reading data from `small_soccer_stars.csv`, this time, you **must** read the data from `soccer_stars.csv`.
# -

# copy/paste the definition of `process_csv` here
def process_csv(filename):
    example_file = open(filename, encoding="utf-8")
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    example_file.close()
    return example_data


# +
# use process_csv to read 'soccer_stars.csv'
csv_data = process_csv('soccer_stars.csv')

# split the header and other rows into appropriate variables
csv_header = csv_data[0]
csv_rows = csv_data[1:]

print(csv_header)
print(csv_rows[0:2])


# + [markdown] deletable=false editable=false
# We will now copy/paste some function and data structure definitions from Lab-P7 to get us started with the project.

# + [markdown] deletable=false editable=false
# ### Function 1: `format_euros(euros)` 
#
# You **must** write a helper function that takes in a **string** representing the `Wage` or `Value` (such as `"€250K"` or `"€158.5M"`), and converts it into an **int**.
#
# For example, `"€250K"` should be converted to `250000`, and `"€158.5M"` should be converted to `158500000`.
#
# You can **assume** that the first character of the input string `euros` always starts with the Euro symbol (€), and that **if** the last character is either `"K"` or `"M"`, it represents the preceeding number in thousands or millions, respectively. Note that the last character **need not** be `"K"` or `"M"` in all inputs. If the last character is not one of these letters, then the entire input string (except the starting €) can be **assumed** to be an **integer**.
#
# **Note:** You may copy/paste your definition of `format_euros` from Lab-P7 here.
# -

# define the `format_euros` function here
def format_euros(euros):
    last_character = euros[-1]
    euro_num = 0
    if last_character == "K":
        euro_num = (float(euros[1:-1])*1000)
    elif last_character == "M":
        euro_num = (float(euros[1:-1])*1000000)
    else:
        euro_num = (float(euros[1:]))
    return euro_num


# + deletable=false editable=false
grader.check("format_euros")


# + [markdown] deletable=false editable=false
# ### Function 2: `cell(row_idx, col_name)` 
#
# This function must take in a row index, `row_idx` and a column name, `col_name` as its inputs, and return the value in `soccer_stars.csv` stored there. There is **no missing data** in this dataset, so you do **not** have to worry about returning `None` for **missing data**.
#
# Your `cell` function **must** also typecast the values based on column names. These are the expected data types for each of the columns:
#
# - `ID` : **int**,
# - `Name` : **str**,
# - `Age` : **int**,
# - `Nationality` : **str**,
# - `Team` : **str**,
# - `League` : **str**,
# - `Value` : **int**,
# - `Wage` : **int**,
# - `Attacking` : **float**,
# - `Movement` : **float**,
# - `Defending` : **float**,
# - `Goalkeeping` : **float**,
# - `Overall rating` : **int**,
# - `Position` : **str**,
# - `Height` : **int**,
# - `Preferred foot` : **str**.
#
# Make special care to convert the `Height` into an **int** by slicing off the units, and to convert the `Wage` and `Value` into **ints** using the `format_euros` helper function.
#
# **Note:** You may copy/paste your definition of `cell` from Lab-P7 here. Since the variables `csv_header` and `csv_rows` are defined in this notebook to be data in `soccer_stars.csv`, the same function from Lab-P7 will now read the data from `soccer_stars.csv` instead of `small_soccer_stars.csv`.
# -

# define the `cell` function here
def cell(row_idx, col_name):
    col_idx = csv_header.index(col_name) # extract the `col_idx` from the `col_name`
    val = csv_rows[row_idx][col_idx] # extract the value in `csv_rows`
    if val == " ":
        return None
    elif col_name in ['ID', "Age",'Overall rating']:
        val = int(val)
    elif col_name in ['Attacking', 'Movement', 'Defending', 'Goalkeeping']:
        val = float(val)
    elif col_name in ['Nationality', 'Team', 'League', 'Name', 'Position', 'Preferred foot']:
        val = str(val)
    elif col_name in ['Height']:
        val = int(val[:-2])
    elif col_name in ['Value', 'Wage']:
        val = format_euros(val)
    return val


# + deletable=false editable=false
grader.check("cell")

# + [markdown] deletable=false editable=false
# ### Data Structure 1: `players` 
#
# You **must** now define a data structure `players` that stores all the data in `soccer_stars.csv` after processing the values. This data structure **must** be a **dictionary** of **dictionaries**. The **outer dictionary** must map each player `ID` to another **dictionary** which contains all the data about the player with that `ID`. Each **inner dictionary** corresponding to each player must map the **column names** to their **values** for that player.
#
# #### For the rest of the project, you MUST access data from `soccer_stars.csv` ONLY using this data structure `players`.
#
# The first few elements of `players` **must** look like this:
#
# ```python
# {239085: {'ID': 239085,
#           'Name': 'E. Haaland',
#           'Age': 22,
#           'Nationality': 'Norway',
#           'Team': 'Manchester City',
#           'League': 'Premier League (England)',
#           'Value': 185000000,
#           'Wage': 340000,
#           'Attacking': 78.6,
#           'Movement': 83.6,
#           'Defending': 38.0,
#           'Goalkeeping': 10.4,
#           'Overall rating': 91,
#           'Position': 'ST',
#           'Height': 195,
#           'Preferred foot': 'Left'},
#  231747: {'ID': 231747,
#           'Name': 'K. Mbappé',
#           'Age': 24,
#           'Nationality': 'France',
#           'Team': 'Paris Saint Germain',
#           'League': 'Ligue 1 (France)',
#           'Value': 181500000,
#           'Wage': 230000,
#           'Attacking': 83.0,
#           'Movement': 92.4,
#           'Defending': 30.7,
#           'Goalkeeping': 8.4,
#           'Overall rating': 91,
#           'Position': 'ST',
#           'Height': 182,
#           'Preferred foot': 'Right'},
#  192985: {'ID': 192985,
#           'Name': 'K. De Bruyne',
#           'Age': 32,
#           'Nationality': 'Belgium',
#           'Team': 'Manchester City',
#           'League': 'Premier League (England)',
#           'Value': 103000000,
#           'Wage': 350000,
#           'Attacking': 82.4,
#           'Movement': 77.6,
#           'Defending': 63.0,
#           'Goalkeeping': 11.2,
#           'Overall rating': 91,
#           'Position': 'CM',
#           'Height': 181,
#           'Preferred foot': 'Right'},
#  ...
# }
# ```
#
# **Note:** You may copy/paste your definition of `players` from Lab-P7 here. Since the variables `csv_header` and `csv_rows` are defined in this notebook to be data in `soccer_stars.csv`, the same code from Lab-P7 will now use the data from `soccer_stars.csv` instead of `small_soccer_stars.csv` to define `players`.
# -

# define the `players` data structure here
# but do NOT display it as it is very large
players = {}
for row_idx in range(len(csv_rows)):
    
    player_id = cell(row_idx, 'ID')
    player_row_idx = row_idx
    row_idx = player_id
    
    #players[row_idx] = player_id
    player = {}
    for column in csv_header:
        column_value = cell(player_row_idx, column) 
        player[column] = column_value
        players[row_idx] = player
# players


# + deletable=false editable=false
grader.check("players")

# + [markdown] deletable=false editable=false
# You are all set! You are now ready to start solving the questions.

# + [markdown] deletable=false editable=false
# **Question 1:** What are the **all** the statistics of the player with the `ID` *158023*?
#
# Your output **must** be a **dict** whose keys are **all** the **column names** in the dataset, and the corresponding values are the values under that column for the player with the given `ID`.
# -

# compute and store the answer in the variable 'stats_player_158023', then display it
stats_player_158023 = players[158023]
stats_player_158023

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** Find **all** the statistics of the **highest** valued (`Value`) player.
#
# Your output **must** be a **dict** whose keys are **all** the **column names** in the dataset, and the corresponding values are the values under that column for the player with the **highest** `Value`.
#
# You do **not** have to worry about any ties. There is a **unique** player in the dataset with the highest `Value`.

# +
# compute and store the answer in the variable 'highest_valued_stats', then display it
max_player_value = 0
id_max_player_value = None

for player_id in players:
    player_stats = players[player_id]
    player_value = player_stats['Value']
    if id_max_player_value == None or player_value > max_player_value:
        id_max_player_value = player_id
        max_player_value = player_value
        
highest_valued_stats = players[id_max_player_value]
highest_valued_stats

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** What is the `Nationality` of the player with the **highest** `Wage`?
#
# You do **not** have to worry about any ties. There is a **unique** player in the dataset with the highest `Wage`.

# +
# compute and store the answer in the variable 'highest_wage_nationality', then display it
max_player_wage = 0
id_max_player_wage = None
max_player_nationality = None

for player_id in players:
    player_stats = players[player_id]
    player_wage = player_stats['Wage']
    if id_max_player_wage == None or player_wage > max_player_wage:
        id_max_player_wage = player_id
        max_player_wage = player_wage
        player_nationality = player_stats['Nationality']
        
highest_wage_nationality = player_nationality
highest_wage_nationality

# + deletable=false editable=false
grader.check("q3")

# + [markdown] deletable=false editable=false
# **Question 4:** What is the favored `Position` of the player with the **highest** `Wage`?
#
# You **must** not recompute the player with the highest `Wage`. Instead, you can use the `ID` you found in your answer to **Question 3**, and just find the `Position` of that player. If you did not store the `ID` of that player in **Question 3**, go back and **modify** your answer there, so you can directly use it here.
# -

# compute and store the answer in the variable 'highest_wage_position', then display it
player_stats = players[id_max_player_wage]
player_highest_wage_position = player_stats['Position']
highest_wage_position = player_highest_wage_position
highest_wage_position
    

# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** Find all the teams (`Team`) that belong to the `League` *Premier League (England)*.
#
# Your output **must** be a **list** of **strings** with **no duplicates**. The order does **not** matter.

# +
# compute and store the answer in the variable 'premier_league_teams', then display it
premier_league_teams = {}
for player_id in players:
    all_players_id = players[player_id]
    player_team = all_players_id['Team'] 
    league_player = all_players_id ['League']
    if league_player == 'Premier League (England)':
        premier_league_teams[player_team] = league_player


premier_league_teams = list(premier_league_teams.keys())
premier_league_teams

# + deletable=false editable=false
grader.check("q5")

# + [markdown] deletable=false editable=false
# **Question 6:** Find the **number** of players with each `Preferred foot`. 
#
# Your output **must** be a **dictionary** that maps each `Preferred Foot` (i.e., *Right* and *Left*) to the **number** of players with that `Preferred foot`. Your output **must** look like this:
#
# ```python
# {'Left': 4585, 'Right': 15082}
# ```
#
# You **must** not **hardcode** the feet (i.e., *Right* and *Left*) in your answer. Instead, you must extract that information from the dictionary `players`.  Remember that you **must** extract all the information from the csv file only using the data structure `players`.

# +
# compute and store the answer in the variable 'preferred_foot_count', then display it
preferred_foot_count = {}

for player_id in players:
    all_players_id = players[player_id]
    players_foot = all_players_id['Preferred foot']
    if players_foot not in preferred_foot_count:
        preferred_foot_count[players_foot] = 1
    else:
        preferred_foot_count[players_foot] += 1
    
#     preferred_foot_count[players_foot] = 0
# preferred_foot_count


# for player_id in players:
#     all_players_id = players[player_id]
#     players_foot = all_players_id['Preferred foot']
#     preferred_foot_count[players_foot] += 1



preferred_foot_count

# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** What is the **average** `Overall rating` of *Right* vs *Left* footed players (`Preferred foot`)?
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'Left': 64.3494002181025, 'Right': 63.14427794722185}
# ```
#
# You **must** not **hardcode** the feet (i.e., *Right* and *Left*) in your answer. Instead, you must extract that information from the dictionary `players`.
#
# **Hint**: You should first compute a dictionary that computes the **total** `Overall rating` of *Left* and *Right* footed players, then divide the values in this dictionary by the corresponding values in the dictionary you computed in **Question 6** to find the **average**.

# +
preferred_foot_avg_overall = {}

for player_id in players:
    player = players[player_id]
    player_preferred_foot = player["Preferred foot"]
    player_rating = player["Overall rating"]
    
    if player_preferred_foot not in preferred_foot_avg_overall:
        preferred_foot_avg_overall[player_preferred_foot] = player_rating
    else:
        preferred_foot_avg_overall[player_preferred_foot] += player_rating

for foot in preferred_foot_avg_overall:
    preferred_foot_avg_overall[foot] /= preferred_foot_count[foot]
preferred_foot_avg_overall

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Food for thought:** We notice that Left-footed players have a slightly higher `Overall rating` on **average** than Right-footed players. Can you explain what is going on here?
# -

# Food for thought is an entirely OPTIONAL exercise
# you may leave your thoughts here as a comment if you wish to


# + [markdown] deletable=false editable=false
# ### Soccer Positions
#
# We will now analyze the various **positions** on the soccer field. Before we get started, it will be helpful to have at least a rough idea as to what the different **positions** are. Here is an image that explains where each **position** is expected to play on the soccer field:
# -

# <div><img src="attachment:positions.jpg" style="height: 400px;"/></div>

# + [markdown] deletable=false editable=false
# The **bottom** of the image is the team's goalpost, and the **top** is the opposite team's goalpost. The positions closer to the **bottom** of the image are broadly tasked with **protecting** their team's goal, while the positions closer to the **top** of the image are tasked with **scoring** goals against the opposition.
#
# Apart from the *Goalkeeper* (**GK**), the **five** players closest to their own goalpost (**LWB**, **LB**, **CB**, **RB**, **RWB**) are called *Defenders*. The **five** players in the middle of the field (**CDM**, **LM**, **CM**, **RM**, **CAM**) are called *Midfielders*, and the **four** players closest to the oppposite team's goalpost (**LW**, **CF**, **RW**, **ST**) are called the *Forwards*.
#
# With this brief explanation, you are ready to tackle more questions in this project!

# + [markdown] deletable=false editable=false
# **Question 8:** For **each** `Position`, find the **number** of players who play in that `Position`.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'ST': 3126,
#  'CM': 1076,
#  'GK': 2084,
#  'CF': 62,
#  'CAM': 2911,
#  ...
# }
# ```
#
# You **must** not **hardcode** the positions in your answer. Instead, you must extract that information from the dictionary `players`.
# -

# compute and store the answer in the variable 'positions_count', then display it
positions_count = {}
for player_id in players:
    all_players_id = players[player_id]
    players_postition = all_players_id['Position']
    positions_count[players_postition] = 0
positions_count
for player_id in players:
    all_players_id = players[player_id]
    players_postition = all_players_id['Position']
    positions_count[players_postition] += 1
positions_count

# + deletable=false editable=false
grader.check("q8")

# + [markdown] deletable=false editable=false
# **Question 9:** Find the **average** `Age` of players in **each** `Position`.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'ST': 23.2552783109405,
#  'CM': 24.481412639405203,
#  'GK': 23.379078694817657,
#  'CF': 28.822580645161292,
#  'CAM': 22.032291308828583,
#  ...
# }
# ```
#
# You **must** not **hardcode** the positions in your answer. Instead, you must extract that information from the dictionary `players`.

# +
# compute and store the answer in the variable 'positions_avg_age', then display it
positions_avg_age = {}
for player_id in players:
    player = players[player_id]
    player_position = player["Position"]
    player_age = player["Age"]
    
    if player_position not in positions_avg_age:
        positions_avg_age[player_position] = player_age
    else:
        positions_avg_age[player_position] += player_age
        
for position in positions_avg_age:
    positions_avg_age[position] /= positions_count[position]

positions_avg_age    

# + deletable=false editable=false
grader.check("q9")

# + [markdown] deletable=false editable=false
# **Food for thought:** Notice that players at the position **CF** (Center Forward) are significantly older on average than players who play at other positions. Similarly, players at positions **LW** (Left Wing Forward), and **RW** (Right Wing Forward) are also older on average than players at other positions. Can you explain this phenomenon? On average do you notice any patterns in the ages of the players as we move up the field from the *Defenders* to the *Forwards*?
# -

# Food for thought is an entirely OPTIONAL exercise
# you may leave your thoughts here as a comment if you wish to


# + [markdown] deletable=false editable=false
# **Question 10:** Find the **average** `Height` of players in **each** `Position`.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'ST': 182.81222008957133,
#  'CM': 179.23234200743494,
#  'GK': 188.366122840691,
#  'CF': 178.24193548387098,
#  'CAM': 176.6496049467537,
#  ...
# }
# ```
#
# You **must** not **hardcode** the positions in your answer. Instead, you must extract that information from the dictionary `players`.

# +
# compute and store the answer in the variable 'positions_avg_height', then display it
positions_avg_height = {}
for player_id in players:
    player = players[player_id]
    player_position = player["Position"]
    player_height= player["Height"]
    
    if player_position not in positions_avg_height:
        positions_avg_height[player_position] = player_height
    else:
        positions_avg_height[player_position] += player_height
        
for position in positions_avg_height:
    positions_avg_height[position] /= positions_count[position]

positions_avg_height   

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Food for thought:** Notice that players at the position **GK** (Goalkeeper) tend to be the tallest by far, followed by players at the position **CB** (Center Back). Can you explain why this is the case? Also, notice that although the positions **CF** (Center Forward) and **ST** (Striker) appear very close to each other in the Position map, there is a significant difference in their average heights (and average ages). What does that tell you about the roles of the players at these positions?
# -

# Food for thought is an entirely OPTIONAL exercise
# you may leave your thoughts here as a comment if you wish to


# + [markdown] deletable=false editable=false
# ### Function 3: `average_stat_by_position(col_name)` 
#
# This function must take in a `col_name` of a **numerical** column (such as `"Age"`, `"Overall rating"`, `"Value"`, `"Wage"`, `"Attacking"`, `"Movement"`, `"Defending"`, `"Goalkeeping"`, or `"Height"`), and then return a **dict** that maps **each** `Position` in the dataset to the **average** value under the `col_name` of all the players at that `Position`.
#
# You may assume that the values under the given `col_name` are always **numerical** (i.e., **int** or **float**).
#
# **Hint**: Recall that the dictionary `players` represents each player as a **dict**. So, if you wanted to extract a particular `stat` of a player, you can **index** directly **without looping** through the **dict**.
# -

# define the `average_stat_by_position` function here
def average_stat_by_position(col_name): 
    stat_by_position = {}
    
    for player_id in players:
        player = players[player_id]
        player_position = player["Position"]
        player_col_name = player[col_name]
        

        if player_position not in stat_by_position:
            stat_by_position[player_position] = player_col_name
        else:
            stat_by_position[player_position] += player_col_name

    for position in stat_by_position:
        
         stat_by_position[position] /= positions_count[position]

    return stat_by_position  
        

# + deletable=false editable=false
grader.check("average_stat_by_position")

# + [markdown] deletable=false editable=false
# **Question 11:** Find the **average** `Attacking` stat of players in **each** `Position`.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'ST': 56.65591810620609,
#  'CM': 57.14814126394047,
#  'GK': 14.351439539347414,
#  'CF': 64.66774193548387,
#  'CAM': 55.027825489522414,
#  ...
# }
# ```
#
# You **must** use the `average_stat_by_position` function to answer this question.
# -

# compute and store the answer in the variable 'positions_avg_attacking', then display it
positions_avg_attacking = average_stat_by_position("Attacking")
positions_avg_attacking

# + deletable=false editable=false
grader.check("q11")

# + [markdown] deletable=false editable=false
# **Food for thought:** Which positions have the highest average `Attacking` stat? Do you notice any anomalies? Notice that among the *Defenders*, the position **CB** (Center Back) has a significantly **lower** `Attacking` stat than other positions such as **LB** (Left Back), **RB** (Right Back), **LWB** (Left Wing Back), and **RWB** (Right Wing Back). Similarly, note that the **Midfield** position **CM** (Center Midfield) has a higher average than more offensive positions such as **CAM** (Center Attacking Midfield) and **ST** (Striker). Can you explain this?
# -

# Food for thought is an entirely OPTIONAL exercise
# you may leave your thoughts here as a comment if you wish to


# + [markdown] deletable=false editable=false
# **Question 12:** Find the **average** `Movement` stat of players in **each** `Position`.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'ST': 64.60620601407543,
#  'CM': 65.4442379182156,
#  'GK': 38.34232245681379,
#  'CF': 67.86129032258067,
#  'CAM': 68.510958433528,
#  ...
# }
# ```
#
# You **must** use the `average_stat_by_position` function to answer this question.
# -

# compute and store the answer in the variable 'positions_avg_movement', then display it
positions_avg_movement = average_stat_by_position('Movement')
positions_avg_movement

# + deletable=false editable=false
grader.check("q12")

# + [markdown] deletable=false editable=false
# **Food for thought:** Which positions have the highest average `Movement` stat? Notice that the players on the wings have higher `Movement` on average than players in the center of the field. Can you explain this? Do you notice any **correlations** between the `Movement` and another statistic that we have already looked at? If so, can you explain why that **correlation** exists?
# -

# Food for thought is an entirely OPTIONAL exercise
# you may leave your thoughts here as a comment if you wish to


# + [markdown] deletable=false editable=false
# **Question 13:** **Which** `Position` has the **highest** `Defending` stat on **average**?
#
# Your output **must** be a **string** that represents the `Position` with the **highest** `Defending` stat. You do **not** have to worry about breaking any ties. There is a **unique** `Position` with the **highest** `Defending` stat.
#
# You **must** use the `average_stat_by_position` function to answer this question.

# +
# compute and store the answer in the variable 'best_defending_position', then display it
avg_defending_pos = 0
# avg_defending_id = None
# avg_defending_id == None or

for position in average_stat_by_position('Defending'):
    avg_defending_val = average_stat_by_position('Defending')[position]
    
    if avg_defending_val > avg_defending_pos:
        avg_defending_pos = avg_defending_val
        best_defending_position = position
best_defending_position

# + deletable=false editable=false
grader.check("q13")


# + [markdown] deletable=false editable=false
# ### Forming Teams
#
# For the rest of this project, we will attempt to construct **teams** for the various teams in our dataset.
#
# To start with, it would be useful to identify the **best** player at any given `Position` for a `Team`. We could get more fancy here, by using a stat such as `Defending`, or perhaps a combination of stats such as `Defending`, `Movement`, and `Height` to identify the **best** *CB*, and use stats such as `Attacking` to identify the **best** *CF*.
#
# However, we will keep it **simple** here, and just use the `Overall rating` to determine the **best** players.

# + [markdown] deletable=false editable=false
# ### Function 4: `best_player_of_team_at_position(position, team)` 
#
# This function must take in a `position` as well as a `team` and then return the `ID` of the player who plays for the given `team`, and has the **highest** `Overall rating` among **all other players** who play at that `position` for the same `team`.
#
# In case two players are **tied** with the **same** `Overall rating`, the ties **must** be broken in favor of the player with the **smaller** `ID`.
#
# In case there are **no** players who play at the given `position` for the given `team`, then the function **must** return `None`.
#
# **Note**: It is important to find the `ID` of the best player, and **not** something like their `Name`. This is because if we have the `ID`, we can then use the `players` **dict** to extract **all** statistics about the player.

# +
# define the `best_player_of_team_at_position` function here
def best_player_of_team_at_position(position, team):
    id_best_player_position = None
    
    for player_id in players:
        all_players_id = players[player_id]
        player_team = all_players_id['Team']
        player_positions = all_players_id['Position']
        player_overall_rate = all_players_id['Overall rating']
        if player_team == team and player_positions == position:
            if id_best_player_position == None or player_overall_rate > players[id_best_player_position]['Overall rating']:
                id_best_player_position = player_id
            if player_overall_rate == players[id_best_player_position]['Overall rating']:
                if player_id < id_best_player_position:
                    id_best_player_position = player_id
    return id_best_player_position
            
            
    
    
        

# + deletable=false editable=false
grader.check("best_player_of_team_at_position")

# + [markdown] deletable=false editable=false
# **Question 14:** **What** is the `ID` of the **best** (highest `Overall rating`) player at `Position` *CDM* for the `team` *Manchester United*?
#
# You **must** use the `best_player_of_team_at_position` function to answer this question.
# -

# compute and store the answer in the variable 'best_cdm_man_utd_id', then display it
best_cdm_man_utd_id = best_player_of_team_at_position('CDM','Manchester United' )
best_cdm_man_utd_id

# + deletable=false editable=false
grader.check("q14")

# + [markdown] deletable=false editable=false
# **Question 15:** **What** are the statistics of the **best** (highest `Overall rating`) player at `Position` *RW* for the `team` *Liverpool*?
#
# You **must** use the `best_player_of_team_at_position` function to answer this question.
# -

# compute and store the answer in the variable 'best_rw_liverpool', then display it
id_best_rw_liverpool = best_player_of_team_at_position('RW', 'Liverpool')
best_rw_liverpool = players[id_best_rw_liverpool]
best_rw_liverpool

# + deletable=false editable=false
grader.check("q15")

# + [markdown] deletable=false editable=false
# ### Forming Teams
#
# Every team would like to **start** their games with their **best** players on the field at each position. Now that we have a function for finding the **best** player at any `Position`, we can use it identify the **best** player at **each** `Position` for any `Team`.
#
# There are a few problems with this approach. For a start, *most* teams will **not** have players for **each** `Position`. For example, a team which uses a *Striker* (**ST**) might not need a *Center Forward* (**CF**) as well. Alternately, a team might play **two** *Center Midfielders* (**CM**) and **not** use any *Right Midfielders* (**RM**) or *Left Midfielders* (**LM**) at all.
#
# For now, we will not deal with these complexities. We will simply pick the **best** player for **each** `Position`, to form a team. We also won't concern ourselves with **how many** players are picked in total.

# + [markdown] deletable=false editable=false
# ### Function 5: `best_starting_players_of(team)` 
#
# This function must take in a `team` and return a **dict** mapping each `Position` to the `ID` of the **best player** (i.e., player with the **highest** `Overall`) at that `Position` for the given `team`.
#
# In the case where two players are **tied** with the **same** `Overall rating`, the ties **must** be broken in favor of the player with the **smaller** `ID`.
#
# In the case where there are **no** players who play at a particular `Position` for the given `team`, the `Position` must **not** appear as a **key** in the **dictionary**.

# +
# define the `best_starting_players_of` function here
all_positions = positions_count.keys()

def best_starting_players_of(team):
    best_position_player_dict = {}
    
    for position in all_positions:
        id_best_position = best_player_of_team_at_position(position, team)
        if id_best_position == None:
            continue
        else:
            best_position_player_dict[position] = id_best_position
    return best_position_player_dict
        


# + deletable=false editable=false
grader.check("best_starting_players_of")

# + [markdown] deletable=false editable=false
# **Question 16:** **Who** are the **best starting players** of the `Team` *Paris Saint Germain*?
#
# Your output **must** be a **dict** that maps each `Position` for which *Paris Saint Germain* has a player to the `ID` of the **best** player (i.e., **highest** `Overall rating`) they have at that position.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'CDM': 200888,
#  'GK': 230621,
#  'LW': 202166,
#  'RW': 231443,
#  'RB': 235212,
#  'CAM': 255253,
#  'CB': 207865,
#  'RM': 264652,
#  'CM': 199556,
#  'LB': 252145,
#  'ST': 231747}
# ```
#
# You **must** use the `best_starting_players_of` function to answer this question.
# -

# compute and store the answer in the variable 'best_starters_of_psg', then display it
best_starters_of_psg = best_starting_players_of('Paris Saint Germain')
best_starters_of_psg

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** **What** are the names (`Name`) of the **best starting players** of the `Team` *FC Bayern München*?
#
# Your output **must** be a **dict** that maps each `Position` for which *FC Bayern München* has a player to the `Name` of the **best** player (i.e., **highest** `Overall rating`) they have at that position.
#
# Your output **must** be a **dict** that looks as follows:
#
# ```python
# {'CDM': 'J. Kimmich',
#  'LM': 'K. Coman',
#  'GK': 'O. Kahn',
#  'RW': 'B. Sarr',
#  'RWB': 'P. Lahm',
#  'LWB': 'F. Krätzig',
#  'CAM': 'J. Musiala',
#  'CB': 'M. de Ligt',
#  'RM': 'S. Gnabry',
#  'CM': 'L. Goretzka',
#  'ST': 'H. Kane'}
# ```
#
# You **must** use the `best_starting_players_of` function to answer this question.
#
# **Note**: If you cannot type the characters of the team's name using your keyboard, you can just copy/paste it from the question above.
# -

best_starters_of_bayern = {}
for player_id in players:
    player = players[player_id]
    player_name = all_players_id['Name']
    player_position = all_players_id ['Position']
    player_team = all_players_id ['Team']
    if player == 'FC Bayern München':
        best_of_bayern = best_starting_players_of('FC Bayern München')['Position']
    best_starters_of_bayern[player_position] = player_name
best_starters_of_bayern
    

# + deletable=false editable=false
grader.check("q17")

# + [markdown] deletable=false editable=false
# **Question 18:** What is the **cumulative** `Value` of the **bench** of the `Team` *FC Barcelona*?
#
# The **bench** refers to the players in the squad of the team (i.e., players whose `Team` is *FC Barcelona*), who are **not** one of the **best starting players**. The **cumulative** `Value` refers to the **sum** of the `Value` of **all** the players on the **bench**.
#
# **Hint**: You can use the `best_starting_players_of` function to identify the **best starting players** of *FC Barcelona*, and then identify all the players from that team, who are **not** among its best starting players.

# +
# compute and store the answer in the variable 'bench_value_barcelona', then display it
# best_starting_players_of('FC Barcelona')
bench_value_barcelona = 0
best_players_barcelona=list(best_starting_players_of('FC Barcelona').values())
for player_id in players:
    if player_id not in best_players_barcelona:
        player_stats = players[player_id]
        player_value = player_stats['Value'] 
        player_team = player_stats['Team']
        if player_team == 'FC Barcelona':
            bench_value_barcelona += player_value

print(bench_value_barcelona)

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** **Find** the **average** `Attacking` stat of the **best starting players** for **each** `Team` in the `League` *Premier League (England)*.
#
# Your output **must** be a **dict** that maps **each** `Team` in the `League` *Premier League (England)* to the **sum** of `Attacking` stats of all the **best starting players** of that `Team` **divided** by the **number** of **best starting players** of that `Team`.
#
# Recall that you already made a **list** of all the teams in *Premier League (England)* to answer **Question 5**. You can loop through that **list** instead of computing the teams in *Premier League (England)* again, or looping unnecessarily over a larger data structure.
#
# **Hint**: You can loop through all the teams in the given league, find the **best starting players** of **each** team, then have a nested loop to find the **average** of the `Attacking` stat of all the **best starting players** of that team.

# +
# compute and store the answer in the variable 'avg_attacking_prem_league', then display it
avg_attacking_prem_league = {}
# sum_of_attack = 0
# count = 0
# attck_val_count = {}

for team in premier_league_teams:
    premier_starter_players = best_starting_players_of(team)
    sum_of_attack = 0
    count = 0

    for position, player_id in premier_starter_players.items():
        if player_id is not None: #avg_attacking_prem_league:
            sum_of_attack += players[player_id]['Attacking']
            count += 1
    if count > 0:
        attck_avg = sum_of_attack / count
        avg_attacking_prem_league[team] = attck_avg
#     attck_val = players[player_id]['Attacking']
#     if attck_val not in attck_val_count:
#         attck_val_count[attck_val] = 1
#     else:
#         attck_val_count[attck_val] += 1
        
# for val in avg_attacking_prem_league:
#     avg_attacking_prem_league[val] /= attck_val_count
avg_attacking_prem_league


# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** **Which** `Team` in the `League` *Premier League (England)*  has the **highest** **average** `Attacking` stat among its **best starting players**?
#
# You do **not** have to worry about breaking any ties. There is a **unique** `Team` whose **best starting players** have the **highest** **average** `Attacking` stat.
#
# You **must** **not** recompute the **average** `Attacking` stat of the **best starting players** of all teams in the *Premier League (England)*. Instead, use the dictionary that you have already computed to answer this question.
# -

# compute and store the answer in the variable 'best_attackers_prem_league', then display it
max_premier_attack = max(avg_attacking_prem_league,key=avg_attacking_prem_league.get)
best_attackers_prem_league = max_premier_attack
best_attackers_prem_league

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
# !jupytext --to py p7.ipynb

# + [code] deletable=false editable=false
public_tests.check_file_size("p7.ipynb")
grader.export(pdf=False, run_tests=False, files=["p7.py"])

# + [markdown] deletable=false editable=false
#  
