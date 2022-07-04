Assignment_2 CS202

HOW TO RUN

    Please ensure that there are 5 files and 1 folder(testcases) in the zip file

    After downloadinng the file update the directory as the location of the testcases file
    the directory string is present in line 4 (please update it here)

    Ensure the terminal is in the correct directory to run the code 

    To run the code type "python3 sourcecode.py"

    the terminal will then give instruction for the form of input required

    --->if you type 'y' the code will automatically take input from testcases folder and will give output for 
      each file in testcases and will store the output in output.txt
      (IT IS VERY ESSENTIAL TO UPDATE THE DIRECTORY  STRING IN LINE=4 BEFORE TYPING "y")

    --->if you type 'n' you have to ensure the before typing 'n' there must be a input in "input.txt" after
    typing 'n' the code will take take input from input.txt and store the output.txt

    IN TERMINAL THE CODE WOULD WHAT FILE IS CURRENTLY RUNNING IF YOU TYPE 'y'

    output.txt file will mention from what file the input has been taken from, the time taken for execution ,check function,and model OR UNSAT
check function will return if atleast one element is present in the model for each cluase in the formula to satisfy AND OF OR'S of CNF Formula(precautionary taken by me)

STORED OUTPUT IS THE TXT FILE WHICH HAS THE EXPECTED OUTPUT FOR EACH "CNF" FILE TESTCASES FOLDER
{I HAVE RUN ALL THE FILES BEFORE SUBMITTING}

LOGIC

The algorithm used to implement the sat-solver is DPLL with recursion 
Pseudo code for DPLL-
    S1,Formula=unit_resolution(Formula)
    if Formula=[],return S1 ---(Formula is a empty list)
    if [] present in Formula, return UNSAT ---(Formula contains a contradiction)
    choose a literal L such that L's count in Formula is maximum --(This will break the encoding to the maximum extent)
    if S2=DPLL(Formula UNION [[L]]) != UNSAT, return (S2 UNION S1)
    if S3=DPLL(Formula UNION [[-L]]) != UNSAT, return (S3 UNION S1)
    return UNSAT

unit_resolution-
    unit_resolution return 2 things
    S- a set of literals that were present as unit clauses in formula or which can be 
       derived by unit unit_resolution
    New Formula- A new formula which results from conditioning Formula on S
        Pseudo Code-
        S= empty set
        unit_clauses= list of all unit clauses
        while(unit_clauses not empty):
            for x in unit_clauses:
                S.add(x)
                formula=simplfy(formula,x)---(simplify function remove all clauses containing x and removes -x from a clause)
                unit_clauses=list of all unit_clauses ---(updating the unit clause list after simplification of formula)
        return solution,Formula

