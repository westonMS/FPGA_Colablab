import ipywidgets as widgets
from ipywidgets import GridspecLayout
from ipywidgets import AppLayout, Button, Layout, jslink, IntText, IntSlider

# function of creating button widget
def create_expanded_button(description, button_style, width="100px"):
    return Button(
        description=description,
        button_style=button_style,
        layout=Layout(height="auto", width=width),
    )


# function of creating grid layout
def create_grid(Col1, Col2, Func, _1_0, _1_1, _2_0, _2_1, _3_0, _3_1, _4_0, _4_1):
    grid = GridspecLayout(5, 4, width="470px")
    grid[0, 0] = create_expanded_button(str(Col1), "info")
    grid[0, 1] = create_expanded_button(str(Col2), "info")
    grid[0, 2] = create_expanded_button(str(Func), "info")
    grid[1, 0] = create_expanded_button(str(_1_0), "info")
    grid[1, 1] = create_expanded_button(str(_1_1), "info")
    grid[2, 0] = create_expanded_button(str(_2_0), "info")
    grid[2, 1] = create_expanded_button(str(_2_1), "info")
    grid[3, 0] = create_expanded_button(str(_3_0), "info")
    grid[3, 1] = create_expanded_button(str(_3_1), "info")
    grid[4, 0] = create_expanded_button(str(_4_0), "info")
    grid[4, 1] = create_expanded_button(str(_4_1), "info")
    for i in range(1, 5):
        grid[i, 2] = widgets.BoundedIntText(
            min=0, max=1, layout=Layout(height="auto", width="100px")
        )
        grid[0, 3] = create_expanded_button("Click to Check", "warning", width="150px")
    for i in range(1, 5):
        grid[i, 3] = create_expanded_button(" ", "warning", width="150px")
    return grid


# creates variable grid size
def create_gridTEST(num_input, input_string, func):
    """
    - num_input = number of inputs in the function
    - input_string = a string of all the default values and input names that are passed in (ex: AB000011011)
    """
    num_row = (2**num_input) + 1
    num_col = num_input + 2
    grid = GridspecLayout(num_row, num_col, width=str(num_col * 120) + "px")

    # creates the default values for the different input combos of the truth table
    for i in range(0, num_row):
        for j in range(0, num_input):
            val = str(input_string[0])
            grid[i, j] = create_expanded_button(val, "info")
            input_string = input_string[1:]

    # creates the click to check button as well as the userinput section of the table
    for i in range(1, num_row):
        grid[i, num_input] = widgets.BoundedIntText(
            min=0, max=1, layout=Layout(height="auto", width="100px")
        )
        grid[0, num_col - 1] = create_expanded_button(
            "Click to Check", "warning", width="150px"
        )

    # creates the output section of the truth table to know if you're right or not
    for i in range(1, num_row):
        grid[i, num_col - 1] = create_expanded_button(" ", "warning", width="150px")

    grid[0, num_input] = create_expanded_button(func, "info")
    return grid


# function of creating a 2input grid layout
def create_grid_NOT(Col1, Func, _1_0, _2_0):
    grid = GridspecLayout(3, 3, width="365px")
    grid[0, 0] = create_expanded_button(str(Col1), "info")
    grid[0, 1] = create_expanded_button(str(Func), "info")
    grid[1, 0] = create_expanded_button(str(_1_0), "info")
    grid[2, 0] = create_expanded_button(str(_2_0), "info")
    for i in range(1, 3):
        grid[i, 1] = widgets.BoundedIntText(
            min=0, max=1, layout=Layout(height="auto", width="100px")
        )
        grid[0, 2] = create_expanded_button("Click to Check", "warning", width="150px")
    for i in range(1, 3):
        grid[i, 2] = create_expanded_button(" ", "warning", width="150px")
    return grid


# function of checking if your input answer is right or not
def CheckAnswer1_1(grid, val1, val2, val3, val4):
    if grid[1, 2].value == val1:
        grid[1, 3].button_style = "Success"
        grid[1, 3].description = "Correct!"
    else:
        grid[1, 3].button_style = "Danger"
        grid[1, 3].description = "Wrong! Submit again"

    if grid[2, 2].value == val2:
        grid[2, 3].button_style = "Success"
        grid[2, 3].description = "Correct!"
    else:
        grid[2, 3].button_style = "Danger"
        grid[2, 3].description = "Wrong! Submit again"

    if grid[3, 2].value == val3:
        grid[3, 3].button_style = "Success"
        grid[3, 3].description = "Correct!"
    else:
        grid[3, 3].button_style = "Danger"
        grid[3, 3].description = "Wrong! Submit again"

    if grid[4, 2].value == val4:
        grid[4, 3].button_style = "Success"
        grid[4, 3].description = "Correct!"
    else:
        grid[4, 3].button_style = "Danger"
        grid[4, 3].description = "Wrong! Submit again"


# function for checking if the input answer is right or not for the NOT gate
def CheckAnswer1_3(grid, val1, val2):
    if grid[1, 1].value == val1:
        grid[1, 2].button_style = "Success"
        grid[1, 2].description = "Correct!"
    else:
        grid[1, 2].button_style = "Danger"
        grid[1, 2].description = "Wrong! Submit again"
    if grid[2, 1].value == val2:
        grid[2, 2].button_style = "Success"
        grid[2, 2].description = "Correct!"
    else:
        grid[2, 2].button_style = "Danger"
        grid[2, 2].description = "Wrong! Submit again"


# Create grids containing buttons in this part for AND gate
grid1_1 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_1[0, 2] = create_expanded_button("F= AB", "info")

# Create grids containing buttons in this part for OR gate
grid1_2 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_2[0, 2] = create_expanded_button("F=A+B", "info")

# Create grids containing buttons in this part for NOT gate
grid1_3 = create_grid_NOT("A", "F", 0, 1)
grid1_3[0, 1] = create_expanded_button("F=!A", "info")

# Create grids containing buttons in this part for NOR gate
grid1_4 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_4[0, 2] = create_expanded_button("F=FINISH THIS", "info")

# Create grids containing buttons in this part for NAND gate
grid1_5 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_5[0, 2] = create_expanded_button("F=FINISH THIS", "info")

# Create grids containing buttons in this part for XOR gate
grid1_6 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_6[0, 2] = create_expanded_button("F=A^B", "info")

# Create grids containing buttons in this part for XNOR gate
grid1_7 = create_grid("A", "B", "F", 0, 0, 0, 1, 1, 0, 1, 1)
grid1_7[0, 2] = create_expanded_button("F=~(A^B)", "info")


gridTEST = create_gridTEST(2, "ABF00011011", "F=TEST")
# THIS CAN PROBABLY BE PLACED IN THE CREATE FUNCTION WITH F AS AN ARGUMENT ABCF000001010011100101110111


# LOOK INTO HAVING THE CHECK ANSWER BUTTON DO DIFFERENT THINGS
# DON'T LIKE THIS IMPLEMENTATION. Find a way to only need one 'on_button_clicked' function

# Process when clicking the "Check" button
# AND
def on_button_clicked(self):
    CheckAnswer1_1(grid1_1, 0, 0, 0, 1)


# OR
def on_button_clicked2(self):
    CheckAnswer1_1(grid1_2, 0, 1, 1, 1)


# NOT
def on_button_clicked3(self):
    CheckAnswer1_3(grid1_3, 1, 0)


# NOR
def on_button_clicked4(self):
    CheckAnswer1_1(grid1_4, 1, 0, 0, 0)


# NAND
def on_button_clicked5(self):
    CheckAnswer1_1(grid1_5, 1, 1, 1, 0)


# XOR
def on_button_clicked6(self):
    CheckAnswer1_1(grid1_6, 0, 1, 1, 0)


# XNOR
def on_button_clicked7(self):
    CheckAnswer1_1(grid1_7, 1, 0, 0, 1)


def CheckAnswerTEST(grid, num_inputs, input):
    for i in len(input):
        if grid[i + 1, num_inputs].value == input[i]:
            grid[i + 1, num_inputs + 1].button_style = "Success"
            grid[i + 1, num_inputs + 1].description = "Correct!"
        else:
            grid[i + 1, num_inputs + 1].button_style = "Danger"
            grid[i + 1, num_inputs + 1].description = "Wrong! Submit again"


# TEST
def on_button_clicked8(self):
    CheckAnswerTEST(gridTEST, 2, "1111")
