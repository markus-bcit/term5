           Database Systems
       Install MySQL on Windows




Relational Database Systems
 Install MySQL on Windows




                                  1 of 37
                                           Database Systems
                                       Install MySQL on Windows



Introduction:
The goal of this document is to serve as a walkthrough of the installation of MySQL in Windows.




                                                                                                  2 of 37
                                           Database Systems
                                       Install MySQL on Windows

Step 1:
Download the MySQL Installer from https://dev.mysql.com/downloads/installer/
Look for the full version (larger download), not the web installer.
(ex: mysql-installer-community-8.0.39.0.msi)




Step 2:
Run the MySQL 8 Installer (ex: mysql-installer-community-8.0.39.0.msi)




                                                                               3 of 37
                                          Database Systems
                                      Install MySQL on Windows

Allow User Account Control to make changes to your device - YES




And again (click YES):




                                                                  4 of 37
                                       Database Systems
                                   Install MySQL on Windows

For Setup Type, choose "Custom".




                                                              5 of 37
                                                Database Systems
                                            Install MySQL on Windows

Note: Your version may be newer than the ones provided here. Ex: 8.0.41 instead of 8.0.39.
Please use the latest version of MySQL.

Include the following (4) in the install:
 - MySQL Server 8.0.39 (X64)
 - MySQL Workbench 8.0.39 (X64)
 - MySQL Shell 8.0.39 (X64)
 - Samples and Examples 8.0.39 (X86)




                                                                                             6 of 37
                                            Database Systems
                                        Install MySQL on Windows

Install Microsoft Visual C++ Redistributable if required – click "Execute", Agree to Terms and Conditions
and Install:




                                                                                                   7 of 37
                                            Database Systems
                                        Install MySQL on Windows

Click "Next" once the Redistributables have installed




                                                                   8 of 37
                                             Database Systems
                                         Install MySQL on Windows

Click Execute and sit back and watch the show:




Note: This portion of the install wizard changes frequently. If your steps are slightly different than the
ones shown here, you should be able to accept the defaults and continue with the installation.




                                                                                                     9 of 37
                                         Database Systems
                                     Install MySQL on Windows



Keep Development Computer as Config Type, Keep all other defaults
EXCEPT click "Show Advanced and Logging Options"




                                                                    10 of 37
                                           Database Systems
                                       Install MySQL on Windows

Authentication Method – Use Strong Password Encryption:
Notice: the many warnings about strong encryption.
This may cause some incompatibility problems but will see how to change this later if needed.




                                                                                                11 of 37
                                     Database Systems
                                 Install MySQL on Windows

Create a root password.

IMPORTANT: Write down your password so you can remember it!




                                                              12 of 37
                                            Database Systems
                                        Install MySQL on Windows

Create a Windows Service and run at startup (all default options):




                                                                     13 of 37
                                 COMP 2714 Relational Database Systems
                                      Install MySQL on Windows

eave the defaults for Server File Permissions (click "Next"):




                                                                         14 of 37
                                 COMP 2714 Relational Database Systems
                                      Install MySQL on Windows

eave the defaults for Server File Permissions (click "Next"):




                                                                         15 of 37
The defaults should also be ok for logging.

Binary and Slow Query logs should be enabled and General log should be disabled.




                                                                                   16 of 37
For case sensitivity it should be Lower Case (default):

Server ID can be left as 1.




                                                          17 of 37
Click "Execute" to apply configuration:




                                          18 of 37
If it worked – it should complete as follows; click "Finish":




                                                                19 of 37
Step 3:
Configure Samples and Examples, click "Next":




                                                20 of 37
Remember your password? Type it here and click "Check", then click "Next":




                                                                             21 of 37
Click Execute, wait until finished, click Finish:




                                                    22 of 37
Step 4:
Check to see if MySQL was installed.
We've already created a sample database, but we're going to check the Windows Service is running and
that we can connect to MySQL via the Command Prompt.



Next check to see if MySQL Server is running as a Windows Service:
Click Start Menu, type services, click Services Desktop App:




                                                                                              23 of 37
Find MySQL80 – Verify that Status = Running and Startup Type = Automatic:




                                                                            24 of 37
Verify you can connect to mysql via the Command Prompt:
Click Start Menu – type cmd and click Command Prompt Desktop App:




                                                                    25 of 37
At the prompt, type the following mysql -u root -p
This:
 - connects to the localhost (since we didn't specify another host with -h option)
 - specifies we want to connect with user root (with the -u option)
 - and forces a prompt for the password (with the -p option)


If you get the following error message:
'mysql' is not recognized as an internal or external command, operable
program or batch file.
follow the instructions below to add the mysql bin folder to the environment variables for the command
prompt:



Add MySQL to environment variables:
Click Start Menu – type environment
and click "Edit the system environment variables" Control Panel App:




                                                                                               26 of 37
Click Environment Variables:




                               27 of 37
Click Path, Click Edit:




                          28 of 37
Click New, Click Browse, find C:\Program Files\MySQL\MySQL Server 8.0\bin\, click OK:




Note: That's C:\Program Files\MySQL\MySQL Server 8.0\bin\
NOT C:\Program Files\MySQL\MySQL Shell 8.0\bin\

If you already have C:\Program Files\MySQL\MySQL Shell 8.0\bin\ it's ok to have both "Shell" and
"Server" in the path environment variable.

Click Ok, 3 times to close the environment variables windows.




                                                                                                   29 of 37
Step 5:

Open MySQL Workbench
Typing workb in the start menu was enough to find it for me.




                                                               30 of 37
The startup screen for MySQL Workbench looks like this:




If you don't have a “Local instance MySQL80” connection button on the bottom right create a new
connection by clicking the + next to MySQL Connections.




                                                                                              31 of 37
Creating a “Local instance MySQL80” connection button:
Give your new connection a name: Local instance MySQL80
Leave the Hostname as 127.0.0.1 (or you can use localhost – same thing).
Keep the default port 3306.
Click Test Connect to see if it works (it will prompt you for a password).
Click Ok.




                                                                             32 of 37
Open up Local instance MySQL80.

Double click the “Local instance MySQL80” connection button and enter your root password when
prompted.




                                                                                            33 of 37
Once open you should see a screen like this:




At this point I'll point out 4 main parts of the screen.

    1. There is a Schema (or Database) Section on the bottom right that shows all the databases,
       tables, views, procedures and functions with the databases.
    2. At the top there is a Query Section for typing in your queries or opening an SQL file. You can
       click on the lightning bolt with the cursor    to execute a single query at a time.
    3. Once you execute a query (for example a SELECT or SHOW TABLES) you'll see the results in the
       Result Grid below the Query Section
    4. The Output Section shows additional information about the queries that have run. It will show
       the number of rows returned, how long the query took to execute or it will show an error and a
       hint to find your syntax error in your query.




                                                                                               34 of 37
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

Submit a screenshot with the version that is shown on the screen.
Filename: 01_MySQL_Version_Workbench.jpg




                                                                                    35 of 37
Step 6:
Run MySQL from the Command Line.

If a Command Prompt window is still running, close it and restart it.


At the prompt, type the following mysql -u root -p
It will prompt for a password (still remember it?).
If everything is good mysql should welcome you and you should see the prompt change to mysql>




                                                                                           36 of 37
At the new mysql> prompt type:

show variables like "version";



Submit a screenshot with the version that is shown on the screen.
Filename: 02_MySQL_Version_Command_Line.jpg




Note: if you are still logged in at the mysql> prompt you can exit with the quit command.

Type quit to exit the MySQL Command Line Client tool.




                                                                                            37 of 37
