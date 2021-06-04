import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as m_box
import pandas as pd
import datetime
import numpy as np
import matplotlib.pyplot as plt

win = tk.Tk()
win.title("Sleeptastic")
win.geometry("1100x1100")
container = ttk.Frame(win)
canvas = tk.Canvas(container, width=990)
scrollbar = ttk.Scrollbar(container, orient="vertical", command=canvas.yview)
frame = ttk.Frame(canvas)

frame.bind(
    "<Configure>",
    lambda e: canvas.configure(
        scrollregion=canvas.bbox("all")
    )
)

canvas.create_window((0, 0), window=frame)

canvas.configure(yscrollcommand=scrollbar.set)
container.pack()
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

# for i in range(50):
#     ttk.Label(frame, text="Sample scrolling label").pack()


details = ttk.Label(frame, text='Details ')
details.grid(padx=40, row=0, column=0, sticky=tk.W)

day1 = ttk.Label(frame, text='Day1 ')
day1.grid(padx=40, row=1, column=0, sticky=tk.W)

labels = ['falling asleep time ', 'getting out of bed ', 'stress substance ',
          'sleep duration ', 'quality ', 'Stress throughout the day ']
for i in range(len(labels)):
    label = 'label' + str(i+1)
    label = ttk.Label(frame, text=labels[i],)
    label.grid(row=0, column=i+1, sticky=tk.W)

myList = []
for i in range(6):
    entry = ttk.Entry(frame, width=22)
    entry.grid(row=1, column=i+1, sticky=tk.W)
    myList.append(entry)


myList2 = []
count = 1


def addDayFun():
    add_day.configure(foreground='Blue')
    rowList = []
    global count
    day = ttk.Label(frame, text='Day'+str(count+1))
    day.grid(padx=40, row=count+1, column=0, sticky=tk.W)
    for i in range(6):
        entry2 = ttk.Entry(frame, width=22)
        entry2.grid(row=count+1, column=i+1, sticky=tk.W)
        rowList.append(entry2)
    myList2.append(rowList)
    count += 1


a = 0


def storeData():
    button2.configure(foreground='Blue')
    global a
    x1 = []
    x2 = []
    x3 = []
    x4 = []
    x5 = []
    x6 = []
    try:
        x1.append(myList[0].get())
        x2.append(myList[1].get())
        if myList[2].get() == 'alcohal' or myList[2].get() == 'stress' or myList[2].get() == 'melatonin':
            x3.append(myList[2].get())
        x4.append(float(myList[3].get()))
        x5.append(float(myList[4].get()))
        x6.append(float(myList[5].get()))
        for i in range(len(myList2)):
            x1.append(myList2[i][0].get())
            x2.append(myList2[i][1].get())
            if myList2[i][2].get() == 'alcohal' or myList2[i][2].get() == 'stress' or myList2[i][2].get() == 'melatonin':
                x3.append(myList2[i][2].get())
            x4.append(float(myList2[i][3].get()))
            x5.append(float(myList2[i][4].get()))
            x6.append(float(myList2[i][5].get()))

        df = pd.DataFrame({
            'falling asleep time ': x1,
            'getting out of bed ': x2,
            'stress substance ': x3,
            'sleep duration ': x4,
            'quality ': x5,
            'Stress throughout the day ': x6
        }, columns=labels)
        df.to_csv(r'E:\\abc.csv', index=False, header=True)
        df['falling asleep time '] = pd.to_datetime(df['falling asleep time '])
        df['getting out of bed '] = pd.to_datetime(df['getting out of bed '])
        a += 1
    except:
        m_box.showerror('Error', 'Invalid input !')


def submit():
    button.configure(foreground='Blue')
    global a
    if a > 0:
        win2 = tk.Tk()
        win2.title('Data Visualization')
        win2.geometry("1000x500")

        def graph1():
            df2 = pd.read_csv(r'E:\\abc.csv')
            if df2.shape[0] < 7:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df2['stress substance '][i] == 'stress':
                    x.append(i+1)
                    y.append(df2['sleep duration '][i])

            plt.plot(x, y, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.show()

        def graph2():

            df3 = pd.read_csv(r'E:\\abc.csv')
            if df3.shape[0] < 30:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df3['stress substance '][i] == 'stress':
                    x.append(i+1)
                    y.append(df3['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df3['stress substance '][i] == 'stress':
                    x2.append(i+1)
                    y2.append(df3['sleep duration '][i])

            plt.subplot(2, 1, 1)
            plt.plot(x, y, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(2, 1, 2)
            plt.plot(x2, y2, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.show()

        def graph3():

            df4 = pd.read_csv(r'E:\\abc.csv')
            if df4.shape[0] < 90:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df4['stress substance '][i] == 'stress':
                    x.append(i+1)
                    y.append(df4['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df4['stress substance '][i] == 'stress':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            x3 = []
            y3 = []

            for i in range(90):
                if df4['stress substance '][i] == 'stress':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            plt.subplot(3, 1, 1)
            plt.plot(x, y, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 2)
            plt.plot(x2, y2, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 3)
            plt.plot(x3, y3, marker='o', color='Blue')
            plt.title('Sleep hours while in Stress durring 90 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.show()


############### buttons for alcohal ###################################


        def graph11():

            df2 = pd.read_csv(r'E:\\abc.csv')
            if df2.shape[0] < 7:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df2['stress substance '][i] == 'alcohal':
                    x.append(i+1)
                    y.append(df2['sleep duration '][i])

            plt.plot(x, y, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.legend()
            plt.show()

        def graph22():

            df3 = pd.read_csv(r'E:\\abc.csv')
            if df3.shape[0] < 30:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df3['stress substance '][i] == 'alcohal':
                    x.append(i+1)
                    y.append(df3['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df3['stress substance '][i] == 'alcohal':
                    x2.append(i+1)
                    y2.append(df3['sleep duration '][i])

            plt.subplot(2, 1, 1)
            plt.plot(x, y, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(2, 1, 2)
            plt.plot(x2, y2, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.show()

        def graph33():

            df4 = pd.read_csv(r'E:\\abc.csv')
            if df4.shape[0] < 90:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df4['stress substance '][i] == 'alcohal':
                    x.append(i+1)
                    y.append(df4['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df4['stress substance '][i] == 'stress':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            x3 = []
            y3 = []

            for i in range(90):
                if df4['stress substance '][i] == 'alcohal':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            plt.subplot(3, 1, 1)
            plt.plot(x, y, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 2)
            plt.plot(x2, y2, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 3)
            plt.plot(x3, y3, marker='o', color='Red')
            plt.title(
                'Sleep hours while stress substance is alcohal durring 90 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.show()

        ######################### graph for melatonin ################

        def graph111():

            df2 = pd.read_csv(r'E:\\abc.csv')
            if df2.shape[0] < 7:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df2['stress substance '][i] == 'melatonin':
                    x.append(i+1)
                    y.append(df2['sleep duration '][i])

            plt.plot(x, y, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.legend()
            plt.show()

        def graph222():

            df3 = pd.read_csv(r'E:\\abc.csv')
            if df3.shape[0] < 30:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df3['stress substance '][i] == 'melatonin':
                    x.append(i+1)
                    y.append(df3['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df3['stress substance '][i] == 'melatonin':
                    x2.append(i+1)
                    y2.append(df3['sleep duration '][i])

            plt.subplot(2, 1, 1)
            plt.plot(x, y, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(2, 1, 2)
            plt.plot(x2, y2, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.show()

        def graph333():

            df4 = pd.read_csv(r'E:\\abc.csv')
            if df4.shape[0] < 90:
                m_box.showerror('Error', 'Less data then required !')
                win2.destroy()
            x = []
            y = []
            for i in range(7):
                if df4['stress substance '][i] == 'melatonin':
                    x.append(i+1)
                    y.append(df4['sleep duration '][i])
            x2 = []
            y2 = []

            for i in range(30):
                if df4['stress substance '][i] == 'melatonin':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            x3 = []
            y3 = []

            for i in range(90):
                if df4['stress substance '][i] == 'melatonin':
                    x2.append(i+1)
                    y2.append(df4['sleep duration '][i])

            plt.subplot(3, 1, 1)
            plt.plot(x, y, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 7 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 2)
            plt.plot(x2, y2, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 30 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")

            plt.subplot(3, 1, 3)
            plt.plot(x3, y3, marker='o', color='Green')
            plt.title(
                'Sleep hours while stress substance is melatonin durring 90 Days')
            plt.xlabel('Days')
            plt.ylabel("Amount of Hours of Sleep")
            plt.show()

        f2 = ttk.LabelFrame(win2, text='Buttons to display graphs')
        f2.grid(row=0, column=0, padx=10, pady=20)

        label1 = ttk.Label(f2, text='Effecting Factors !',
                           font=('Helvetica', 18, 'bold'))
        label1.grid(row=0, column=0, sticky=tk.W, padx=5, pady=8)

        button1 = tk.Button(f2, text='Stress 7Days',
                            height=2, width=25, command=graph1)
        button1.grid(row=1, column=0, sticky=tk.W, padx=15)

        button2 = tk.Button(f2, text='Stress 30Days',
                            height=2, width=25, command=graph2)
        button2.grid(row=2, column=0, sticky=tk.W, padx=15)

        button3 = tk.Button(f2, text='Stress 90Days',
                            height=2, width=25, command=graph3)
        button3.grid(row=3, column=0, sticky=tk.W, padx=15)

        button11 = tk.Button(f2, text='alcohal 7Days',
                             height=2, width=25, command=graph11)
        button11.grid(row=4, column=0, sticky=tk.W, padx=15)

        button22 = tk.Button(f2, text='alcohal 30Days',
                             height=2, width=25, command=graph22)
        button22.grid(row=5, column=0, sticky=tk.W, padx=15)

        button33 = tk.Button(f2, text='alcohal 90Days',
                             height=2, width=25, command=graph33)
        button33.grid(row=6, column=0, sticky=tk.W, padx=15)

        button111 = tk.Button(f2, text='melatonin 7Days',
                              height=2, width=25, command=graph111)
        button111.grid(row=7, column=0, sticky=tk.W, padx=15)

        button222 = tk.Button(f2, text='melatonin 30Days',
                              height=2, width=25, command=graph222)
        button222.grid(row=8, column=0, sticky=tk.W, padx=15)

        button333 = tk.Button(f2, text='melatonin 90Days',
                              height=2, width=25, command=graph333)
        button333.grid(row=9, column=0, sticky=tk.W, padx=15)

        win2.mainloop()
    else:
        m_box.showerror('Error', 'First enter data and store data !')


add_day = tk.Button(win, text='addDay', command=addDayFun, height=1, width=8)
add_day.pack()

button2 = tk.Button(win, text='Store Data',
                    command=storeData, height=1, width=8)
button2.pack()

button = tk.Button(win, text='Submit', command=submit, height=1, width=8)
button.pack()


# container.pack()
# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="right", fill="y")

win.mainloop()
