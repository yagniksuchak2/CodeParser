Project Outline:

The set of scripts in this directory are collectively used to download commit log from github and then parse it to get data(and statistics) corresponding to exception handling code.

Following are the main scripts:

allRunn.py
ghProc.py
ghLogDb.py
logChunk.py
PatchMethod.py

ghProc.py -> This script can be used to process log corresponding to one github project. It takes argument as the directory containing log corresponding to a github project. For example, if there is a project name android(Directory path /home/username/top_java/android/) which contains the log file to be processed(all_changed_log.txt). The script would be ran using following command on CLI.

python ghProc.py /home/username/top_java/android

Note: The argument passed is the path of the directory containing the logfile and not the logfile itself.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

ghLogDb.py -> This script is called by ghProc.py

It defines 3 classes which are as follows.

Patch
Sha
ghLogDb

ghLogDb object is created in ghProc.py and would contain following members.

log_file : The absolute path of logFile. In out example it would be /home/username/top_java/android/all_changed_log.txt
project_name : Name of the project. In out example it would be android.
curr_method : The present method at any instance of code execution. This is nothing but context i.e. line corresponding to @@ ...@@ in log.


Some of the important methods of ghLogDb class are:

__str__
isSha -> determine if line is SHA? (uses regular expression + commit key)
isAuthor -> determine if this is the author line and extract the “Author:” field.
isDate -> determine if line is the date line.
createPatchWithNoPrevVersion -> identifies and creates a Patch object for a new file.
createPatch -> identifies and creates a Patch object for an existing file.
processPatch -> Given a patch object and a line, determines if we have a new patch to create, or 
processLog
processLastChunk

The most important method is processLog which processes the logfile.


logChunk.py : This script processes the actual code from the log file. The file consist of Shas(Commit ids). Each Sha would have one or more diffs(patches). Each patch would have a code chunk. logChunk.py processes that code chunk.




allRunn.py -> The above all scripts can be collectively used to process log of one github project. Now, if we want to run these script on multiple script, we can use allRunn.py script.This script takes argument as the directory containing directories that contains the logfile for github projects. 

For example, If we want to generate statistics about all top_java projects. We can have a directory structure like /home/username/top_java and in top_java directory we have java_project1, java_project2, java_project3. So, following would be the command to run allRunn.py script.

python allRunn.py /home/username/top_java









