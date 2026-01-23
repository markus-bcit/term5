# Added By User
- Take your time to fully extract text from images in slides or pdfs, they're the source of truth for a given topic, clarify with the user if needed.

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
*   **Distractors to avoid:** 
    *   **SMP** (Symmetric Multiprocessing) is a hardware architecture.
    *   **ABI** is an interface standard.
    *   **ISA** is the hardware/software boundary.

## ⚠️ Critical Definitions (Word-for-Word)

*   **Operating System:** A program that **controls the execution** of application programs and acts as an **interface** between applications and computer hardware.
*   **Process:** A **program in execution**.
*   **Reentrant:** Kernel routines must be **reentrant** to allow several processors to execute the same kernel code simultaneously.
*   **Privileged Instructions:** Instructions that can **only be executed by the monitor (OS)**.
*   **Time-Sharing Goal:** **Minimize response time**.
*   **Batch Multiprogramming Goal:** **Maximize processor utilization**.
