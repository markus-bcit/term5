# Lab 1: Processes, Linux Commands, and Program Execution

## Task 1: Compile and Run assembly_example

**1. What is the name of the register pointing to the next instruction?**

**Answer:** IP

**2. What changes were observed to the registers and to the memory after running the program?**
*(Note: Don’t include any memory addresses that change on compilation.)*

**Answer:** 

Registers:
       * r0: Changed to 0x1F
       * r1: Changed to 0x5
       * r2: Changed to 0x1A
       * r3: Changed to 0x20
   * Memory:
       * The memory of answer changed to 0x1a
---

## Task 2: Observing Processes

### Observing Processes with top

**3. Look up S -- the process statuses in the top manual. Copy and paste them below.**

**Answer:**![[Pasted image 20260109125714.png]]


### Checking System Details

**4. How many processors are there? Submit a screenshot of the cpus with your answer.**

**Answer:**
![[Pasted image 20260109125800.png]]

**5. Count the number of tasks (processes) running. Submit a screenshot of process statuses to confirm.**

**Answer:** 412 total,![[Pasted image 20260109130658.png]] 

### Tasks and Multitasking

**6. Explain how the OS manages more tasks than processors using multitasking.**

**Answer:** The OS uses Time Slicing, where it uses timer interrupts at a regular interval, usually 0.2s. It pauses the current program and switches to a different one. Or in other words, it uses context switching.  

### Using ps Instead of top

**7. Use `ps` commands to track and manage processes. How is it different from `top`?**

**Answer:** `top`uses a more interactive and dynamic experience, constantly updating as the programs use more/less usage. `ps` is static that works well for outputting to things like a file or program. 

---

## Exploring /proc Directory

### Process Details in /proc

**8. What information does `/proc/<PID>` provide?**

**Answer:** `/proc/<PID>` provides execution context for the given `PID`. It contains the state for the process.

### Manual Exploration

**9. Summarize your findings for the following from `man proc`:**

*   **Process states:**
    *   **Answer:** 
	    * R (running) - Running or waiting for the CPU 
	    * S (sleeping) - Waiting for something, like I/O to complete
	    * D (Disk sleeping) - Uninterruptible  Waiting for disk I/O to complete
	    * Z (zombie) - Terminated but parent process hasn't received the exit code 
	    * T (stopped) - Stopped by signal 
*   **cmdline:**
    *   **Answer:**  Contains the complete command line for the process, including all args.
*   **stat:**
    *   **Answer:** display status information about the process. 
