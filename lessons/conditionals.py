"""Checks light, if green, says go."""

light: str = input("What color is the light? ")

if(light == "Green"):
    print("Go!")
    print("Drive safe! Love, mom.")
else:
    if(light != "Red"):
        if(light != "Yellow"):
          print("Do a backflip")
    if(light == "Yellow"):
        print("Slow down.")
    if(light == "Red"):
         print("Stop!")
print("Don't look at your phone.")