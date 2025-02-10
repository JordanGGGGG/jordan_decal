# 1) Suppose your current working directory is ~/Desktop/classes/python_decal/. What command would allow you to navigate directly to ~/Desktop?
#Answer: cd... /Desktop
# 2) What does ~/ mean?
#Answer: This is the symbol for the main directory. This is the directory that you start in when you first open the terminal and you can access all other directories from here.
# 3) What's the difference between and abolute and a relative path in your terminal?
#Answer: An absolute path allows you to go to a directory from the main directory. Example: cd ~/python_decal/jordan_decal. A relative path allows you to go to another directory from anywhere on the computer. Example: cd... /jordan_decal.
# 4) What command would bring you back to your home directory?
#Answer: cd ~
# 5) If you called rm ./ in your current working directory, what would it do? 
#Answer: It would attempt to remove your current directory but that would just result in an error since that isn't allowed.
# 6) In your current working directory, what does calling "git add" do? What about "git commit"? What about "git push"?
#Answer: git add would add all the files in that directory into the staging area. Using git commit will add all of the files and directories in the staging area onto your local repository. Git push adds your repository to github, which you can then share with others.
# 7) Let's say you call "git add" in your current working directory and then "git status". What message would appear? What is it telling you?
#Answer: It would tell you that you are on branch master and it would show everything that is in the working tree. This is a list of everything that is ready to be committed to the local repository.
# 8) What has been the most frustrating error or bug you've encountered in this class so far? How did you troubleshoot and resolve it?
#Answer: I haven't encountered any frustrating bug or errors in this class but one bug that I remember being resolved was when trying to push using the git push command. On git bash on windows, you must type git push origin master instead of origin main since it is a different name on windows than on mac.
# 9) How does cloning a repository differ from pulling from a repository?
#Answer: Cloning a repository creates a copy on your computer of that repository. Pulling from a repository will sync the files from the repository onto your local computer. This allows you to work directly on those files if you have access to it.
# 10) Tell me a fun fact!
#Answer: A lot of the same commands from git bash (e.g. ls, pwd, cd, etc) work the same on windows powershell and I found that interesting.
