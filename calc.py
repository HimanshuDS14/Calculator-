



from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("380x550+200+100")

root.resizable(False , False)
root.config(bg = 'yellow')



entry_box = Entry(font = "verdana 14 bold" , width  =22 ,bd = 6 , justify = RIGHT , bg = 'cyan')
entry_box.insert(0 , '0')
entry_box.place(x = 30  ,y =10)


def enterNumber(x):
    if entry_box.get()=='0':
        if x=='.':
            entry_box.insert(1,".")
        else:
            entry_box.delete(0  ,'end')
            entry_box.insert(0 , str(x))


    else:
        length = len(entry_box.get())
        entry_box.insert(length , str(x))


def enterOperator(x):
    if entry_box.get()!='0':
        length = len(entry_box.get())

        all_text = entry_box.get()
        last_char =all_text[-1:]

        if last_char in ['+' , '-' , '/'] or all_text[-2:] == '**':
            pass
        else:
            entry_box.insert(length , btn_operator[x]['text'])




def funcclear():
    entry_box.delete(0 , 'end')
    entry_box.insert(0 , '0')


result = 0
def funcOperator():
    content = entry_box.get()

    result = eval(content)
    entry_box.delete(0 , "end")
    entry_box.insert(0 , result)

    status.configure(text = content + " = "+ str(result))




def deletedig():
    length = len(entry_box.get())
    entry_box.delete(length-1 , 'end')

    if(length==1):
        entry_box.insert(0 , "0")




btn_number = []

for i in range(10):
    btn_number.append(Button(width = 4 , text = str(i) , bd = 6 ,bg = "magenta", command = lambda x = i:enterNumber(x)))

btn_text = 1
for i in range(0,3):
    for j in range(0,3):
        btn_number[btn_text].place(x=30+j*90 , y = 70+i*70)
        btn_text +=1

btnzero = Button(width = 14 ,text = '0' , bd = 6 ,bg = "light green", command = lambda x = 0:enterNumber(x))
btnzero.place(x = 25 , y = 280)

btnclr = Button(width = 4 , text = 'C' ,bg = "pink", font = "times 15 bold" , bd = 5  ,command = funcclear)
btnclr.place(x = 25 , y = 340)

btndot = Button(width = 4 , text = "." , bd = 5  ,bg = "light green", font = 'times 10 bold' , command = lambda x = '.':enterNumber(x) )
btndot.place(x = 160 , y = 280)

btnequals = Button(width = 4 , text = "=" , bd = 5 ,bg = "light green", command = funcOperator)
btnequals.place(x = 220 , y = 280)

btndelete = Button(width =14 , text = "< Back" ,bd = 4 ,bg = "pink", font = "times 14 bold" , command = deletedig)
btndelete.place(x = 100 , y = 340)


status = Label(root , text = "History : " , height = 3 , anchor = W , font = "verdana 11 bold" )
status.pack(side = BOTTOM , fill = X)



btn_operator = []

for i in range(4):
    btn_operator.append(Button(width = 4 , font = "times 15 bold" , bg = "light green",bd = 5 , command = lambda x = i:enterOperator(x)))

btn_operator[0]['text'] = "+"
btn_operator[1]['text'] = "-"
btn_operator[2]['text'] = "*"
btn_operator[3]['text'] = "/"


for i in range(4):
    btn_operator[i].place(x=290 , y = 70+i*70)




root.mainloop()