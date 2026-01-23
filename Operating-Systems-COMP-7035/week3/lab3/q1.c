#include <stdio.h>
#include <stdlib.h>
 #include <unistd.h>

 int main(int argc, char *argv[]) {
 printf("hello (pid:%d)\n", (int) getpid());
 int rc = fork();
 if (rc < 0) {
 // fork failed
0 fprintf(stderr, "fork failed\n");
1 exit(1);
2 } else if (rc == 0) {
3 // child (new process)
4 printf("child (pid:%d)\n", (int) getpid());
5 } else {
6 // parent goes down this path (main)
7 printf("parent of %d (pid:%d)\n",
8 rc, (int) getpid());
9 }
0 return 0;
1 }
