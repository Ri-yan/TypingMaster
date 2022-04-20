from tkinter import *  # this line means that we are importing all the classes and methods present in tkinter module
import random
from ttkthemes import *
from tkinter import ttk
from time import sleep

totalTime =60
def start_timer():
    textArea.config(state=NORMAL)
    textArea.focus()
    for time in range(1, 61):
        elapsed_timer_label.config(text=time)
        remaining_time = totalTime-time
        remaining_timer_label.config(text=remaining_time)
        sleep(1)
        root.update()


# GUI PART ##############################


root = ThemedTk()
root.get_themes()
root.set_theme('radiance')
root.geometry('940x735+200+0')
root.resizable(0, 0)
root.overrideredirect(True)  # removes title bar

mainFrame = Frame(root, bd=4)  # frame is a container where we add labels etc
mainFrame.grid()  # grid will add  frame to root window
titleFrame = Frame(mainFrame, bg='orange')
titleFrame.grid(row=0, column=0)
titleLabel = Label(titleFrame, text='Master Typing', bg='goldenrod3',
                   font=('algerian', 28, 'bold'), fg='white', width=38, bd=10)
titleLabel.grid(pady=5)

paragraph_frame = Frame(mainFrame)
paragraph_frame.grid(row=1, column=0)
paragraph_list = [
    ' I failed the first quarter of a class in middle school, so I made a fake report card. I did this every quarter that year. I forgot that they mail home the end-of-year cards, and my mom got it before I could intercept with my fake. She was PISSED—at the school for their error. The teacher also retired that year and had already thrown out his records, so they had to take my mother’s “proof” (the fake ones I made throughout the year) and “correct” the “mistake.” ',

    ' In my junior year of high school, this guy asked me on a date. He rented a Redbox movie and made a pizza. We were watching the movie and the oven beeped so the pizza was done. He looked me dead in the eye and said, “This is the worst part.” I then watched this boy open the oven and pull the pizza out with his bare hands, rack and all, screaming at the top of his lungs. We never had a second date.Ok so then what is i cannot tell you because that didnt happen.',

    'I went to this girl’s party the week after she beat the shit out of my friend. While everyone was getting trashed, I went around putting tuna inside all the curtain rods and so like weeks went by and they couldn’t figure out why the house smelled like festering death. They caught me through this video where these guys at the party were singing Beyonce while I was in the background with a can of tuna.This is what happened in this short funny story if you like.',

    'One time way back in sixth grade math class I had to fart really bad. Me being the idiot that I am decided that it would be silent. Big surprise it wasn’t. The only person talking was the teacher and she was interrupted by freaking cannon fire farts. She said she was disappointed I couldn’t hold it in and proceeded to tell a story of how she taught a famous athlete who did nearly the same thing.I felt ashamed then everyone laughed and at the end I also laughed.',

    'So a couple weeks ago, me and my friends were sitting on this cement kind of pedestal (as we called it) It’s basically the steps up to the portable. (classroom that no one uses) and this weird supply French teacher comes up to us and says: you shouldn’t be sitting on this ground, it’s too cold and it’s bad for your ovaries. I asked her how or why and she said that if children sit on cold ground their ovaries will freeze and that we won’t be able to have kids.',
    'One of the most valuable possession of human life is its health. With good health, one can attain everything in life. In order to perform an important work effectively, one has to be in sound health. Nowadays, everyone is suffering from some sort of mental, health, chronic or physical illness, which however deprives them. Often bad habits such as smoking have brought upon diseases and weakness upon a person which he is not aware of and are of no value to their family and society.',
    'Alcohol is taken in almost all cool and cold climates, and to a very much less extent in hot ones. It is taken by people who live in the Himalaya Mountains, but not nearly so much by those who live in the plains of India. Alcohol is not necessary in any way to anybody. The regular use of alcohol, even in small quantities, tends to cause mischief in many ways to various organs of the body. It affects the liver, it weakens the mental powers, and lessens the energy of the body.',

    'The Computer is an automatic device that performs mathematical calculations and logical operations. They are being put to use in widely divergent fields such as book-keeping, spaceflight controls, passanger reservation service, language translation etc. There are two categories: analog and digital. The former represents numbers by some physical quantity such as length, angular relation or electric current whereas the latter represent numbers by seperate devices for each digit.'
    ]
random.shuffle(paragraph_list)

labelParagraph = Label(paragraph_frame, text=paragraph_list[0], font=('arial', 14, 'bold'),
                       wraplength=912, justify='left')
labelParagraph.grid(row=0, column=0)
textAreaFrame = Frame(mainFrame)
textAreaFrame.grid(row=2, column=0)
textArea = Text(textAreaFrame, font=('arial', 12, 'bold'), width=100, height=7, bd=4, relief=GROOVE, wrap='word',
                state=DISABLED)
textArea.grid()

frame_output = Frame(mainFrame)
frame_output.grid(row=3, column=0)

elapsed_time_label = Label(frame_output, text='Elapsed Time', fg='red', font=('Tahoma', 12, 'bold'))
elapsed_time_label.grid(row=0, column=0, padx=5)

elapsed_timer_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
elapsed_timer_label.grid(row=0, column=1, padx=5)

remaining_time_label = Label(frame_output, text='Remaining Time', fg='red', font=('Tahoma', 12, 'bold'))
remaining_time_label.grid(row=0, column=2, padx=5)

remaining_timer_label = Label(frame_output, text='60 sec', font=('Tahoma', 12, 'bold'))
remaining_timer_label.grid(row=0, column=3, padx=5)

wpm_label = Label(frame_output, text='WPM', fg='red', font=('Tahoma', 12, 'bold'))
wpm_label.grid(row=0, column=4, padx=5)

wpm_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wpm_count_label.grid(row=0, column=5, padx=5)

accuracy_label = Label(frame_output, text='Accuracy', fg='red', font=('Tahoma', 12, 'bold'))
accuracy_label.grid(row=0, column=6, padx=5)

accuracy_percent_label = Label(frame_output, text='0%', font=('Tahoma', 12, 'bold'))
accuracy_percent_label.grid(row=0, column=7, padx=5)

totalwords_label = Label(frame_output, text='Total Words', fg='red', font=('Tahoma', 12, 'bold'))
totalwords_label.grid(row=0, column=8, padx=5)

totalwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
totalwords_count_label.grid(row=0, column=9, padx=5)

wrongwords_label = Label(frame_output, text='Wrong Words', fg='red', font=('Tahoma', 12, 'bold'))
wrongwords_label.grid(row=0, column=10, padx=5)

wrongwords_count_label = Label(frame_output, text='0', font=('Tahoma', 12, 'bold'))
wrongwords_count_label.grid(row=0, column=11, padx=5)

buttonFrame = Frame(mainFrame)
buttonFrame.grid(row=4, column=0)

startButton = ttk.Button(buttonFrame, text='Start', command=start_timer)
startButton.grid(row=0, column=0, padx=10)
# use ttk. to apply themes
resetButton = ttk.Button(buttonFrame, text='Reset', state=DISABLED)
resetButton.grid(row=0, column=1, padx=10)

exitButton = ttk.Button(buttonFrame, text='Exit', command=root.destroy)
exitButton.grid(row=0, column=2, padx=10)

keyboard_frame = Frame(mainFrame)
keyboard_frame.grid(row=5, column=0)

frame1to0 = Frame(keyboard_frame)
frame1to0.grid(pady=3)

label1 = Label(frame1to0, text='1', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label1.grid(row=0, column=0, padx=5)
label2 = Label(frame1to0, text='2', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label2.grid(row=0, column=1, padx=5)
label3 = Label(frame1to0, text='3', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label3.grid(row=0, column=2, padx=5)
label4 = Label(frame1to0, text='4', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label4.grid(row=0, column=3, padx=5)
label5 = Label(frame1to0, text='5', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label5.grid(row=0, column=4, padx=5)
label6 = Label(frame1to0, text='6', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label6.grid(row=0, column=5, padx=5)
label7 = Label(frame1to0, text='7', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label7.grid(row=0, column=6, padx=5)
label8 = Label(frame1to0, text='8', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label8.grid(row=0, column=7, padx=5)
label9 = Label(frame1to0, text='9', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label9.grid(row=0, column=8, padx=5)
label0 = Label(frame1to0, text='0', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
label0.grid(row=0, column=9, padx=5)

frameqtop = Frame(keyboard_frame)
frameqtop.grid(row=1, column=0, pady=3)

labelq = Label(frameqtop, text='q', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelq.grid(row=0, column=0, padx=5)
labelw = Label(frameqtop, text='w', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelw.grid(row=0, column=1, padx=5)
labele = Label(frameqtop, text='e', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labele.grid(row=0, column=2, padx=5)
labelr = Label(frameqtop, text='r', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelr.grid(row=0, column=3, padx=5)
labelt = Label(frameqtop, text='t', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelt.grid(row=0, column=4, padx=5)
labely = Label(frameqtop, text='y', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labely.grid(row=0, column=5, padx=5)
labelu = Label(frameqtop, text='u', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelu.grid(row=0, column=6, padx=5)
labeli = Label(frameqtop, text='i', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labeli.grid(row=0, column=7, padx=5)
labelo = Label(frameqtop, text='o', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelo.grid(row=0, column=8, padx=5)
labelp = Label(frameqtop, text='p', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelp.grid(row=0, column=9, padx=5)

frameatol = Frame(keyboard_frame)
frameatol.grid(row=2, column=0, pady=3)

labela = Label(frameatol, text='a', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labela.grid(row=0, column=0, padx=5)
labels = Label(frameatol, text='s', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labels.grid(row=0, column=1, padx=5)
labeld = Label(frameatol, text='d', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labeld.grid(row=0, column=2, padx=5)
labelf = Label(frameatol, text='f', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelf.grid(row=0, column=3, padx=5)
labelg = Label(frameatol, text='g', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelg.grid(row=0, column=4, padx=5)
labelh = Label(frameatol, text='h', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelh.grid(row=0, column=6, padx=5)
labelj = Label(frameatol, text='j', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelj.grid(row=0, column=7, padx=5)
labelk = Label(frameatol, text='k', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelk.grid(row=0, column=8, padx=5)
labell = Label(frameatol, text='l', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labell.grid(row=0, column=9, padx=5)

frameztom = Frame(keyboard_frame)
frameztom.grid(row=3, column=0, pady=3)
labelz = Label(frameztom, text='z', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelz.grid(row=0, column=0, padx=5)
labelx = Label(frameztom, text='x', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelx.grid(row=0, column=1, padx=5)
labelc = Label(frameztom, text='c', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelc.grid(row=0, column=2, padx=5)
labelv = Label(frameztom, text='v', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelv.grid(row=0, column=3, padx=5)
labelb = Label(frameztom, text='b', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelb.grid(row=0, column=4, padx=5)
labeln = Label(frameztom, text='n', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labeln.grid(row=0, column=5, padx=5)
labelm = Label(frameztom, text='m', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE, width=5,
               height=2)
labelm.grid(row=0, column=6, padx=5)

spaceFrame = Frame(keyboard_frame)
spaceFrame.grid(row=4, column=0, pady=3)
labelspace = Label(spaceFrame, text='', bg='black', fg='white', font=('arial', 10, 'bold'), bd=10, relief=GROOVE,
                   width=40, height=2)
labelspace.grid(row=0, column=6, padx=5)


def changeBG(widget):
    widget.config(bg='dark blue')
    widget.after(300, lambda: widget.config(bg='black'))


label_number = [label1, label2, label3, label4, label5, label6, label7, label8, label9, label0]
number_labels = [label0, label1, label2, label3, label4, label5, label6, label7,
                 label8, label9]
label_alphabet = [labelq, labelw, labele, labelr, labelt, labely, labelu, labeli, labelo, labelp, labela, labels,
                  labeld, labelf, labelg, labelh, labelj, labelk
    , labell, labelz, labelx, labelc, labelv, labelb, labeln, labelm]
space_label_list = [labelspace]

binding_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
binding_small_alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'n', 'o', 'p', 'q', 'r', 's', 't',
                       'u', 'v', 'w', 'x', 'y', 'z']
binding_capital_alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                         'U', 'V', 'W', 'X', 'Y', 'Z']

for numbers in range(10):
    root.bind(numbers, lambda event, x=number_labels[numbers]: changeBG(x))

for capital_alpha in range(len(binding_capital_alpha)):
    root.bind(binding_capital_alpha[capital_alpha], lambda event, x=label_alphabet[capital_alpha]: changeBG(x))

for SMALL_alpha in range(len(binding_capital_alpha)):
    root.bind(binding_small_alpha[SMALL_alpha], lambda event, x=label_alphabet[SMALL_alpha]: changeBG(x))

root.bind('<space>', lambda event, x=labelspace: changeBG(x))

root.mainloop()

# for themeing pip install ttkthemesf
