#when I call the constructor obj = MazeToGraphImplementation()
#I should pass it as an additional argument <self> inside functions
#self is like <this> in Java.
#The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.

#the call is: file_name.class_name()
import InferenceEngine
import time
import os

class TestClass:
    start_time = time.time()
    copyOfCantusFirmusList = [] #contains string objects
    
    cantusFirmus = list((
    "........",
    "........",
    ".....*..",
    "........",
    "........",
    "........",
    "....*.*.",
    "*......*",
    ".*......",
    "..*.....",
    "...*....",
    "........",
    "........",
    "........",
    "........",
    ))
    
    print("The maze with cantus firmus\n")
    copyOfCantusFirmusList = cantusFirmus.copy()
    #list now has string objects, because grid is constructed upon string characters
    
    for lists in copyOfCantusFirmusList:
        for i in lists:
            print(i, end='\t')
        print()
        
    inferenceEngineObject = InferenceEngine.InferenceEngine(copyOfCantusFirmusList)    
    print('finished in ',(time.time() - start_time), ' seconds')
    os.system("pause")