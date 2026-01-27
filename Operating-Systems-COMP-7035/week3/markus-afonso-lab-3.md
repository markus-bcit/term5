# Lab 3: Process API Coding Questions

## Question 1
**Prompt:** Write a program that calls `fork()`. Access a variable `x` (e.g., set to 100) before forking. What value is `x` in the child? What happens when both change `x`?

*   **Code:** `q1.c`
*   **Answer:**
    *   Value in child: [Fill in]
    *   Effect of concurrent changes: [Fill in]
*   **Output:**
    *   [Paste Output Here]

## Question 3
**Prompt:** Child prints "hello", Parent prints "goodbye". Ensure Child prints first *without* using `wait()`.

*   **Code:** `q3.c`
*   **Answer:**
    *   How achieved without wait: [Fill in]
*   **Output:**
    *   [Paste Output Here]

## Question 5
**Prompt:** Use `wait()` in the parent. What does it return? What happens if you use `wait()` in the child?

*   **Code:** `q5.c`
*   **Answer:**
    *   `wait()` returns: [Fill in]
    *   `wait()` inside child: [Fill in]
*   **Output:**
    *   [Paste Output Here]

## Question 6
**Prompt:** Use `waitpid()` instead of `wait()`. When is it useful?

*   **Code:** `q6.c`
*   **Answer:**
    *   When is `waitpid()` useful: [Fill in]
*   **Output:**
    *   [Paste Output Here]

## Question 8
**Prompt:** Create two children. Connect stdout of one to stdin of the other using `pipe()`.

*   **Code:** `q8.c`
*   **Answer:**
    *   Description of functionality: [Fill in]
*   **Output:**
    *   [Paste Output Here]
