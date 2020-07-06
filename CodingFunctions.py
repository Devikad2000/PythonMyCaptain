#accessing elements from a tuple using position and finding value
i=0;
myTuple=("red","yellow","black");
print(myTuple);
y=int(input("Which element would you like to access? Enter position"));
print(myTuple[y-1]);

#accessing elements from a tuple using value and finding position
i=0;
myTuple=("red","yellow","black");
print(myTuple);
z=input("Which element would you like to access? Enter value");
for i in range(0,3):
    if(myTuple[i]== z):
         print("element "+z+" is in postition:");
         print(i);

#assigning values to different lists
k=0;
myList=[1,2,3,4,5];
print(myList);
a=int(input("How many elements would you like to insert"));
while(k<a):
    x=int(input("Which element would you like input"));
    myList.append(x);
    k=k+1;
print(myList);

#Deleting different dictionary elements
c="y";
myDict={"A":"Apple","B":"Bat","C":"Cat","D":"Dog"};
print(myDict);
while(c=="y"):
    b=input("Enter which element to delete");
    del myDict[b];
    c=input("would you like to delete again? if so enter y else n");
print(myDict);
