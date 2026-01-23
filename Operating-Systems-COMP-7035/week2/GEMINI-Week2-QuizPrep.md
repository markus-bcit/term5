# Week 2 OS Quiz Prep (Strict Definitions & Table 4.2)

## ⚠️ CRITICAL: Table 4.2 Mappings (Memorize This!)

**Do NOT use outside knowledge. Use THIS table.**

| Ratio | Description | Example Systems |
| :--- | :--- | :--- |
| **1:1** (One-to-One) | Each thread of execution is a unique process with its own address space and resources. | **Traditional UNIX implementations** |
| **M:1** (Many-to-One) | A process defines an address space and dynamic resource ownership. Multiple threads are created and managed by that process. | **Windows NT, Solaris, Linux, OS/2, Mach** |

*   **Key Takeaway:** If the question asks "Which system uses M:1?" or "Which system uses Multithreading as defined in Table 4.2?", the answer is **Windows NT, Solaris, Linux**.
*   **Key Takeaway:** If the question asks "Which system uses 1:1?", the answer is **Traditional UNIX**.

---

## 📝 Critical Definitions (Word-for-Word)

### Process
*   **Definition:** "A program in execution. An instance of a running program. An entity that can be assigned to, and executed on, a processor."
*   **Two Essential Elements:**
    1.  **Program Code:** May be shared.
    2.  **A set of data:** Associated with that code.
*   **Role:** The unit of **Resource Ownership**.

### Threads
*   **Definition:** "A dispatchable unit of work. Includes a processor context and its own data area for a stack."
*   **Role:** The unit of **Dispatching/Execution**.

### The 4 Benefits of Threads
1.  Less time to **create**.
2.  Less time to **terminate**.
3.  **Switching** is faster.
4.  Efficiency in **communication**.

---

## 💻 Registers (The "Which Address?")

*   **Program Counter (PC):** Address of the **NEXT** instruction.
*   **Instruction Register (IR):** The **CURRENT** instruction.
*   **Stack Pointer (SP):** Address of the **TOP** of the stack.

---

## 🔄 Process States (5-State Model)

*   **Running -> Ready:** Time-out (Timer Interrupt).
*   **Running -> Blocked:** I/O Wait.
*   **Blocked -> Ready:** Event Occurs.
*   **Forbidden Move:** Blocked -> Running (Must go to Ready first).

---

## 🧪 Practice Quiz (Based on Table 4.2)

1.  **T/F:** According to Table 4.2, Traditional UNIX implementations use the M:1 (Many-to-One) mapping.
2.  **T/F:** Windows NT and Linux are examples of systems that use the M:1 threading model.
3.  **T/F:** A process is the unit of dispatching.
4.  The **Program Counter** holds the address of the ________ instruction.
5.  What state does a Running process go to if it gets a **Time-out**?