Relational Database Design and SQL
      Install MySQL on Mac




                                     1 of 27
Introduction:
The goal of this document is to serve as a walkthrough of the installation of MySQL 8 on Mac.

For this document, we will be installing MySQL on your host computer.

Step 1: Install MySQL.
Go to http://mysql.com/downloads




                                                                                                2 of 27
Find and click MySQL Community (GPL) Downloads at the bottom




                                                               3 of 27
Click MySQL Community Server




                               4 of 27
MySQL Community server 8.0 should be display with Mac OS already be selected,

Click download next to the 64-bit DMG archive.




                                                                                5 of 27
You DO NOT need to sign up, instead click "No thanks, just start my download"




The DMG file should download.
(ex: mysql-8.0.22-macos10.15-x86_64.dmg)




                                                                                6 of 27
Click on the DMG in the downloads folder to run the image.

Run the PKG file from within the downloaded MySQL DMG image file




                                                                   7 of 27
You will need to click "Allow" to continue.




                                              8 of 27
Shown below is the MySQL Community Installation Wizard.




                                                          9 of 27
Proceed through the MySQL Installation Wizard.

Agree with the License Agreement.
Leave the default install directory.

When prompted, select “Strong Password Encryption” (SHA 256).




                                                                10 of 27
Create a new password for your MySQL root account.
IMPORTANT! Make sure you remember or write down this password! We will need this password to
login to MySQL.




                                                                                      11 of 27
Below is the screen showing the installation was completed successfully.
Click Close.




                                                                           12 of 27
Step 2: Install MySQL Workbench.
Go back to the MySQL website

http://mysql.com/downloads

and look for MySQL Workbench.




                                   13 of 27
Again, there is no need to login.




                                    14 of 27
Open the downloaded DMG file for MySQL Workbench.




Drag the MySQL Workbench icon to the Applications folder




                                                           15 of 27
Confirm it is installed by going into the mac launcher




Run MySQL Workbench.

If prompted that MySQL Workbench can't be open because it cannot be checked for malicious,




                                                                                             16 of 27
Go to System Preferences




                           17 of 27
Click Security and Privacy.
You should see that MySQL Workbench was blocked.
Click “Open Anyway”.




                                                   18 of 27
Click Open.




              19 of 27
This is MySQL Workbench.

MySQL Workbench will automatically add the default connection called "Local instance 3306".
You can create other connections (by clicking the plus symbol                        next to "MySQL
Connections") if you wish to explore other databases on other computers, but since MySQL has already
one we don't need to at this point.



Open a connection to your local instance by clicking on "Local instance 3306".




                                                                                              20 of 27
Enter the password you created when you installed MySQL Server.




This is the main screen for MySQL Workbench.




                                                                  21 of 27
Clicking on Schemas will show of the databases that you will create and the system databases.




Currently we haven't created any databases yet, so we don't have many databases. This view is currently
only showing the system database called sys. There are other system databases not shown here that
will talk about later.




                                                                                                22 of 27
There is a query editor window that will let you type SQL commands and run them.

Let's practice running a command.

In the query editor window type the following command:
SHOW VARIABLES LIKE 'version';

Note: the MYSQL keywords such as SHOW, VARIABLES and LIKE are case INSENSITIVE.
This means you can type them in all uppercase like this: SHOW VARIABLES LIKE 'version';
or in all lowercase like this: show variables like 'version';
and it makes no difference.

To run a command, click the lightning bolt with a cursor on it (   ).
Run the command.




                                                                                    23 of 27
You will see the result grid show up showing the result of your command.




In this case, the command, SHOW VARIABLES LIKE 'version';
will display the value of the version variable which contains a value
corresponding to version of MySQL you are running.
You should see your version look like something like 8.0.22.



Submit a screenshot with the version that is shown on the screen.
Filename: 01_MySQL_Version_Workbench.jpg




                                                                           24 of 27
Step 3: Run MySQL from the Command Line.



Open up the terminal app.




Run the following command:
mysql --version




If you will get an error message like this:
Command not found: mysql

The command FAILED, but don't worry, we can fix it by adding the mysql bin folder to the PATH
variable:

Run this (if you have the above error):
export PATH=/usr/local/mysql/bin:$PATH




Next, login to the MySQL Command Line Client using the following command:
mysql -u root -p

This is prompt for the mysql root password. Do you still remember your password?!?




                                                                                                25 of 27
If everything is good mysql should welcome you and you should see the prompt change to mysql>




Run the following command to show the MySQL version:
SHOW VARIABLES LIKE 'version';




                                                                                           26 of 27
Submit a screenshot with the version that is shown on the screen.
Filename: 02_MySQL_Version_Command_Line.jpg




Note: if you are still logged in at the mysql> prompt you can exit with the quit command.

Type quit to exit the MySQL Command Line Client tool.




That's it - you are done!




                                                                                            27 of 27
