#.../FILE CONVERSION POSITIONED_TO_DELIMITED /...

#paths for input and output files
inpath=r'D:\python_prj\source_file.txt'
outpath=r'D:\python_prj\dest_file.txt'

#Reading the file
with open(inpath,'r') as file:
  lines1=file.read()
  lines=lines1.split('\n') 

#Provide the starting positions in the list:ins_pos
ins_pos=[1,2,3,7,11,12,16,20,21,22,23,24,25,34,35,38,42,51,66,74,85,96,101,112,126]
#ins_pos = [int(f) for f in input().strip().split(',') ]

#Logic to insert at position
def abc():
  for i in range(0,len(ins_pos)):
    ins_pos[i]+=i
  return ins_pos 
abc()

#Reading line by line and appending delimiter at given position and finally writing to file
line_num=-1
for line in lines:
    ele=[]
    line_num+=1    
    for i in line:
      ele.append(i)
    for c in ins_pos: 
      ele.insert(c,'|') 
    final1="".join([str(st) for st in ele])
    #lines[line_num]=final1  --uncomment if u want to store final data to list for nxt operations
    with open(outpath,'a+') as file:
      file.write(final1+'\n')
print('FILE DELIMITED WITH | -SUCCESS')