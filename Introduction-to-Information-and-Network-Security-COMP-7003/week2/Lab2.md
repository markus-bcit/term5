# Lab 2: Linux Basics

## Step 1: Baseline Observation
**Run `uptime` and record:**

```
❯ uptime 
 10:14:56 up 48 min,  1 user,  load average: 0.36, 0.50, 0.66
```
- Current time: `10:14:56`
- System uptime: `48 min`
- Load averages: `0.36, 0.50, 0.66`

**Run `top` and record:**
- Load averages (top): `0.41, 0.49, 0.63`
- Top CPU consumer: `brave` (browser)
- Memory usage (baseline): `5561.3`

---

## Step 2: Process Lifecycle Mechanics

### Anchor your shell
**Run `ps` for interactive shell:**
```
❯ ps
    PID TTY          TIME CMD
   5044 pts/0    00:00:00 fish
  12777 pts/0    00:00:00 ps
```
- PID:  `5044`
- TTY:  `pts/0`
- Command name: `fish` 

**Using `/proc` for that PID:**
- Complete command line (`/proc/<PID>/cmdline`): `/proc/5044/cmdline`
- Executable path (`/proc/<PID>/exe`): `/proc/5044/exe` 
- Current working directory (`/proc/<PID>/cwd`): `/proc/5044/cwd`

**Inspect open files (`/proc/<PID>/fd/`):**
1. FD: ____ | Target: ____ | Representation: ____
2. FD: ____ | Target: ____ | Representation: ____
3. FD: ____ | Target: ____ | Representation: ____

### Prove process termination
- New shell PID (via `pidof`): 
- PID/TTY verification: 
- Terminal closed? [ ]
- `kill <PID> -0` fails? [ ]
- `/proc/<PID>` exists? [ ]

---

## Step 3: Observe Idle Behaviour
- Load averages (start): 
- Load averages (end): 
- Processes remain same? [ ]

---

## Step 4: Controlled CPU Pressure
- Baseline `top` load/CPU: 
- Workload CPU usage: 
- Workload load averages: 
- Load averages after stopping: 

**Risk Path (CPU):**
Asset (____) -> Entry Point (____) -> Weak Spot (____) -> Damage (____)
- **CIA Classification: [Confidentiality / Integrity / Availability]** 
- **Justification:** 

---

## Step 5: Controlled Disk Pressure
- Baseline load averages: 
- Sustained write throughput (`iotop`): 
- Disk activity elevated? [ ]

**Risk Path (Disk):**
Asset (____) -> Entry Point (____) -> Weak Spot (____) -> Damage (____)
- **CIA Classification: [Confidentiality / Integrity / Availability]** 
- **Justification:** 

---

## Step 6: Controlled Memory Pressure
- Baseline load averages: 
- Resident memory usage: 
- Percent memory usage: 
- Process disappeared from `top`? [ ]
- Memory usage dropped? [ ]

**Risk Path (Memory):**
Asset (____) -> Entry Point (____) -> Weak Spot (____) -> Damage (____)
- **CIA Classification: [Confidentiality / Integrity / Availability]** 
- **Justification:** 
