# Added By User
- Take your time to fully extract text from images in slides or pdfs, they're the source of truth for a given topic, clarify with the user if needed.
- MAKE SURE to include key sub definitions
# OS Quiz Prep & Observations

This file tracks specific phrasing and patterns observed in quizzes/practice to match the instructor's strict expectations.

## 📝 Observed Question Phrasing

### 1. The ABI (Application Binary Interface)
*   **Question Style:** "The ABI is the machine code that is executed. True or False?"
*   **Correct Answer:** **False**.
*   **Definition to remember:** The ABI is the **interface** (the boundary/standard) between the application and the OS/Hardware. It defines the system call interface and binary portability. It is **not** the code itself, but the *rules* for how that code interacts with the system.

### 2. Memory Hierarchy Characteristics
*   **Question Style:** "What is NOT a key characteristic of the memory hierarchy?" (Options might include: Speed/Access Time, Cost, Capacity, Function).
*   **Key Concept:** The three trade-offs are **Cost, Capacity, and Access Time**. 
*   **Keywords:**
    *   **Decreasing** cost per bit.
    *   **Increasing** capacity.
    *   **Increasing** access time (slower).
    *   **Decreasing** frequency of access.

### 3. Interaction Languages/Standards
*   **Question Style:** "What language/standard is used to interact with the machine/OS?"
*   **Correct Term:** **JCL (Job Control Language)**.
*   **Context:** Used in Batch Systems to provide instructions to the **Monitor** (the early OS).

## ⚠️ Critical Definitions (Word-for-Word)

*   **Operating System:** A program that **controls the execution** of application programs and acts as an **interface** between applications and computer hardware.
*   **Process:** A **program in execution**. The unit of **Resource Ownership**.
*   **Thread:** The unit of **Dispatching/Execution**.
*   **Reentrant:** Kernel routines must be **reentrant** to allow several processors to execute the same kernel code simultaneously.
*   **Privileged Instructions:** Instructions that can **only be executed by the monitor (OS)**.
*   **Time-Sharing Goal:** **Minimize response time**.
*   **Batch Multiprogramming Goal:** **Maximize processor utilization**.
*   **Trap:** An error or exception condition generated **within the currently running process**.
*   **Interrupt:** An event that is **external** to and independent of the running process.

---

## 🏛️ Week 2: Processes & Threads (Course Specifics)

### 1. Table 4.2 Mappings (Strict Adherence)
*   **1:1 Mapping:**
    *   **Description:** Each thread is a unique process (Single-threaded).
    *   **System:** **Traditional UNIX**.
*   **M:1 Mapping:**
    *   **Description:** A process defines an address space; multiple threads are created/managed within it.
    *   **System:** **Windows NT, Solaris, Linux, OS/2, Mach**.

### 2. Registers (The "Brain")
*   **Processor State Information:** Consists of **User-visible registers**, **Control/Status registers (PSW)**, and **Stack Pointers**.
    *   *Note:* The **Process Identifier (PID)** is part of the PCB but **NOT** part of the "Processor State Information" (Register Set).
*   **PSW (Program Status Word):** Status, Condition Codes (Zero, Carry), Execution Mode (User/Kernel).
*   **PC (Program Counter):** Address of the **NEXT** instruction.
*   **IR (Instruction Register):** The **CURRENT** instruction.

### 3. Process States
*   **The Forbidden Transition:** You can **NEVER** go directly from **Blocked → Running**. You must go to **Ready** first.
*   **Suspend States:**
    *   **Blocked/Suspend:** Blocked process swapped to disk.
    *   **Ready/Suspend:** Ready process swapped to disk.
*   **Zombie State:** The process has been terminated but still has its task structure in the process table.

### 4. Thread Implementations
*   **ULT (User-Level):**
    *   Kernel sees 1 Process.
    *   **Fast switching** (No mode switch).
    *   **Drawback:** If one thread blocks, **Entire Process Blocks**. No SMP support.
    *   **Jacketing:** A workaround to convert blocking calls to non-blocking to prevent process freezing.
*   **KLT (Kernel-Level):**
    *   Kernel sees All Threads.
    *   **Slower switching** (Mode switch required).
    *   **Benefit:** True concurrency (SMP), one blocking thread doesn't stop others.

### 5. Quiz Logic & "Gotchas"
*   **Process Swapping != Spawning:** Swapping is moving to disk. Spawning is creating a new process.
*   **Suspending:** Suspending a process involves suspending **ALL** threads of the process.
*   **Creation Time:** Threads take **LESS** time to create than processes (Question asks "Which is NOT a characteristic" -> "More time to create").
