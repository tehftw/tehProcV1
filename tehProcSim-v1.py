# tehProcSim-v1.py



# The machine is named tehProc


# tehProc-v1 memory outline:

# four one-bit latches:
# memoryM, regA, regB, regC(output of logical operations)


FileQuickMode = True        # Set true: to make it default to reading from file named"program". For debug mostly
CONCISE_DISPLAY_MODE = True # Set true: to make the memory  displayed in a way shorter way

# Declaring how the processor's memory is shown in-program
A = False
B = False
C = False
M = False






ASMInstructionList = [ ]
ASM_numberOfInstructions = 0

def asm_AddInstruction (instruction_name) :
    global ASM_numberOfInstructions
    global ASMInstructionList
    ASM_numberOfInstructions = ASM_numberOfInstructions + 1
    ASMInstructionList.append(instruction_name)


#       TAKING IN THE CODE FROM THE TEXTFILE
ProgramFilename = "program" # For the ASM program code


if( not FileQuickMode ):
    print("Put in filename of the program. ")
    Input_ProgramFilename = input( "set empty to default to '%s':" %(ProgramFilename) )
    if (Input_ProgramFilename) :
        ProgramFilename = Input_ProgramFilename


# Setting what to do in case of a command that isn't valid in the current ASM code TODO: make it functional
PROGRAM_FILE_FIX_MODE = "IGNORE"



# copied from stackoverflow https://stackoverflow.com/questions/12330522/reading-a-file-without-newlines
ProgramArray = open(ProgramFilename, 'r').read().splitlines()



#            Simulator-only procedures
#   Printing the state of the memory and command list:

def PrintMemory ():
    print("Memory:")
    memory_string = GetMemoryString()
    print(memory_string)

def GetMemoryString() :
    memory_string = " A: %i  B: %i  C: %i  M: %i" % (A, B, C, M)
    return memory_string

def PrintProcessorData ():
    # for commands and memory, comments etc.
    i = 0
    print("Highest instruction number: ", ASM_numberOfInstructions)
    print("Printing instruction list:")
    for cur_com in ASMInstructionList:
        print(i, cur_com)
        i = i + 1
    print ( " Memory is four SR latches: regA, regB, regC, memoryM. ")
    print ( " No actual program reading yet " )

def PrintFullProgramArray ():
    print("Printing the full current program: ")
    i = 0
    for cur_com in ProgramArray :
        print( i, cur_com )
        i = i+1

def PrintEverything__ProcesorData_Memory_Registers_Program () :
    PrintProcessorData()
    PrintMemory()
    PrintFullProgramArray()
# End of Sim-Only procedures TODO: Move them to another .py file


# Before going further, it should print the memory, registers, and command list so that I can see it's working
PrintProcessorData()
PrintMemory()



LIVE_DEBUG_ENABLED = False # it will be funny if I don't use that at all xD

DEBUG_STRING_LIST = [ " [DEBUG_STRING] "]

def simulator_DEBUG(STRING_FOR_DEBUG) :
    memory_string = GetMemoryString()
    string_for_debug = "%s;    %s " % (STRING_FOR_DEBUG, memory_string)
    DEBUG_STRING_LIST.append(string_for_debug)
    if (LIVE_DEBUG_ENABLED):
       print(STRING_FOR_DEBUG)


def simulator_PRINT_FULL_DEBUG () :
    i = 0
    for debug_line in DEBUG_STRING_LIST:
        print(i, debug_line)
        i = i + 1



# PROCEDURES WITH USING THE PROCESSOR


# TODO: fix instruction set

asm_AddInstruction("NONE")


def instruction_NONE() :
    DEBUG_STRING = "NONE"

    DEBUG_STRING += ";"
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("SET_A")


def instruction_SET_A() :
    DEBUG_STRING = "SET_A: "

    global A
    A = True

    DEBUG_STRING += "A = %i;" % A
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("SET_B")


def instruction_SET_B() :
    DEBUG_STRING = "SET_B: "

    global B
    B = True

    DEBUG_STRING += "B = %i;" % B
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("SET_C")


def instruction_SET_C() :
    DEBUG_STRING = "SET_C: "

    global C
    C = True

    DEBUG_STRING += "C = %i;" % C
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("SET_M")


def instruction_SET_M() :
    DEBUG_STRING = "SET_M: "

    global M
    M = True

    DEBUG_STRING += "M = %i;" % M
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("RES_A")


def instruction_RES_A() :
    DEBUG_STRING = "RES_A: "

    global A
    A = False

    DEBUG_STRING += "A = %i;" % A
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("RES_B")


def instruction_RES_B() :
    DEBUG_STRING = "SET_B: "

    global B
    B = False

    DEBUG_STRING += "B = %i;" % B
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("SET_C")


def instruction_RES_C() :
    DEBUG_STRING = "SET_C: "

    global C
    C = False

    DEBUG_STRING += "C = %i;" % C
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("RES_M")


def instruction_RES_M() :
    DEBUG_STRING = "RES_M: "

    global M
    M = False

    DEBUG_STRING += "M = %i;" % M
    simulator_DEBUG(DEBUG_STRING)



asm_AddInstruction("RES_M")


def instruction_WRITE() :
    DEBUG_STRING = "WRITE: "

    global A
    global M
    if( A == 1 ):
        instruction_SET_M()
    else :
        instruction_RES_M()

    DEBUG_STRING += "M = %i;" % M
    simulator_DEBUG(DEBUG_STRING)

def instruction_READ() :
    DEBUG_STRING = "READ: "

    global A
    global M
    if( M == 1 ):
        instruction_SET_A()
    else :
        instruction_RES_A()

    DEBUG_STRING += "A = %i;" % A
    simulator_DEBUG(DEBUG_STRING)




# The if-else string that checks each assembly word
# TODO: Find a better way to do it

# Lambdas?



def simulator_InstructionCheck(CurrentInstruction) :
    cic = CurrentInstruction


    if (  cic == "NONE"  ) :
        instruction_NONE()
    if (cic == "SET_A" ) :
        instruction_SET_A()
    if (  cic == "SET_B" ) :
        instruction_SET_B()
    if (  cic == "SET_C" ) :
        instruction_SET_C()
    if (  cic == "SET_M" ) :
        instruction_SET_M()
    if (  cic == "RES_A" ) :
        instruction_RES_A()
    if (  cic == "RES_B" ) :
        instruction_RES_B()
    if (  cic == "RES_C" ) :
        instruction_RES_C()
    if (  cic == "RES_M" ) :
        instruction_RES_M()
    if ( cic == "WRITE") :
        instruction_WRITE()
    if ( cic == "READ") :
        instruction_READ()


# TODO: Before executing the program, check it's validity: so whether all the instructions are in the ASM dictionary

# PROCESSOR SIMUlATOR MAIN 'LOOP'
PROCESSOR_RUNNING = True

if( __name__ == "__main__" ) :
    while(PROCESSOR_RUNNING) :

#       hardcoded to test the functionality:
        for current_instruction in ProgramArray :
            simulator_InstructionCheck(current_instruction)



        # END OF PROGRAM
        PROCESSOR_RUNNING = False

    # important to show the debug and memory afterwards
    print(" ")
    print(" - - - PROGRAM HAS ENDED!!! - - - ")
    print(" ")
    simulator_PRINT_FULL_DEBUG()
    print(" ")
    PrintEverything__ProcesorData_Memory_Registers_Program()
    print(" ")
    PrintMemory()











