well_depth = int(input("Enter the depth of the wall: "))
frog_jump = int(input("Enter height the frog can jump up: "))
frog_slip = int(input("Enter the height the frog slips down: "))

current_depth = well_depth - frog_jump
day = 0

if frog_jump == frog_slip:
    print("The frog is always stuck in the well.")
else:
    while current_depth > 0:
        day += 1
        print(f"On day {day} the frog leaps to the depth of {current_depth} meters.")
        current_depth += frog_slip
        print(f"At night he slips down to the depth of {current_depth} meters.")
        current_depth -= frog_jump
    
if day != 0:
    print(f"The frog gets out of the well on day {day+1}.")

