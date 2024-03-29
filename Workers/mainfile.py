from tkinter import *
from tkinter import ttk
import time
import tkinter as tk
from PIL import ImageTk, Image
from tkinter.font import Font
import tkinter
import tkinter.font as font

# Problem A
from LongestCommonSubSequence import LongestCommonSubsequence, LargestCommonSequenceReader
# Problem B
from ShortestCommonSuperSequence import ShortestCommonSequence, ShortestCommonSequenceReader
# Problem C
from EditDistance import Distance, EditReader
# Problem D
from LongestIncreasingSubsequence import LongestIncresingSequence, LongestIncresingSequenceReader
# Problem E
from MatrixChainMultiplication import MatrixChainMultiplication, MatrixChainMultiplicationReader
#Problem F
from Knapsack import KnapSack, KnapSackReader
#Problem G
from PartitionProblem import PartitionProblem, PartitionProblemReader
#Problem H
from RodCutting import RodCutting, RodCuttingReader
#Problem I
from CoinChangeProblem import FindMinCoins, CoinChangeReader
#Problem J
from WordBreakProblem import WordBreak, WordBreakReader

AllFiles = ""
var = ""
var2 = ""
Result = ""
lines = []


def RunAlgo():
    global AllFiles, var, var2, Result

    # Problem A
    if var == 1:
        strings = AllFiles[var2 - 1][0].split()
        Result = LongestCommonSubsequence(strings[0], strings[1],
                                          len(strings[0]), len(strings[1]))
        Result = ''.join(map(str, Result))

        labelTest.configure(text="String-1: " + strings[0] + "\nString-2: " +
                            strings[1],
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="Longest Common Sub-Sequence Is: " + Result +
                             "\nLength: " + str(len(Result)),
                             foreground="BLACK",
                             background="GRAY")

    # Problem B
    if var == 2:
        strings = AllFiles[var2 - 1][0].split()
        Result = ShortestCommonSequence(strings[0], strings[1])
        Result = ''.join(map(str, Result))

        labelTest.configure(text="String-1: " + strings[0] + "\nString-2: " +
                            strings[1],
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="Super-Sequence Is: " + Result +
                             "\nWith Length: " + str(len(Result)),
                             foreground="BLACK",
                             background="GRAY")

    # Problem C
    if var == 3:
        strings = AllFiles[var2 - 1][0].split()
        Result = Distance(strings[0], strings[1])

        labelTest.configure(text="String-1: " + strings[0] + "\nString-2: " +
                            strings[1],
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="Minimum Numbers Of Edits Required: " +
                             str(Result),
                             foreground="BLACK",
                             background="GRAY")

    # Problem D
    if var == 4:
        data2 = []
        data1 = AllFiles[var2 - 1][0].split()
        for i in range(0, len(data1)):
            data1[i] = int(data1[i])
        Result = LongestIncresingSequence(data1)
        data1, data2 = data1[:len(data1) // 2], data1[len(data1) // 2:]
        labelTest.configure(text="Input Array: " + str(data1) + "\n" +
                            str(data2),
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(
            text="Length Of Longest Incresing Sub-Sequence: " + str(Result),
            foreground="BLACK",
            background="GRAY")

    # Problem E
    if var == 5:
        data1 = AllFiles[var2 - 1][0].split()
        for i in range(0, len(data1)):
            data1[i] = int(data1[i])
        Result = MatrixChainMultiplication(data1)

        data1, data2 = data1[:len(data1) // 2], data1[len(data1) // 2:]
        labelTest.configure(text="Dimensions Of Matrices: " + str(data1) +
                            "\n" + str(data2),
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="Minimum Numbers Of Multiplications : " +
                             str(Result),
                             foreground="BLACK",
                             background="GRAY")

    # Problem F
    if var == 6:
        v = []
        w = []
        W = 0
        data = AllFiles[var2 - 1]

        v = data[0][0].split()
        w = data[1][0].split()
        W = int(data[2][0])
        for i in range(0, len(v)):
            v[i] = int(v[i])

        for i in range(0, len(w)):
            w[i] = int(w[i])

        Result = KnapSack(v, w, W)

        labelTest.configure(text="Value: " + str(v) + "\nWeight: " + str(w) +
                            "\nKnapSack Capacity: " + str(W),
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="KnapSack Value Is : " + str(Result),
                             foreground="BLACK",
                             background="GRAY")

    # Problem G
    if var == 7:
        data1 = []
        data = AllFiles[var2 - 1][0].split()
        for i in range(0, len(data)):
            data[i] = int(data[i])

        Result = PartitionProblem(data, len(data))

        if (len(data) > 40):
            data1, data2 = data[:len(data) // 2], data[len(data) // 2:]
            labelTest.configure(text="Input Array: " + str(data1) + "\n" +
                                str(data2),
                                foreground="BLACK",
                                background="GRAY")

        else:
            labelTest.configure(text="Input Array: " + str(data),
                                foreground="BLACK",
                                background="GRAY")

        if (Result == True):
            labelTest2.configure(
                text="Array Can Be Divided Into Two Subsets Of Equal Sum ✔",
                foreground="BLACK",
                background="GRAY")

        else:
            labelTest2.configure(
                text="Array Can Not Be Divided Into Two Subsets Of Equal Sum ❌",
                foreground="BLACK",
                background="GRAY")

    # Problem H
    if var == 8:
        # print(var2)
        Length = []
        Price = []
        RodLength = 0
        data = AllFiles[var2 - 1]

        Length = data[0][0].split()
        Price = data[1][0].split()
        RodLength = int(data[2][0])
        for i in range(0, len(Length)):
            Length[i] = int(Length[i])

        for i in range(0, len(Price)):
            Price[i] = int(Price[i])

        Result = RodCutting(Price, len(Price))

        labelTest.configure(text="Rod Length Matrix: " + str(Length) +
                            "\nRod Price Matrix: " + str(Price) +
                            "\nRod Length: " + str(RodLength),
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(text="Profit Value Is : " + str(Result),
                             foreground="BLACK",
                             background="GRAY")

    # Problem I
    if var == 9:
        data = AllFiles[var2 - 1][0].split()
        for i in range(0, len(data) - 1):
            data[i] = int(data[i])

        rupee = int(data[len(data) - 1])
        data.pop()
        data = list(dict.fromkeys(data))

        Result = FindMinCoins(data, rupee)
        data1, data2 = data[:len(data) // 2], data[len(data) // 2:]
        labelTest.configure(text="List Of Available Coins: " + str(data1) +
                            "\n" + str(data2) + "\nDesired Change Of Rupee: " +
                            str(rupee),
                            foreground="BLACK",
                            background="GRAY")

        labelTest2.configure(
            text="Minimum Number Of Coins Required To Get Desired Change Is : "
            + str(Result),
            foreground="BLACK",
            background="GRAY")

    # Problem J
    if var == 10:
        data = AllFiles[var2 - 1][0].split()
        for i in range(0, len(data) - 1):
            data[i] = str(data[i])
        stri = str(data[len(data) - 1])
        data.pop()

        lookup = [-1] * (len(stri) + 1)
        Result = WordBreak(data, stri, lookup)
        data1, data2 = data[:len(data) // 2], data[len(data) // 2:]
        labelTest.configure(text="Words: " + str(data1) + "\n" + str(data2) +
                            "\nDesired Word: " + (stri),
                            foreground="BLACK",
                            background="GRAY")
        if Result:
            labelTest2.configure(text="String Can Be Segmented ✔ ",
                                 foreground="BLACK",
                                 background="GRAY")

        else:
            labelTest2.configure(text="String Can Not Be Segmented ❌ ",
                                 foreground="BLACK",
                                 background="GRAY")


AlgoDict = {
    "Longest_Common_Subsequence": 1,
    "Shortest_Common_Supersequence": 2,
    "Levenshtein_Distance_(edit-distance)": 3,
    "Longest_Increasing_Subsequence": 4,
    "Matrix_Chain_Multiplication ": 5,
    "0-1_Knapsack_Problem": 6,
    "Partition_Problem": 7,
    "Rod_Cutting_Problem": 8,
    "Coin_Change_Making_Problem": 9,
    "Word_Break_Problem": 10
}
OptionDict = {
    "File_01.txt": 1,
    "File_02.txt": 2,
    "File_03.txt": 3,
    "File_04.txt": 4,
    "File_05.txt": 5,
    "File_06.txt": 6,
    "File_07.txt": 7,
    "File_08.txt": 8,
    "File_09.txt": 9,
    "File_10.txt": 10,
}
OptionList = [
    "Longest_Common_Subsequence", "Shortest_Common_Supersequence",
    "Levenshtein_Distance_(edit-distance)", "Longest_Increasing_Subsequence",
    "Matrix_Chain_Multiplication ", "0-1_Knapsack_Problem",
    "Partition_Problem", "Rod_Cutting_Problem", "Coin_Change_Making_Problem",
    "Word_Break_Problem"
]
FileList = [
    "File_01.txt",
    "File_02.txt",
    "File_03.txt",
    "File_04.txt",
    "File_05.txt",
    "File_06.txt",
    "File_07.txt",
    "File_08.txt",
    "File_09.txt",
    "File_10.txt",
]

app = tk.Tk()
simg = ImageTk.PhotoImage(Image.open("2112.jpg"))

my = Label(app, image=simg)

my.image = simg

my.place(x=0, y=0)

Frame(app, height=516, width=5, bg='black')

app.attributes("-fullscreen", True)

app.title("Main Window")

my_font = Font(family="Times New Roman", size=30, weight="bold")

x1 = tk.Label(app,
              foreground="#66FF00",
              background="#808080",
              text="\nSelect The Algorithm 👇",
              font=my_font)
x1.pack(fill=tk.X, pady=9, padx=10)

variable = tk.StringVar(app)
variable.set("Algorithm's List ")

x1 = tk.OptionMenu(app, variable, *OptionList)
x1.config(width=90, font=('Helvetica', 20), bg="GRAY")
x1.pack(fill=tk.X, padx=10)
x1['menu'].config(bg="#7BCAB6")

x2 = tk.Label(app,
              foreground="#66FF00",
              background="#808080",
              text="\nSelect The File 👇",
              font=my_font)
x2.pack(fill=tk.X, pady=9, padx=10)
variable2 = tk.StringVar(app)
variable2.set("Files List")

x2 = tk.OptionMenu(app, variable2, *FileList)
x2.config(width=90, font=('Helvetica', 20), bg="GRAY")
x2.pack(fill=tk.X, pady=9, padx=10)
x2['menu'].config(bg="#7BCAB6")
myFont = font.Font(size=15, font="bold")

#callback functions


def callback2(*args):

    global var2, var
    if (var == 6 or var == 8):
        var2 = OptionDict[variable2.get()]
        strings = AllFiles[var2 - 1]
    else:
        var2 = OptionDict[variable2.get()]
        strings = AllFiles[var2 - 1][0].split()


#Output Display
labelTest = tk.Label(text="", font=('Helvetica', 14), fg='red')
labelTest.pack(pady=10, padx=90)
labelTest2 = tk.Label(text="", font=('Helvetica', 14), fg='red')
labelTest2.pack(pady=10, padx=90)

#run button
button1 = tk.Button(app, text='RUN', bg="GRAY", command=RunAlgo)
button1['font'] = myFont
button1.pack(pady=50, padx=60)

#Exit Button
button2 = tk.Button(app, text='EXIT', bg="GRAY", command=app.quit)
button2['font'] = myFont
button2.pack(pady=10, padx=90)


def callback(*args):
    global Result
    AllFiles = ReadFiles(variable.get())


def ReadFiles(algo):
    global var
    var = AlgoDict[algo]
    #Problem A
    if (var == 1):
        global AllFiles
        AllFiles = LargestCommonSequenceReader()

    #Problem B
    if (var == 2):

        AllFiles = ShortestCommonSequenceReader()

    #Problem C
    if (var == 3):

        AllFiles = EditReader()

    #Problem D
    if (var == 4):

        AllFiles = LongestIncresingSequenceReader()

    #Problem E
    if (var == 5):

        AllFiles = MatrixChainMultiplicationReader()

    #Problem F
    if (var == 6):

        AllFiles = KnapSackReader()
    #Problem G
    if (var == 7):
        AllFiles = PartitionProblemReader()

    #Problem H
    if (var == 8):
        AllFiles = RodCuttingReader()

    #Problem I
    if (var == 9):
        AllFiles = CoinChangeReader()

    #Problem J
    if (var == 10):
        AllFiles = WordBreakReader()


variable.trace("w", callback)
variable2.trace("w", callback2)
app.mainloop()