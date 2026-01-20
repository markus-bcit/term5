                                Processes




                               Dr. Ailbhe Gill


Textbook: Operating Systems: Internals and Design Principles, 9th
                 Edition by William Stallings


Pearson Education   ©   2018       Processes       January 16, 2026   1 / 62
Today’s Lecture




  • What is a process?
  • Process states
  • Process description
  • Process control
  • Execution of the operating system
  • UNIX SVR4 process management




  Pearson Education   ©   2018   Processes   January 16, 2026   2 / 62
Learning Objectives


After studying this chapter, you should be able to:
  • Define the term process and explain the relationship between
     processes and process control blocks.
  • Explain the concept of a process state and discuss the state
     transitions the processes undergo.
  • List and describe the purpose of the data structures and data
     structure elements used by an OS to manage processes.
  • Assess the requirements for process control by the OS.
  • Understand the issues involved in the execution of OS code.
  • Describe the process management scheme for UNIX SVR4.




  Pearson Education   ©   2018   Processes             January 16, 2026   3 / 62
                         What Is a Process?




Pearson Education   ©   2018    Processes   January 16, 2026   4 / 62
OS Management of Application Execution




Why is it important to manage application execution effectively?
 • Resources are made available to multiple applications
  • The processor is switched among multiple applications so all will
    appear to be progressing
  • The processor and I/O devices must be used efficiently to do this.




  Pearson Education   ©   2018    Processes             January 16, 2026   5 / 62
Process Elements



Two essential elements of a process are:
Two essential elements of a process are:
  1   Program code
            Which may be shared with other processes that are executing the same
            program
  2   A set of data associated with that code
When the processor begins to execute the program code, we refer to this
executing entity as a process




  Pearson Education   ©   2018        Processes              January 16, 2026   6 / 62
Process Control Block



 • Contains the process elements
   which uniquely characterize a
   process.
 • Makes it possible to interrupt a
   running process and later
   resume execution as if the
   interruption had not occurred
 • Created and managed by the
   operating system
 • Key tool that allows support for
   multiple processes
                                      Figure 1: Simplified Process Control
                                      Block

  Pearson Education   ©   2018   Processes                January 16, 2026   7 / 62
Process States




Trace
Lists the sequence of instructions that execute for that process.

The behavior of the processor can be characterized by showing how the
traces of the various processes are interleaved.
Dispatcher
Small program that switches the processor from one process to another




  Pearson Education   ©   2018     Processes              January 16, 2026   8 / 62
Traces of Processes




                                 Figure 2: Traces of Processes


  Pearson Education   ©   2018              Processes            January 16, 2026   9 / 62
Combined Trace of Processes


Example
Let us view these traces from the processor’s point of view.
The figure on the next slide shows the interleaved traces resulting from the
first 52 instruction cycles (for convenience, the instruction cycles are
numbered).
The shaded areas represent code executed by the dispatcher.
The same sequence of instructions is executed by the dispatcher in each
instance because the same functionality of the dispatcher is being
executed.
We assume that the OS only allows a process to continue execution for a
maximum of six instruction cycles, after which it is interrupted; this
prevents any single process from monopolizing processor time.



  Pearson Education   ©   2018     Processes             January 16, 2026   10 / 62
Combined Trace of Processes




                                 Figure 3: Combined Trace of Processes
  Pearson Education   ©   2018                  Processes                January 16, 2026   11 / 62
Process Execution




   Figure 4: Snapshot of Example Execution at Instruction Cycle 13 (Fig. 3)

  Pearson Education   ©   2018      Processes              January 16, 2026   12 / 62
                               Process States




Pearson Education   ©   2018        Processes   January 16, 2026   13 / 62
Two-State Process Model




  • The first step in designing an OS to control processes is to describe
    the behavior that we would like the processes to exhibit.
  • We can construct the simplest possible model by observing that, at
    any time, a process is either being executed by a processor or not.
  • In this model, a process may be in one of two states: Running or
    Not Running




  Pearson Education   ©   2018    Processes              January 16, 2026   14 / 62
Two-State Process Model




                                 Figure 5: Two-State Process Model

  Pearson Education   ©   2018                Processes              January 16, 2026   15 / 62
Reasons for Process Creation




  Pearson Education   ©   2018   Processes   January 16, 2026   16 / 62
Process Creation



Process spawning
When the OS creates a process at the explicit request of another process

Parent process
Is the original, creating, process

Child process
Is the new process




  Pearson Education   ©   2018       Processes          January 16, 2026   17 / 62
Reasons for Process Termination




  Pearson Education   ©   2018   Processes   January 16, 2026   18 / 62
Process Termination




  • There must be a means for a process to indicate its completion
  • A batch job should include a HALT instruction or an explicit OS
    service call for termination
  • For an interactive application, the action of the user will indicate
    when the process is completed (e.g., log off, quitting an application)




  Pearson Education   ©   2018    Processes              January 16, 2026   19 / 62
Five-State Process Model
  • If all processes were always ready to execute, then the queuing
    discipline suggested by Fig. 5(b) would be effective.
  • The queue is a first-in-first-out list and the processor operates in
    round-robin fashion on the available processes (each process in the
    queue is given a certain amount of time, in turn, to execute and then
    returned to the queue, unless blocked).
  • However, even with the simple example that we have described, this
    implementation is inadequate: Some processes in the Not Running
    state are ready to execute, while others are blocked, waiting for an
    I/O operation to complete.
  • Thus, using a single queue, the dispatcher could not just select the
    process at the oldest end of the queue.
  • Rather, the dispatcher would have to scan the list looking for the
    process that is not blocked and that has been in the queue the
    longest.
  • A more natural way to handle this situation is to split the Not
    Running state into two states: Ready and Blocked
  Pearson Education   ©   2018   Processes             January 16, 2026   20 / 62
Five-State Process Model




                                 Figure 6: Five-State Process Model




  Pearson Education   ©   2018                 Processes              January 16, 2026   21 / 62
Process States for Trace




                                 Figure 7: Process States for Trace




  Pearson Education   ©   2018                Processes               January 16, 2026   22 / 62
Queuing Model for Process State Transition Diagram with
Suspend States




Figure 8: Queuing Model for Process State Transition Diagram with Suspend
States
  Pearson Education   ©   2018     Processes              January 16, 2026   23 / 62
Reasons for Process Suspension




  Pearson Education   ©   2018   Processes   January 16, 2026   24 / 62
Suspended Processes

Swapping
Involves moving part of all of a process from main memory to disk

Because disk I/O is generally the fastest I/O on a system, swapping will
usually enhance performance
However, swapping is also an I/O operation and therefore there is the
potential for making the problem worse, not better.
Suspended Processes
When none of the processes in main memory is in the Ready state, the OS
swaps one of the blocked processes out on to disk into a suspend queue.

 ➤ The suspend queue is a queue of existing processes that have been temporarily
   kicked out of main memory, or suspended
 ➤ The OS then brings in another process from the suspend queue or it honors a
   new-process request
 ➤ Execution then continues with the newly arrived process
  Pearson Education   ©   2018        Processes                January 16, 2026    25 / 62
Process State Transition Diagram with Suspend States




          Figure 9: Process State Transition Diagram with Suspend States
  Pearson Education   ©   2018        Processes              January 16, 2026   26 / 62
Characteristics of a Suspended Process



Characteristics of a Suspended Process
  • The process is not immediately available for execution
  • The process was placed in a suspended state by an agent: either
    itself, a parent process, or the OS, for the purpose of preventing its
    execution
  • The process may or may not be waiting on an event
  • The process may not be removed from this state until the agent
    explicitly orders the removal




  Pearson Education   ©   2018     Processes              January 16, 2026   27 / 62
                         Process Description




Pearson Education   ©   2018     Processes   January 16, 2026   28 / 62
General Structure of Operating System Control Tables




         Figure 10: General Structure of Operating System Control Tables


  Pearson Education   ©   2018       Processes               January 16, 2026   29 / 62
Process Tables




  • Must be maintained to manage processes
  • There must be some reference to memory, I/O, and files, directly or
    indirectly
  • The tables themselves must be accessible by the OS and therefore are
    subject to memory management




  Pearson Education   ©   2018   Processes            January 16, 2026   30 / 62
Process Control Structures




To manage and control a process the OS must know:
  • The attributes of the process that are necessary for its management
  • Where the process is located




  Pearson Education   ©   2018     Processes           January 16, 2026   31 / 62
Process Control Structures


     Regarding process attributes
         • Each process has associated with it a number of attributes that are
           used by the OS for process control

Process Image
The collection of program, data, stack, and attributes is referred to as the
process image
     Regarding process location
         • A process must include a program or set of programs to be executed;
           A process will consist of at least sufficient memory to hold the
           programs and data of that process
         • Process image location will depend on the memory management
           scheme being used



  Pearson Education   ©   2018        Processes               January 16, 2026   32 / 62
Typical Elements of a Process Image


  1   User Data
             The modifiable part of the user space. May include program data, a
             user stack area, and programs that may be modified.
  2   User Program
             The program to be executed.
  3   Stack
             The execution of a program typically involves a stack that is used to
             keep track of procedure calls and parameter passing between
             procedures. So, each process has one or more stacks associated with it.
  4   Process Control Block
             Data needed by the OS to control the process (see Table 3.5).



*stacks are last-in-first-out (LIFO) data structures
   Pearson Education   ©   2018           Processes             January 16, 2026   33 / 62
User Processes in Virtual Memory




                           Figure 11: User Processes in Virtual Memory



  Pearson Education   ©   2018               Processes               January 16, 2026   34 / 62
Role of the Process Control Block

The most important data structure in an OS!
Process Control Block
  • Contains all of the information about a process that is needed by the
    OS
  • Blocks are read and/or modified by virtually every module in the OS
  • Defines the state of the OS


Difficulty is not access, but protection:
  • A bug in a single routine could damage process control blocks, which
    could destroy the system’s ability to manage the affected processes
  • A design change in the structure or semantics of the process control
    block could affect a number of modules in the OS


  Pearson Education   ©   2018    Processes             January 16, 2026   35 / 62
Typical Elements of a Process Control Block

  1   Processor State Information
      Consists of the contents of processor registers. Typically, the register
      set will include:
         • User-visible registers: A user-visible register is one that may be
           referenced by means of the machine language that the processor
           executes while in user mode.
         • Control and status registers: These are a variety of processor registers
           that are employed to control the operation of the processor.
           E.g.
                • Program counter: Contains the address of the next instruction to be
                  fetched
                • Condition codes: Result of the most recent arithmetic or logical
                  operation (e.g., sign, zero, carry, equal, overflow)
                • Status information: Includes interrupt enabled/disabled flags, execution
                  mode
         • Stack pointers: The stack pointer points to the top of the stack.


  Pearson Education   ©   2018            Processes                  January 16, 2026   36 / 62
Typical Elements of a Process Control Block
  2   Process Identification (using identifiers)
      Numeric identifiers that may be stored with the process control block
      include:
         • Identifier of this process
         • Identifier of the process that created this process (parent process)
         • User identifier

  3   Process Control Information
      Scheduling and state information that is needed by the OS to control
      and coordinate the various active processes.
      E.g.
         • Process state: Defines the readiness of the process to be scheduled for
           execution (e.g., running, ready, waiting, halted).
         • Priority: One or more fields may be used to describe the scheduling priority of
           the process. In some systems, several values are required (e.g., default,
           current, highest-allowable).
         • Scheduling-related information: This will depend on the scheduling algorithm
           used. E.g. the amount of time that the process has been waiting.
         • Event: Identity of event the process is awaiting before it can be resumed.

  Pearson Education   ©   2018           Processes                   January 16, 2026   37 / 62
Typical Elements of a Process Control Block

  6   Data Structuring
      A process may be linked to other process in a queue, ring, or some
      other structure.
      E.g.
         • All processes in a waiting state for a particular priority level may be linked in
           a queue.
         • A process may exhibit a parent-child (creator-created) relationship with
           another process.
         • The process control block may contain pointers to other processes to support
           these structures.
  7   Interprocess Communication
      Various flags, signals, and messages may be associated with
      communication between two independent processes.
         • Some or all of this information may be maintained in the process control
           block.



  Pearson Education   ©   2018            Processes                   January 16, 2026   38 / 62
Typical Elements of a Process Control Block


  8   Process Privileges
      Processes are granted privileges in terms of the memory that may be
      accessed and the types of instructions that may be executed.
         • In addition, privileges may apply to the use of system utilities and services.
  9   Memory Management
         • This section may include pointers to segment and/or page tables that
           describe the virtual memory assigned to this process.
 10 Resource Ownership and Utilization
         • Resources controlled by the process may be indicated, such as opened
           files.
         • A history of utilization of the processor or other resources may also be
           included; this information may be needed by the scheduler.




  Pearson Education   ©   2018            Processes                  January 16, 2026   39 / 62
Processes and Resources

A snapshot of resource allocation to three processes P1, P2 and P3.
Undashed lines indicate allocated resources, dashed lines indicate resources
still needed.




Figure 12: Processes and Resources (Resource Allocation at One Snapshot in
Time)



  Pearson Education   ©   2018      Processes              January 16, 2026   40 / 62
Process Identification


  • Each process is assigned a unique numeric identifier
       ➤ Otherwise there must be a mapping that allows the OS to locate the
         appropriate tables based on the process identifier
  • Many of the tables controlled by the OS may use process identifiers
    to cross-reference process tables
  • Memory tables may be organized to provide a map of main memory
    with an indication of which process is assigned to each region
       ➤ Similar references will appear in I/O and file tables
  • When processes communicate with one another, the process identifier
    informs the OS of the destination of a particular communication
  • When processes are allowed to create other processes, identifiers
    indicate the parent and descendants of each process



  Pearson Education   ©   2018        Processes                  January 16, 2026   41 / 62
Program Status Word
All processor designs include a register or set of registers, often known as
the program status word (PSW):
  • Contains condition codes plus other status information
  • EFLAGS register is an example of a PSW used by any OS running on
     an x86 processor




                                 Figure 13: x86 EFLAGS Register

  Pearson Education   ©   2018               Processes            January 16, 2026   42 / 62
Process List Structures




                                 Figure 14: Process List Structures


  Pearson Education   ©   2018                Processes               January 16, 2026   43 / 62
                               Process Control




Pearson Education   ©   2018         Processes   January 16, 2026   44 / 62
Modes of Execution




  1   User Mode
         • Less-privileged mode
         • User programs typically execute in this mode
  2   System Mode
         • More-privileged mode
         • Also referred to as control mode or kernel mode
         • Kernel of the operating system




  Pearson Education   ©   2018        Processes              January 16, 2026   45 / 62
Typical Functions of an Operating System Kernel



  1   Process Management
      e.g. creation, termination, scheduling, control block management,
      switching
  2   Memory Management
      e.g. address space allocation to processes, swapping
  3   I/O Management
  4   Support Functions
      e.g. interrupt handling




  Pearson Education   ©   2018     Processes                 January 16, 2026   46 / 62
Process Creation




Once the OS decides to create a new process it:
  • Assigns a unique process identifier to the new process
  • Allocates space for the process
  • Initializes the process control block
  • Sets the appropriate linkages
  • Creates or expands other data structures




  Pearson Education   ©   2018      Processes           January 16, 2026   47 / 62
Mechanisms for Interrupting the Execution of a Process




  Pearson Education   ©   2018   Processes   January 16, 2026   48 / 62
System Interrupts



  1   Interrupt
      Due to some sort of event that is external to and independent of the
      currently running process
         • Clock interrupt:
           The OS determines whether the currently running process has been
           executing for the maximum allowable unit of time (time slice).
           If it has, this process must be switched to a Ready state and another
           process dispatched.
               ➤ Time Slice: The maximum amount of time that a process can execute
                 before being interrupted




  Pearson Education   ©   2018         Processes               January 16, 2026   49 / 62
System Interrupts

  • I/O interrupt: The OS determines what I/O action has occurred. If the
    I/O action constitutes an event for which one or more processes are waiting,
    then the OS moves all of the corresponding blocked processes to the Ready
    state (and Blocked/Suspend processes to the Ready/Suspend state).
    The OS must then decide whether to resume execution of the process
    currently in the Running state or to preempt that process for a
    higher-priority Ready process.
  • Memory fault:
    The processor encounters a virtual memory address reference for a word that
    is not in main memory. The OS must bring in the block (page or segment) of
    memory containing the reference from secondary memory to main memory.
    After the I/O request is issued to bring in the block of memory, the process
    with the memory fault is placed in a blocked state; the OS then performs a
    process switch to resume execution of another process.
    After the desired block is brought into memory, that process is placed in the
    Ready state.


  Pearson Education   ©   2018       Processes               January 16, 2026   50 / 62
System Interrupts




  2   Trap
      An error or exception condition generated within the currently
      running process
      OS determines if the condition is fatal
         • Moved to the Exit state and a process switch occurs
         • Action will depend on the nature of the error and the design of the OS




  Pearson Education   ©   2018        Processes               January 16, 2026   51 / 62
Mode Switching



 • If no interrupts are pending the processor:
       ➤ Proceeds to the fetch stage and fetches the next instruction of the
         current program in the current process
 • If an interrupt is pending the processor:
       ➤ Sets the program counter to the starting address of an interrupt
         handler program
       ➤ Switches from user mode to kernel mode so that the interrupt
         processing code may include privileged instructions




  Pearson Education   ©   2018       Processes               January 16, 2026   52 / 62
Change of Process State

The steps in a full process switch are:
  1   Save the context of the processor
  2   Update the process control block of the process currently in the
      Running state
  3   Move the process control block of this process to the appropriate
      queue
  4   Select another process for execution
  5   Update the process control block of the process selected
  6   Update memory management data structures
  7   Restore the context of the processor to that which existed at the time
      the selected process was last switched out

If the currently running process is to be moved to another state (Ready,
Blocked, etc.), then the OS must make substantial changes in its
environment
  Pearson Education   ©   2018     Processes              January 16, 2026   53 / 62
     Supplemental Material: UNIX
      SVR4 Process Management




Pearson Education   ©   2018   Processes   January 16, 2026   54 / 62
UNIX SVR4


 • Uses the model where most of the OS executes within the
   environment of a user process
 • System processes run in kernel mode
      ➤ Executes operating system code to perform administrative and
        housekeeping functions
 • User Processes
      ➤ Operate in user mode to execute user programs and utilities
      ➤ Operate in kernel mode to execute instructions that belong to the
        kernel
      ➤ Enter kernel mode by issuing a system call, when an exception is
        generated, or when an interrupt occurs




 Pearson Education   ©   2018      Processes               January 16, 2026   55 / 62
UNIX Process States




  Pearson Education   ©   2018   Processes   January 16, 2026   56 / 62
UNIX Process State Transition Diagram




                      Figure 15: UNIX Process State Transition Diagram
  Pearson Education   ©   2018             Processes              January 16, 2026   57 / 62
Process Control

Process creation is by means of the kernel system call, fork()

When a process issues a fork() request, the OS performs the following
functions:
  1   Allocates a slot in the process table for the new process
  2   Assigns a unique process ID to the child process
  3   Makes a copy of the process image of the parent, with the exception
      of any shared memory
  4   Increments counters for any files owned by the parent, to reflect that
      an additional process now also owns those files
  5   Assigns the child process to the Ready to Run state
  6   Returns the ID number of the child to the parent process, and a 0
      value to the child process


  Pearson Education   ©   2018      Processes               January 16, 2026   58 / 62
After Creation



After creating the process the Kernel can do one of the following, as part
of the dispatcher routine:
   • Stay in the parent process. Control returns to user mode at the point
     of the fork() call of the parent.
   • Transfer control to the child process. The child process begins
     executing at the same point in the code as the parent, namely at the
     return from the fork() call.
   • Transfer control to another process. Both parent and child are left in
     the Ready to Run state.




  Pearson Education   ©   2018    Processes              January 16, 2026   59 / 62
UNIX Process Image




  Pearson Education   ©   2018   Processes   January 16, 2026   60 / 62
UNIX Process Table Entry




  Pearson Education   ©   2018   Processes   January 16, 2026   61 / 62
UNIX U Area




  Pearson Education   ©   2018   Processes   January 16, 2026   62 / 62
