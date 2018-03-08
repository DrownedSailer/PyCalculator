# This is a little graphical calculator program made using pygame
# It will be be capable of * / + -
# It will be simple and clean

import pygame, sys

pygame.init()
pygame.display.set_caption("PyCalculator")

size = width, height = 500, 600
screen = pygame.display.set_mode(size)
mainfont = pygame.font.Font(None, 100) # create font
cmouse = pygame.mouse.get_pos()
mouse_click = False
button_width = 165
button_height = 80
space = 2
button_width_function = button_width * .6
button_height_function = button_height * .8

numq = [""]
firstnumber = "None"
secondnumber = "None"
action = "None"
result = 0

row1_y = 260
row2_y = row1_y + button_height + space
row3_y = row1_y + button_height + button_height + (space*2)
row4_y = row1_y + button_height + button_height + button_height + (space*3)
column1_x = 0
column2_x = column1_x + button_width + space
column3_x = column1_x + button_width + button_width + (space*2)
column4_x = column1_x + button_width + button_width + button_width + (space*3)

row1_f = 120
row2_f = row1_f + button_height_function + space
col1_f = 0
col2_f = col1_f + button_width_function + space
col3_f = col1_f + button_width_function*2 + space*2
col4_f = col1_f + button_width_function*3 + space*3

black = (0,0,0)
blue = (0,0,255)
red = (255,0,0)
green = (90,255,0)
white = (255,255,255)

def draw_button(x1,y1,w,h,c_nactive,c_active,msg,c_msg=white):

        global result

        tex = mainfont.render(msg, True, c_msg)
        xmiddle = x1 + (w/2) - 20
        ymiddle = y1 + (h/2) - 20

        if (cmouse[0] > x1) and (cmouse[0] < (x1+w)) and (cmouse[1] > y1) and (cmouse[1] < (y1+h)):
            pygame.draw.rect(screen,c_active,(x1,y1,w,h))
            screen.blit(tex, (xmiddle, ymiddle))
            if mouse_click: 
                result = 0
                return True
        else: 
            pygame.draw.rect(screen,c_nactive,(x1,y1,w,h))
            screen.blit(tex, (xmiddle, ymiddle))

def add(n1,n2):

        return n1 + n2

def subtract(n1,n2):

        return n1 - n2

def multiply(n1,n2):

        return n1*n2

def divide(n1,n2):

        if (n2 == 0):
            return 0
        else:
            return n1 / n2

def prepare_new_num():

        global numq
        global firstnumber
        global secondnumber
        global action

        hold = ""

        for i in numq:
            hold += i

        numq = [""]
        # change numq to N to make sure its empty and if empty dont assign anything
        # if list len is 1 and if list[0] = N then skip
        if ('.' in hold):
            if (firstnumber == "None"): firstnumber = float(hold)
            elif (secondnumber == "None"): secondnumber = float(hold)
        else:
            if (firstnumber == "None"): firstnumber = int(hold)
            elif (secondnumber == "None"): secondnumber = int(hold)
        
        if ((firstnumber != "None") and (secondnumber != "None")):
            if (action == "None"): pass
            elif (action == "add"): 
                firstnumber = add(firstnumber,secondnumber)
                secondnumber = "None"
            elif (action == "subtract"):
                firstnumber = subtract(firstnumber,secondnumber)
                secondnumber = "None"
            elif (action == "multiply"):
                firstnumber = multiply(firstnumber,secondnumber)
                secondnumber = "None"
            elif (action == "divide"):
                firstnumber = divide(firstnumber,secondnumber)
                secondnumber = "None"

def calc_result(action="None"):

        global numq
        global firstnumber
        global secondnumber
        global result

        if (firstnumber == "None"): return

        hold = ""

        for i in numq:
            hold += i
        # second number should always be empty at this point
        numq = [""]

        if ('.' in hold): secondnumber = float(hold)
        else: secondnumber = int(hold)

        if (action == "None"): pass
        elif (action == "add"): 
            result = add(firstnumber,secondnumber)
            
        elif (action == "subtract"):
            result = subtract(firstnumber,secondnumber)
            
        elif (action == "multiply"):
            result = multiply(firstnumber,secondnumber)
            
        elif (action == "divide"):
            result = divide(firstnumber,secondnumber)

        print(result)
        all_clear()
          
def all_clear():

    global firstnumber
    global secondnumber
    global action
    global numq
    global result

    firstnumber = "None"
    secondnumber = "None"
    action = "None"
    numq = [""]
    #result = 0


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN: mouse_click = True 

    screen.fill(white)



    cmouse = pygame.mouse.get_pos()

    pygame.draw.rect(screen,black,(0,100,width,5))



    if (draw_button(column1_x,row1_y,button_width,button_height,blue,green,"1")): numq.append("1")
    if (draw_button(column2_x,row1_y,button_width,button_height,blue,green,"2")): numq.append("2")
    if (draw_button(column3_x,row1_y,button_width,button_height,blue,green,"3")): numq.append("3")

    if (draw_button(column1_x,row2_y,button_width,button_height,blue,green,"4")): numq.append("4")
    if (draw_button(column2_x,row2_y,button_width,button_height,blue,green,"5")): numq.append("5")
    if (draw_button(column3_x,row2_y,button_width,button_height,blue,green,"6")): numq.append("6")

    if (draw_button(column1_x,row3_y,button_width,button_height,blue,green,"7")): numq.append("7")
    if (draw_button(column2_x,row3_y,button_width,button_height,blue,green,"8")): numq.append("8")
    if (draw_button(column3_x,row3_y,button_width,button_height,blue,green,"9")): numq.append("9")

    if (draw_button(0,row4_y,button_width*2+space,button_height,blue,green,"0")): numq.append("0")

    if (draw_button(column3_x,row4_y,button_width,button_height,blue,green,".")): 
        if ('.' not in numq): numq.append(".")

    if (draw_button(col3_f,row1_f,button_width_function,button_height_function,blue,green,"ac")): all_clear()
   
    if (draw_button(col3_f,row2_f,button_width_function,button_height_function,blue,green,"c")): 
        numq = [""]
        action = "None"

    if (draw_button(col1_f,row1_f,button_width_function,button_height_function,blue,green,"+")): 
        prepare_new_num()
        action = "add"

    if (draw_button(col1_f,row2_f,button_width_function,button_height_function,blue,green,"-")): 
        prepare_new_num()
        action = "subtract"

    if (draw_button(col2_f,row1_f,button_width_function,button_height_function,blue,green,"*")): 
        prepare_new_num()
        action = "multiply"

    if (draw_button(col2_f,row2_f,button_width_function,button_height_function,blue,green,"/")): 
        prepare_new_num()
        action = "divide"

    # equal must be at bottom
    if (draw_button(col4_f,row1_f,button_width_function*2+space,button_height_function*2+space,blue,green,"=")): 
        calc_result(action)
        all_clear()

    temp = ""
    for i in numq:
    	temp += i

    if (temp == ""): temp = "0"
    if (result != 0): temp = str(result)

    
    #if ('.' not in temp): temp = int(temp)
    #else: temp = float(temp)
    #temp = str(temp)


    #if(result != 0):
        #temp = str(result)

    tex = mainfont.render(temp, True, black)
    screen.blit(tex, (10, 30))


    mouse_click = False
    pygame.display.flip()


''' THINGS TO-DO/FIX : BUGS MUST BE ERADICATED

    BUG: multiple decimal points
    DO: center text
    DO: make cleaner buttons



'''
