'''Muhammad Khan 
November 4th 2021
Calculates the distance a suspended object falls given a gravity and time'''

print("This program calculates the distance a suspended object falls","given a gravity and time")
gravity=input("Insert Gravity Here in pixels per second squared: ") #Get gravity from user
gravity=int(gravity) #Convert string to int
fps=input("Enter FPS here: ") # Get FPS from user
fps=int(fps) # Convert string to int
frames=input("Enter the number of frames here: ") # Get number of frames from user
frames=int(frames) # Convert string to int
time=frames/fps # Calculate time object is falling
distance=0.5*gravity*time**2
print("It will drop", distance, "pixels in", time, "seconds") # Output time to user
