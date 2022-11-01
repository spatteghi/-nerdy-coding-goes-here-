print()
print("*** loopy test dos ***")
print()

for item in range(0, 5):
    print(item)

    # ask the user if they want to keep going
    keep_going = input("<enter> to keep looping, or any key to quit")

    # end loop if user presses <enter>
    if keep_going != "":
        break

print()
print("fried chicken")
print()