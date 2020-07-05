x=[];
y=int(input("Enter size of list"));
for i in range(0,y):
    x.append(int(input("Enter values into list")));
print(x);
i=0;
for i in range(0,y):
    if(x[i]>0):
        print(x[i]);
    i=i+1;

#its not hardcoded to the input examples given
#I wasn't sure if we were supposed to but I did not do that. 
