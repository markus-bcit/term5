Lab 2: Linux Basics
Step 1: Baseline Observation
Run uptime and record:


  ❯ uptime
   10:14:56 up 48 min,      1 user,   load average: 0.36, 0.50, 0.66


   Current time: 10:14:56
   System uptime: 48 min
   Load averages: 0.36, 0.50, 0.66

Run top and record:

   Load averages (top): 0.41, 0.49, 0.63
   Top CPU consumer: brave (browser)
   Memory usage (baseline): 5561.3




Step 2: Process Lifecycle Mechanics
Anchor your shell
Run ps for interactive shell:


  ❯ ps
      PID TTY            TIME CMD
     4421 pts/0      00:00:00 fish
     6930 pts/0      00:00:00 ps


   PID: 4421
   TTY: pts/0
   Command name: fish

Using /proc for that PID:

   Complete command line ( /proc/<PID>/cmdline ):
  ❯ cat /proc/4421/cmdline
  fish


      Executable path ( /proc/<PID>/exe ): /proc/4421/exe


  ❯ ls -al exe
  lrwxrwxrwx 1 markus markus 0 Jan 13 12:26 exe -> /usr/bin/fish*


      Current working directory ( /proc/<PID>/cwd ): /proc/4421/cwd


  /proc/4421🔒
  ❯ ls -al cwd
  lrwxrwxrwx 1 markus markus 0 Jan 13 12:51 cwd -> /proc/4421/


Inspect open files ( /proc/4421/fd/ ):

 1.
         FD: 0
         Target: /dev/pts/0
         Representation: the terminal I'm using
 2.
         FD: 3
         Target: /proc/4421/fd/
         Representation: a directory handle
 3.
         FD: 4
         Target: /run/user/1000/fish_universal_variables.notifier|
         Representation: a data pipe to another program for notifications

Prove process termination
      New shell PID (via pidof ): 9608
      PID/TTY verification:


  ❯ ps
         PID TTY             TIME CMD
        9608 pts/2       00:00:00 fish
        9938 pts/2       00:00:00 ps
   Terminal closed? Yes
    kill <PID> -0 fails? Yes


  ❯ kill 4421
  kill: (4421): No such process


    /proc/<PID> exists? No:


  ❯ ls /proc/4421
  ls: cannot access '/proc/4421': No such file or directory




Step 3: Observe Idle Behaviour
   Load averages (start): load average: 0.62, 0.58, 0.62
   Load averages (end): load average: 0.35, 0.51, 0.59
   Processes remain same?
         No they've decreased a bit




Step 4: Controlled CPU Pressure
   Baseline top load/CPU:
         Around 4% with top consumer being obsidian (md application, I'm using linux as my
         regular OS)
   Workload CPU usage: 11.7%
   Workload load averages: load average: 1.10, 0.66, 0.61
   Load averages after stopping: load average: 0.49, 0.57, 0.59

Risk Path (CPU):
Interactive user shell -> User command execution -> single process allowed to consume 100%
CPU -> Keystrokes in other terminals are delayed

CIA Classification: Availability

   Justification: Higher CPU usage can impact other applications, causing them to slow down
   or possibly crash/fail.
Step 5: Controlled Disk Pressure
   Baseline load averages:


  Total DISK READ:                 0.00 B/s | Total DISK WRITE:              0.00 K/s
  Current DISK READ:               0.00 B/s | Current DISK WRITE:             0.00 B/s


   Sustained write throughput ( iotop ):


  ❯ dd if=/dev/zero of=/tmp/lab-io-test bs=1M count=1024 status=progress
  1024+0 records in
  1024+0 records out
  1073741824 bytes (1.1 GB, 1.0 GiB) copied, 0.346526 s, 3.1 GB/s


   Disk activity elevated?
         Yes, write peaks significantly, saw around Total DISK WRITE: 100 K/s and
         Current DISK WRITE: 500 B/s

Risk Path (Disk):
Local file system -> User file creation (dd) -> User process allowed unrestricted disk I/O ->
Other file operations hang or time out

CIA Classification: Availability

   Justification: Higher Disk usage can bottleneck programs causing them to slow down to
   crash/fail.




Step 6: Controlled Memory Pressure
   Baseline load averages: load average: 0.57, 0.50, 0.42


  load average: 1.84, 0.95, 0.61


  15582 markus        20     0     37.3g   24.8g   4896 D    32.5   79.8     0:19.70 perl


   Resident memory usage: 24.8g
   Percent memory usage: 79.8
   Process disappeared from top ?
         No, it stayed there till my computer froze after about 2 minutes
   Memory usage dropped?
         No, it stayed consistent

Risk Path (Memory):
System Memory -> Script execution -> Process allowed to allocate RAM exceeding physical
limits -> System freezes and requires reboot

CIA Classification: Availability

   Justification: My computer froze after a couple minutes, requiring a reboot
