print "Please enter 5 names: "
name1 = str(raw_input("Please enter the 1st name: "))
name2 = str(raw_input("Please enter the 2nd name: "))
name3 = str(raw_input("Please enter the 3rd name: "))
name4 = str(raw_input("Please enter the 4th name: "))
name5 = str(raw_input("Please enter the 5th name: "))

NameList = [name1, name2, name3, name4, name5]
new_NameList = sorted(NameList)
print "The names sorted are " + new_NameList[0] + ", " + new_NameList[1] + ", " + new_NameList[2] + ", " + new_NameList[3] + " and " + new_NameList[4] + "."

R = int(raw_input("Which name do you want to replace? (1-5) "))
new_NameList[R - 1] = str(raw_input("Please enter the new name: "))
new_NameList2 = sorted(new_NameList)
print "The names are " + new_NameList2[0] + ", " + new_NameList2[1] + ", " + new_NameList2[2] + ", " + new_NameList2[3] + " and " + new_NameList2[4] + "."
