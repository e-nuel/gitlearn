# gitlearn
This is a remote repo for testing git

So far we have been able to 
1. Create branches
2. Push codes
3. Add and commit codes
4. Merge Codes
5. Push code dorectries
6. Delete and roll back updates

Some Updates to Git Learn
UserAdmin
create new user -- sudo useradd <username>
Add user to group -- sudo usermod -aG <group> username
switch user  -- sudo su <username>
Git Stash
in the case where a change is added but not committed and you want to switch
 to another branch,
run git stash --> to hide the changes
This enables one to checkout to another branch

To get the changes back, 
git stash pop ---> to get the changes back

In other cases where you need an exitig code to be tested before 
adding the update, you can stash the code, test then pop it back to commit

In cases to revert to history,
run git log to get the update ID of the history
run git checkout <id>

that will indicate that you are not in the updated part of the code
  
DEVOPS AND DATABASES
The devps manager needs to understand how to 
* configure 
* replicate 
* manage databases

TYPES OF DATABASES
Structured



