def main():
    print("Boil? (Y/N)")
    val = input()
    if val == "Y":
        from time import sleep
        boiling = 'BOILING . . .'
        for i in range(10):
         print(boiling[i], sep=' ', end=' ', flush=True); sleep(0.5)
    elif val == "N":
        print("Turning Off")
    else:
        print("You didn't enter a correct input!")
        main()

main()