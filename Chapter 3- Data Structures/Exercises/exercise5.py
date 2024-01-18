invited = ["Ronaldo","Messi","Neymar"]
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])
out_guest = invited.pop(1)
print(out_guest, "couldn't make the dinner!")
new_guest = "Ozil"
invited.insert(1,new_guest)
print("You are welcomed to dinner at my house this afternoon,", invited[0])
print("You are welcomed to dinner at my house this afternoon,", invited[1])
print("You are welcomed to dinner at my house this afternoon,", invited[2])