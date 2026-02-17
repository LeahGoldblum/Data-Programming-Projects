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
grader = otter.Notebook("p6.ipynb")

# + editable=false
import public_tests

# +
# PLEASE FILL IN THE DETAILS
# enter none if you don't have a project partner
# you will have to add your partner as a group member on Gradescope even after you fill this

# project: p6
# submitter: 9030140256
# partner: NETID2
# hours: 12

# + [markdown] deletable=false editable=false
# # Project 6: Power Generators in Wisconsin

# + [markdown] deletable=false editable=false
# ## Learning Objectives:
#
# In this project, you will demonstrate how to:
#
# * access and utilize data in CSV files,
# * process real world datasets,
# * use string methods and sorting function / method to order data.
#
# Please go through [Lab-P6](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/tree/main/lab-p6) before working on this project. The lab introduces some useful techniques related to this project.

# + [markdown] deletable=false editable=false
# ## Testing your code:
#
# Along with this notebook, you must have downloaded the file `public_tests.py`. If you are curious about how we test your code, you can explore this file, and specifically the function `get_expected_json`, to understand the expected answers to the questions.

# + [markdown] deletable=false editable=false
# ## Project Description:
#
# In this project, we will use Python to analyze Electric Power Generation within the state of Wisconsin. The data used in this project has been adapted from [this dataset](https://www.eia.gov/electricity/data/eia860m/) maintained by the **US Energy Information Administration**. `power_generators.csv` has data of all 613 power generators within the state of Wisconsin that were in operation as of August 2023. This file includes information about the capacities, locations, and the technologies used by the generators.

# + [markdown] deletable=false editable=false
# ## Dataset:
#
# A small portion of the dataset `power_generators.csv` you will be working with for this project is reproduced here:

# + [markdown] deletable=false editable=false
# entity_id|entity_name|plant_id|plant_name|generator_id|county|net_summer_capacity|net_winter_capacity|technology|latitude|longitude
# ---|---|---|---|---|---|---|---|---|---|---
# 13781|Northern States Power Co - Minnesota|1756|Saxon Falls|1|Iron|0.5|0.5|Conventional Hydroelectric|46.5392|-90.3742
# 13781|Northern States Power Co - Minnesota|1756|Saxon Falls|2|Iron|0.5|0.6|Conventional Hydroelectric|46.5392|-90.3742
# 20847|Wisconsin Electric Power Co|1775|Brule|1|Florence|1.3|1.3|Conventional Hydroelectric|45.9472|-88.2189
# 20847|Wisconsin Electric Power Co|1775|Brule|2|Florence|2|2|Conventional Hydroelectric|45.9472|-88.2189
# 20847|Wisconsin Electric Power Co|1775|Brule|3|Florence|2|2|Conventional Hydroelectric|45.9472|-88.2189

# + [markdown] deletable=false editable=false
# Each row of data represents a **single** generator. The columns contain the following data about each generator (along with the correct data type you **must** represent it as):
#
# 1. `entity_id` - the **ID** of the **entity** that operates the Power Generator (`int`)
# 2. `entity_name` - the **name** of the **entity** that operates the Power Generator (`str`)
# 3. `plant_id` - the **ID** of the **Power Plant** hosting the Power Generator (`int`)
# 4. `plant_name` - the **name** of the **Power Plant** hosting the Power Generator (`str`)
# 5. `generator_id` - the **ID** of the specific **Power Generator** within its Power Plant (`str`)
# 6. `county` - the **name** of the **county** that the **Power Plant** is located in (`str`)
# 7. `net_summer_capacity` - the maximum **capacity** of the **Power Generator** (in units of MW) during the Summer months (`float`)
# 8. `net_winter_capacity` - the maximum **capacity** of the **Power Generator** (in units of MW) during the Winter months (`float`)
# 9. `technology` - the **technology** used by the **Power Generator** (`str`)
# 10. `latitude` - the **latitude** where the **Power Plant** is located (`float`)
# 11. `longitude` - the **longitude** where the **Power Plant** is located (`float`)
#
# You can find more details on the dataset in [Lab-P6](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/tree/main/lab-p6).

# + [markdown] deletable=false editable=false
# ## Project Requirements:
#
# You **may not** hardcode indices in your code unless specified in the question. If you are not sure what hardcoding is, here is a simple test you can use to determine whether you have hardcoded:
#
# *If we were to change the data (e.g. add more power generators, remove some power generators, or swap some columns or rows), would your code still find the correct answer to the question as it is asked?*
#
# If your answer to that question is *No*, then you have likely hardcoded something. Please reach out to TAs/PMs during office hours to find out how you can **avoid hardcoding**.
#
# **Store** your final answer for each question in the **variable specified for each question**. This step is important because Otter grades your work by comparing the value of this variable against the correct answer.
#
# For some of the questions, we'll ask you to write (then use) a function to compute the answer.  If you compute the answer **without** creating the function we ask you to write, the Gradescope autograder will **deduct** points, even if the way you did it produced the correct answer.
#
# Required Functions:
# - `process_csv`
# - `cell`
# - `find_entities_with_phrase`
# - `num_generators_by`
# - `find_indices_within`
# - `median`
# - `total_summer_capacity_of`
# - `avg_winter_capacity_of`
#     
# Students are only allowed to use Python commands and concepts that have been taught in the course prior to the release of P6. Therefore, **you should not use concepts/modules such as dictionaries, or the pandas module, to name a few examples**. Otherwise, the Gradescope autograder will **deduct** points, even if the way you did it produced the correct answer.
#
# For more details on what will cause you to lose points during code review and specific requirements, please take a look at the [Grading rubric](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-f23-projects/-/blob/main/p6/rubric.md).
# -

# <h2 style="color:red">Warning (Note on Academic Misconduct):</h2>
#
# Under any circumstances, **no more than two students are allowed to work together on a project** as mentioned in the course policies. If your code is flagged by our code similarity detection tools, **both partners will be responsible** for sharing/copying the code, even if the code is shared/copied by one of the partners with/from other non-partner student(s). Note that each case of plagiarism will be reported to the Dean of Students with a zero grade on the project. **If you think that someone cannot be your project partner then don’t make that student your lab partner.** 
# <font color = "red">Project partners must submit only one copy of their project on Gradescope, but they must include the names of both partners.</font>

# + [markdown] deletable=false editable=false
# ## Questions and Functions:
#
# Let us start by importing all the modules we will need for this project.
# -

# it is considered a good coding practice to place all import statements at the top of the notebook
# please place all your import statements in this cell if you need to import any more modules for this project
import csv


# + [markdown] deletable=false editable=false
# ### Function 0: `cell`
#
# Copy and paste the `process_csv` and `cell` functions from your Lab-P6 notebook to the cell below.
#
# You are expected to call the `process_csv` function correctly, and read the data on `power_generators.csv`. After reading the file, define the `csv_header`, and `csv_rows` variables as in Lab-P6, and define the `cell` function.
#
# **Important:** You **must** only use the `cell` function to extract data from the dataset. If you extract any data without explicitly using this function, the Gradescope autograder will **deduct points**.
# -

def process_csv(filename):
    example_file = open(filename, encoding="utf-8")
    example_reader = csv.reader(example_file)
    example_data = list(example_reader)
    example_file.close()
    return example_data


# +
# this call to process_csv reads the data in "power_generators.csv"
csv_data = process_csv("power_generators.csv")


# -

csv_header = csv_data[0] # A list of the column headers

csv_rows = csv_data[1:]


def cell(row_idx, col_name):
    col_idx = csv_header.index(col_name)
    val = csv_rows[row_idx][col_idx]
    if val == " ":
        return None
    elif col_name in ['entity_id', "plant_id"]:
        val = int(val)
    elif col_name in ['net_summer_capacity', 'net_winter_capacity', 'latitude', 'longitude']:
        val = float(val)
    elif col_name in ["entity_name", "plant_name", "generator_id", "county", "technology"]:
        val = str(val)
    return val



# + deletable=false editable=false
grader.check("cell")

# + [markdown] deletable=false editable=false
# **Question 1:** What **unique** technologies (`technology`) are used by the power generators in Wisconsin?
#
# Your output **must** be a *list* which stores all the **unique** technologies (i.e., without any duplicates). The order **does not** matter.

# +
# compute and store the answer in the variable 'technologies', then display it

technologies = []
for idx in range(len(csv_rows)):
    technology = cell(idx, "technology")
    if technology == "":
        continue 
    technologies.append(technology)
    
technologies = list(set(technologies))
technologies

# + deletable=false editable=false
grader.check("q1")

# + [markdown] deletable=false editable=false
# **Question 2:** How many power generators are in the `county` *Dane*?

# +
# compute and store the answer in the variable 'count_dane', then display it
count_dane = 0
for idx in range(len(csv_rows)):
    dane_cont = cell(idx, "county")
    if dane_cont == "Dane":
        count_dane +=1

count_dane

# + deletable=false editable=false
grader.check("q2")

# + [markdown] deletable=false editable=false
# **Question 3:** What is the **total** `net_summer_capacity` of all the power generators in Wisconsin?
#
# Your answer **must** be a **float** that represents the total `net_summer_capacity`. You **must** **ignore** all power generators whose `net_summer_capacity` data is **missing**.
# -

# compute and store the answer in the variable 
#'total_summer_capacity', then display it
total_summer_capacity = 0 
for idx in range(len(csv_rows)):
    if cell(idx, "net_summer_capacity") == None:
        continue
    if cell(idx, "net_summer_capacity") != None:
        total_summer_capacity += cell(idx, "net_summer_capacity")
total_summer_capacity

# + deletable=false editable=false
grader.check("q3")


# + [markdown] deletable=false editable=false
# ### Function 1: `find_entities_with_phrase(phrase)`
#
# We require you to complete the below function. You can review string methods from any of these lecture slides: [Mike](https://canvas.wisc.edu/courses/374263/files/folder/Mikes_Lecture_Notes/Lec13_Strings), [Gurmail](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/tree/main/f23/Gurmail_Lecture_Notes/13_Strings), or [Cole](https://git.doit.wisc.edu/cdis/cs/courses/cs220/cs220-lecture-material/-/tree/main/f23/Cole_Lecture_Notes/13_Strings).
# -

def find_entities_with_phrase(phrase):
    """
    find_entities_with_phrase(phrase) returns a list of all the entity names
    WITHOUT duplicates that CONTAIN the substring
    (case insensitive match) `phrase`.
    """
    #pass # replace with your code
    # TODO: create an empty list
    # TODO: check if the entity name string contains phrase (case insensitive match)
    # TODO: if so, add these entity names to the list (the entity names should be as in the dataset)
    # TODO: return your list of entity names after removing duplicates
    entities_with_phrase = []
    for idx in range(len(csv_rows)):
        entity_name = cell(idx, "entity_name")
       
        if phrase.lower() in entity_name.lower():

            entities_with_phrase.append(entity_name)
            
    return list(set(entities_with_phrase))


# + deletable=false editable=false
grader.check("find_entities_with_phrase")

# + [markdown] deletable=false editable=false
# **Question 4:** Find all entity names (`entity_name`) that contain the string *"Madison"* (case insensitive).
#     
# Your output **must** be a **list**. The order **does not** matter. You **must** use the `find_entities_with_phrase` function to answer this question.

# +
# compute and store the answer in the variable 'madison_entities', 
#then display it
madison_entities = find_entities_with_phrase("Madison")

print(madison_entities)


# + deletable=false editable=false
grader.check("q4")

# + [markdown] deletable=false editable=false
# **Question 5:** Find all entity names (`entity_name`) that contain **either** *"Wisconsin"* **or** *"Power"* (case insensitive).
#
# If an entity's name contains **both** *"Wisconsin"* and *"Power"*, then the `entity_name` must be included **only once** in your list.
#
# Your output **must** be a **list**. The order **does not** matter.
#
# **Hint**: You can use the `find_entities_with_phrase` function on *"Wisconsin"* and *"Power"* to answer this question.
# -

# compute and store the answer in the variable 'entities_contain_wisconsin_power', then display it
wisco_phrase = find_entities_with_phrase("Wisconsin")
powers_phrase = find_entities_with_phrase("Power")
wisco_phrase.extend(powers_phrase)
entities_contain_wisconsin_power = list(set(wisco_phrase))
entities_contain_wisconsin_power

# + deletable=false editable=false
grader.check("q5")

# + [markdown] deletable=false editable=false
# **Question 6:** Find all entity names (`entity_name`) that contain **both** *"Solar"* **and** *"LLC"* (case insensitive).
#
# Your output **must** be a **list**. The order **does not** matter.
#
# **Hint**: You can use the `find_entities_with_phrase` function on *"Solar"* and *"LLC"* to answer this question.

# +
# compute and store the answer in the variable 'entities_contain_solar_llc', then display it
solar_entities = find_entities_with_phrase("Solar")
llc_entities = find_entities_with_phrase("LLC")

entities_contain_solar_llc =[]


for ll_entity_name in llc_entities:
    if ll_entity_name in solar_entities:
        entities_contain_solar_llc.append(ll_entity_name)

# entities_contain_solar_llc = solar_entity



entities_contain_solar_llc = list(set(entities_contain_solar_llc))
entities_contain_solar_llc


# + deletable=false editable=false
grader.check("q6")

# + [markdown] deletable=false editable=false
# **Question 7:** Find the generator IDs (`generator_id`) of all the generators that use the `technology` *"Wood/Wood Waste Biomass"* within the power plant with the `plant_id` *50614*.
#
# Your output **must** be a *list*. The IDs **must** be sorted in **descending (alphabetical) order**.
# -

# compute and store the answer in the variable 'plant_50614_generators', then display it
plant_50614_generators = []
for idx in range(len(csv_rows)):
    if cell(idx, "technology") == "Wood/Wood Waste Biomass":
        if cell(idx, "plant_id") == 50614:
            
            plant_50614_generators.append(cell(idx, "generator_id"))
            plant_50614_generators.sort(reverse=True)
plant_50614_generators

# + deletable=false editable=false
grader.check("q7")

# + [markdown] deletable=false editable=false
# **Question 8:**  What are the power plants (`plant_name`) that contain generators which use the `technology` *Conventional Hydroelectric* and have a `net_summer_capacity` greater than *5*?
#
# You **must** **ignore** all generators with **missing** `net_summer_capacity` data.
#
# Your output **must** be a *list* of **unique** plant names (`plant_name`). The names **must** be sorted in **ascending (alphabetical) order**.

# +
# compute and store the answer in the variable 'powerful_hydro_electric_plants', then display it
powerful_hydro_electric_plants = []
for idx in range(len(csv_rows)):
    if cell(idx, "technology") == "Conventional Hydroelectric":
        net_summer_cap = cell(idx, "net_summer_capacity")    
        if net_summer_cap == None:
            continue
        if net_summer_cap > 5:
            
            powerful_hydro_electric_plants.append(cell(idx, "plant_name"))                                                
            powerful_hydro_electric_plants = (list(set(powerful_hydro_electric_plants)))

            
powerful_hydro_electric_plants.sort()
powerful_hydro_electric_plants

# + deletable=false editable=false
grader.check("q8")


# + [markdown] deletable=false editable=false
# ### Function 2: `num_generators_by(entity_name)`
#
# We require you to complete the below function.
# -

def num_generators_by(entity_name):
    """
    num_generators_by(entity_name) returns the number of
    power generators operated by the given `entity_name`
    (case sensitive match).
    """
    generators_by_entity = 0

    for idx in range(len(csv_rows)):
        entity_gens = cell(idx, "entity_name")
        if entity_gens == entity_name:
            
            generators_by_entity += 1
            #generators_by_entity.count()
                
    return generators_by_entity


# + deletable=false editable=false
grader.check("num_generators_by")

# + [markdown] deletable=false editable=false
# **Question 9:** How **many** generators are operated by the entity (`entity_name`) *Madison Gas & Electric Co*?
#
# You **must** use the `num_generators_by` function to answer this question.

# +
# compute and store the answer in the variable 'num_generators_by_mge', then display it


mge_gens = num_generators_by("Madison Gas & Electric Co")
num_generators_by_mge = mge_gens
num_generators_by_mge

# + deletable=false editable=false
grader.check("q9")

# + [markdown] deletable=false editable=false
# **Question 10:** How **many** generators are operated by entities whose name (`entity_name`) **contains** the **phrase** *River* (case insensitive)?
#
# You **must** use the `num_generators_by` and `find_entities_with_phrase` functions to answer this question.

# +
# compute and store the answer in the variable 'num_generators_by_river', then display it
num_generators_by_river = 0
river_entities = find_entities_with_phrase("River")
for river_name in river_entities:
   # num_generators_by(river_name)
    num_generators_by_river += num_generators_by(river_name)

        
num_generators_by_river

# + deletable=false editable=false
grader.check("q10")

# + [markdown] deletable=false editable=false
# **Question 11:** Which entity (`entity_name`) operates the **most** number of generators within Wisconsin?
#
# You **must** use the `num_generators_by` function to answer this question. You do **not** have to worry about any ties. There is a **unique** entity with the most number of generators in the dataset.
#
# **Hint**: You must first create a list of unique entities (`entity_name`) in the dataset, then loop through them to find the entity with the most number of generators.
#
# **Extra Hint**: If you are clever about it, you can generate a list of all the unique entities using the `find_entities_with_phrase` function. You do **not** have to answer this question that way, but try to find out how you can use it here!

# +
# compute and store the answer in the variable 'most_generators_entity', then display it
most_generators_entity = None
all_entities = []
highest_gens = 0
for idx in range(len(csv_rows)):
    entity_names = cell(idx, "entity_name")
    all_entities.append(entity_names)
    unique_entities = (list(set(all_entities)))

for name in unique_entities:
    nums_generator = num_generators_by(name)
    if nums_generator > highest_gens:
        highest_gens = nums_generator
        most_generators_entity = name

most_generators_entity

# + deletable=false editable=false
grader.check("q11")


# + [markdown] deletable=false editable=false
# ### Function 3: `find_indices_within(lat_min, lat_max, long_min, long_max)` 
#
# We require you to complete the below function.

# +
def find_indices_within(lat_min, lat_max, long_min, long_max):
    """
    find_indices_within(lat_min, lat_max, long_min, long_max) returns a
    list of *row indices* of all generators located within the
    latitudes `lat_min` and `lat_max` (both inclusive) and the
    longitudes `long_min` and `long_max` (both inclusive).
    """
    #pass # replace with your code
    row_indice = []

    for idx in range(len(csv_rows)):
        lat = cell(idx, "latitude")
        long = cell(idx, "longitude")
        if lat >= lat_min:
            if lat <= lat_max:
                if long >= long_min:
                    if long <= long_max:
                        row_indice.append(idx)
    return row_indice
        
    
    

# + deletable=false editable=false
grader.check("find_indices_within")

# + [markdown] deletable=false editable=false
# **Question 12:** How **many** power generators are located **within** the *City of Milwaukee* (`42.9870 <= latitude <= 43.1936`, `-88.0636 <= longitude <= -87.8727`)?
#
# Note that simply checking if the `county` is *Milwaukee* will lead you to count generators that are within *Milwaukee County*, but not within the City. Use the coordinates given above to determine the generators that lie within the City.
#
# You **must** use the `find_indices_within` function to answer this question.
# -

# compute and store the answer in the variable 'num_generators_in_milwaukee', then display it
nums_mke_gens = find_indices_within(42.9870, 43.1936, -88.0636, -87.8727)
num_generators_in_milwaukee = len(nums_mke_gens)
num_generators_in_milwaukee

# + deletable=false editable=false
grader.check("q12")

# + [markdown] deletable=false editable=false
# **Question 13:** What are the **unique** technologies (`technology`) used by power generators located **near** the *University of Wisconsin-Madison Department of Computer Sciences* (`43.0675 <= latitude <= 43.0725`, `-89.4100 <= longitude <= -89.4000`)?
#
# You may assume that any power generator that lies within the coordinates given above are **near** the *University of Wisconsin-Madison Department of Computer Sciences*. You **must** use the `find_indices_within` function to answer this question.
#
# You **must** return a **list** of **unique** technologies. The order **does not** matter. 
# -

# compute and store the answer in the variable 'uw_madison_technologies', then display it
uw_madison_technologies = []
uw_mad_num_gens = find_indices_within(43.0675, 43.0725, -89.4100, -89.4000)
for idx in uw_mad_num_gens:
    technology = cell(idx, "technology")
    uw_madison_technologies.append(technology)
    uw_madison_technologies = list(set(uw_madison_technologies))
uw_madison_technologies

# + deletable=false editable=false
grader.check("q13")

# + [markdown] deletable=false editable=false
# **Question 14:** Which power plant (`plant_name`) in *North Wisconsin* (`44.9657 <= latitude <= 46.6989`, `-92.1908 <= longitude <= -87.6449`) has the generator with the **highest** `net_summer_capacity`?
#
# You may assume that any power generator that lies within the coordinates given above are **in** *North Wisconsin*. You **may** assume that **none** of the `net_summer_capacity` values of any of the power generators within this area are **missing**.
#
# You do **not** have to worry about any ties. There is a **unique** generator in *North Wisconsin* with the highest `net_summer_capacity`.
#
# You **must** use the `find_indices_within` function to answer this question.

# +
# compute and store the answer in the variable 'north_wisconsin_most_powerful', then display it
#all_north_plants = []
north_wisconsin_most_powerful = None
highest_power_plant = 0
north_wis_indices = find_indices_within(44.9657, 46.6989, -92.1908, -87.6449)
for idx in north_wis_indices:
    net_summer_cap = cell(idx, "net_summer_capacity") 
#     highest_power_plant = net_summer_cap
    north_plant_name = cell(idx, "plant_name")
    if north_wisconsin_most_powerful == None:
        north_wisconsin_most_powerful = north_plant_name
            
    elif highest_power_plant < net_summer_cap:
        highest_power_plant = net_summer_cap
        north_wisconsin_most_powerful = north_plant_name
north_wisconsin_most_powerful
   



    

# + deletable=false editable=false
grader.check("q14")


# + [markdown] deletable=false editable=false
# ### Function 4: `median(items)` 
#
# We require you to complete the below function. You may **copy/paste** this function from your Lab-P6 notebook.
# -

def median(items):
    """
    median(items) returns the median of the list `items`
    """
    #pass # replace with your code
    # you may copy/paste this function from your Lab-P6 notebookdef median(items):
    """
    median(items) returns the median of the list `items`
    """
    # sort the list
    sorted_list = sorted(items)
    # determine the length of the list
    list_len = len(sorted_list)
    if list_len % 2 == 1: # determine whether length of the list is odd
        # return item in the middle using indexing
        return sorted_list[list_len // 2]
    else:
        first_middle = sorted_list [list_len // 2 - 1] # use appropriate indexing
        second_middle = sorted_list [list_len // 2] # use appropriate indexing
        return (first_middle + second_middle) / 2


# + deletable=false editable=false
grader.check("median")

# + [markdown] deletable=false editable=false
# **Question 15:** What is the **median** `net_winter_capacity` of *Conventional Hydroelectric* (`technology`) power generators **near** *Lake Winnebago* (`43.6961 <= latitude <= 44.3512`, `-88.5375 <= longitude <= -88.2713`)?
#
# You may assume that any power generator that lies within the coordinates given above are **near** *Lake Winnebago*. You **may** assume that **none** of the `net_winter_capacity` values of any of the power generators within this area are **missing**.
#
# You **must** use the `find_indices_within` and `median` functions to answer this question.

# +
# compute and store the answer in the variable 'winnebago_hydro_winter_capacity', then display it

lake_winne_net_list = []


lake_winne_indices = find_indices_within(43.6961, 44.3512, -88.5375, -88.2713)
for idx in lake_winne_indices:
    net_winter_cap = cell(idx, "net_winter_capacity")
    technology = cell(idx, "technology")
    if technology == "Conventional Hydroelectric":
        lake_winne_net_list.append(net_winter_cap)

winnebago_hydro_winter_capacity = median(lake_winne_net_list)
winnebago_hydro_winter_capacity

# + deletable=false editable=false
grader.check("q15")


# + [markdown] deletable=false editable=false
# ### Function 5: `total_summer_capacity_of(plant_name)` 
#
# We **require** you to complete the below function. This function must take in a `plant_name` and return the **total** `net_summer_capacity` of all the power generators within that power plant. If a particular `plant_name` has **some** generators with **missing data**, those generators **must** be **ignored** while finding the sum.
#
# This function can be **case-sensitive**. You **only** need to consider the power plants whose names **exactly match** `plant_name`.

# +
def total_summer_capacity_of(plant_name):
    """
    total_summer_capacity_of(plant_name) returns the total
    `net_summer_capacity` of all power generators within
    the given `plant_name`; this function **ignores**
    any generator whose `net_summer_capacity` data is
    missing.
    """
    #pass # replace with your code
    total_summer_plant_cap = []
    for idx in range(len(csv_rows)):
        if plant_name == cell(idx, "plant_name"):
            net_summer_cap = cell(idx, "net_summer_capacity")
            if cell(idx, "net_summer_capacity") == None:
                continue
            else:
                total_summer_plant_cap.append(cell(idx, "net_summer_capacity"))
                total_summer_capacity_of = sum(total_summer_plant_cap)
    return total_summer_capacity_of
            
            
    

# + deletable=false editable=false
grader.check("total_summer_capacity_of")

# + [markdown] deletable=false editable=false
# **Question 16:** What is the **net summer capacity** of the **power plant** *Point Beach Nuclear Plant*?
#
# The **net summer capacity** of a **power plant** refers to the **total** `net_summer_capacity` of **all** the generators within the power plant.
#
# You **must** use the `total_summer_capacity_of` function to answer this question.
# -

# compute and store the answer in the variable 'point_beach_summer_capacity', then display it
pb_nuclear = total_summer_capacity_of("Point Beach Nuclear Plant")
point_beach_summer_capacity = pb_nuclear
point_beach_summer_capacity

# + deletable=false editable=false
grader.check("q16")

# + [markdown] deletable=false editable=false
# **Question 17:** Find the **median** of the **net summer capacities** of **all** the **power plants** in Wisconsin.
#
# The **net summer capacity** of a **power plant** refers to the **total** `net_summer_capacity` of **all** the generators within the power plant.
#
# You **must** use the `total_summer_capacity_of` function to answer this question.
#
# **WARNING**: You **must not** find the **median** across all the power **generators**. Multiple generators may belong to the same power plant. Instead, you **must** find the **median** across the **total** power generated by each **power plant**.
#
# **Hint**: You must first make a list of all the **unique** power plants (`plant_name`) in the dataset, then make a **list** of all their **total** net summer capacities (using `total_summer_capacity_of`), and finally, find the **median** of this list.

# +
# compute and store the answer in the variable 'median_summer_capacity', then display it
#median_summer_capacity = None
unique_pp = []
total_unique_pp_sum_net = []
for idx in range(len(csv_rows)):
    ppname = cell(idx, "plant_name")
    unique_pp.append(ppname)
unique_pp = list(set(unique_pp))

total_net_sum_cap = []
for items in unique_pp:
    net_sum_pp = total_summer_capacity_of (items)
    total_net_sum_cap.append(net_sum_pp)
median_summer_capacity = median(total_net_sum_cap)
# if unique_pp in total_summer_capacity_of:
#     #plant_name = unique_pp
#         total_unique_pp_sum_net.append(plant_name)
# total_unique_pp_sum_net= (list(set(total_unique_pp_sum_net)))
# print(total_unique_pp_sum_net)

median_summer_capacity

# + deletable=false editable=false
grader.check("q17")


# + [markdown] deletable=false editable=false
# ### Function 6: `avg_winter_capacity_of(technology)`
#
# We **require** you to complete the below function. This function must take in a `technology` and return the **average** (i.e., **mean**) `net_winter_capacity` of **all** the power generators which use that particular `technology`. If a particular `technology` has **some** generators with **missing data**, those generators **must** be **ignored** while finding the average (i.e., ignored in **both** the *numerator* and the *denominator*).
#
# This function can be **case-sensitive**. You **only** need to consider the technologies whose names **exactly match** `technology`.

# +
def avg_winter_capacity_of(technology):
    """
    avg_winter_capacity_of(technology)
    returns the average (mean) of `net_winter_capacity`
    of all power generators which use the given
    `technology`; generators with missing data
    are ignored.
    """    
    #pass # replace with your code
    same_tech = []
    for idx in range(len(csv_rows)):
        technologies = cell(idx, 'technology')
#         net_winter_cap = cell(idx, 'net_winter_cap')
#         if not ()
        if technologies == None:
            continue 
        if technology == technologies:
            net_winter_cap = cell(idx, 'net_winter_capacity')
            if net_winter_cap != None and technology == technologies:
                same_tech.append(net_winter_cap)
    return sum(same_tech) / len(same_tech)
    
    
#     if len(net_winter_cap) == technologies
                
            


# + deletable=false editable=false
grader.check("avg_winter_capacity_of")

# + [markdown] deletable=false editable=false
# **Question 18:** What is the **average** `net_winter_capacity` of all power generators that use the `technology` *Conventional Hydroelectric*?
#
# You **must** use the `avg_winter_capacity_of` function to answer this question.
# -

# compute and store the answer in the variable 'hydro_avg_winter_capacity', then display it
avg_tech_con_hydro = avg_winter_capacity_of('Conventional Hydroelectric')
hydro_avg_winter_capacity = avg_tech_con_hydro
hydro_avg_winter_capacity

# + deletable=false editable=false
grader.check("q18")

# + [markdown] deletable=false editable=false
# **Question 19:** Which `technology` has the **highest** `net_winter_capacity` on **average**?
#
# You **must** use the `avg_winter_capacity_of` function to answer this question. You do **not** have to worry about any ties. There is a **unique** technology with the highest `net_winter_capacity` on average.
#
# **Hint**: You already created a list of the **unique** technologies to answer Question 1. Loop through that list and find which of those technologies has the **highest** average `net_winter_capacity` (using `avg_winter_capacity_of`).

# +
# compute and store the answer in the variable 'max_winter_capacity_tech', then display it

max_cap_tech = 0
for technology in technologies:
    avg_win_cap = avg_winter_capacity_of(technology)
    if max_cap_tech < avg_win_cap:
        max_cap_tech = avg_win_cap
        
        max_winter_capacity_tech = technology
           
max_winter_capacity_tech

# + deletable=false editable=false
grader.check("q19")

# + [markdown] deletable=false editable=false
# **Question 20:** Find the **difference** between the **average** net winter capacities of the `technology` with the **highest** average and the **second highest** average.
#
# You must use the `avg_winter_capacity_of` function to answer this question.
#
# **Hint**: You have already found the `technology` with the **highest** average. You need to find the `technology` with the **second highest** average, and find the difference between their average net winter capacities using the `avg_winter_capacity_of` function.
#
# **Extra Hint**: There is also another (easier) way to solve this question. Try to find it! Reviewing Lab-P6 could help you find it.

# +
# compute and store the answer in the variable 'diff_avg_winter_capacity', then display it
sec_highest_avg = 0
for technology in technologies:
    avg_win_cap = avg_winter_capacity_of(technology)
#     if max_cap_tech < avg_win_cap:
# #         max_cap_tech = avg_win_cap
    if sec_highest_avg < avg_win_cap and max_cap_tech > avg_win_cap:
        sec_highest_avg = avg_win_cap

diff_avg_winter_capacity = max_cap_tech - sec_highest_avg
diff_avg_winter_capacity 

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
# !jupytext --to py p6.ipynb

# + [code] deletable=false editable=false
public_tests.check_file_size("p6.ipynb")
grader.export(pdf=False, run_tests=False, files=["p6.py"])

# + [markdown] deletable=false editable=false
#  
