# 0x02-shell_redirections
* 0-hello_world: Prints *Hello, World*, followed by a new line to the standard output
* 1-confused_smiley: Displays a confused smiley *"(Ôo)'*
* 2-hellofile: Display the content of the */etc/passwd* file
* 3-twofiles: Display the content of */etc/passwd* and */etc/hosts*
* 4-lastlines: Display the last 10 lines of */etc/passwd*
* 5-firstlines: Display the first 10 lines of */etc/passwd*
* 6-third_line: Displays the third line of the file *iacta*. The file *iacta* must be in the working directory
* 7-file: Creates a file named exactly *\\\*\\\\'"Holberton School"\'\\\*$\?\\\*\\\*\\\*\\\*\\\*:)* containing the text Holberton School ending by a new line
* 8-cwd_state: Writes into the file *ls_cwd_content* the result of the command *ls -la*. If the file *ls_cwd_content* already exists, it will be overwritten. If the file *ls_cwd_content* does not exist, it will be created
* 9-duplicate_last_line: Duplicates the last line of the file *iacta*, the file *iacta* must be in the working directory
* 10-no_more_js: Deletes all the regular files (not the directories) with a *.js* extension that are present in the current directory and all its subfolders
* 11-directories: Counts the number of directories and sub-directories in the current directory, the current and parent directories should not be taken into account and hidden directories should be counted
* 12-newest_files: Displays the 10 newest files in the current directory. One file per line and sorted from the newest to the oldest
* 13-unique: Takes a list of words as input and prints only words that appear exactly once. Input format one line, one word. Output format one line, one word. Words will be sorted
* 14-findthatword: Display lines containing the pattern *root* from the file */etc/passwd*
* 15-countthatword: Display the number of lines that contain the pattern *bin* in the file */etc/passwd*
* 16-whatsnext: Display lines containing the pattern *root* and 3 lines after them in the file */etc/passwd*
* 17-hidethisword: Display all the lines in the file /etc/passwd that do not contain the pattern *bin*
* 18-letteronly: Display all lines of the file */etc/ssh/sshd_config* starting with a letter. Will include capital letters as well
* 19-AZ: Replace all characters *A* and *c* from input to *Z* and *e* respectively
* 20-hiago: Removes all letters *c* and *C* from input
* 21-reverse: Reverse its input
* 22-users_and_homes: Write a script that displays all users and their home directories, sorted by users. Based on the */etc/passwd* file