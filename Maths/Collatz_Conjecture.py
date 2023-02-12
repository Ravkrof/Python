import matplotlib.pyplot as plt


def collatz(n, count):
    if n == 1:
        return count
    elif n % 2 == 0:
        return collatz(n / 2, count + 1)
    else:
        return collatz(3 * n + 1, count + 1)


def get_n_vals_and_loops():
    try:
        start = int(input("Enter the start of the range (Number is included): "))
        end = int(input("Enter the end of the range (Number is included): ")) + 1
        n_vals = range(start, end)
        loops = []
        for i in n_vals:
            loops.append(collatz(i, 0))
        return n_vals, loops
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return get_n_vals_and_loops()


def TwoD_plot(n_vals, loops):
    plt.plot(n_vals, loops)
    plt.xlabel("Starting integer")
    plt.ylabel("Number of terms")
    plt.title("Collatz Conjecture")
    plt.show()


def ThreeD_plot(n_vals, loops):
    fig = plt.figure(facecolor='black')
    ax = fig.add_subplot(111, projection='3d', facecolor='black')
    ax.scatter(n_vals, [0]*len(n_vals), loops, c='white')
    ax.set_xlabel("n_vals", color='white')
    ax.set_ylabel("0", color='white')
    ax.set_zlabel("loops", color='white')
    ax.xaxis.label.set_color('white')
    ax.yaxis.label.set_color('white')
    ax.zaxis.label.set_color('white')
    ax.tick_params(colors='white')
    plt.show()

def print_loops(n_vals, loops):
    print("Number\tLoops")
    for i, loop in zip(n_vals, loops):
        print(f"{i}\t\t{loop}")


def menu():
    print("Select an option:")
    print("1. Plot Collatz Conjecture using a 2D plot")
    print("2. Print the number of loops for each integer in the range")
    print("3. Plot Collatz Conjecture using a 3D plot")
    print("4. Edit Values for Range")
    print("5. Quit")
    try:
        choice = int(input("Enter your choice (1-5): "))
        return choice
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
        return menu()


def main():
    n_vals, loops = get_n_vals_and_loops()
    choice = 0
    while choice != 5:
        choice = menu()
        if choice == 1:
            TwoD_plot(n_vals, loops)
        elif choice == 2:
            print_loops(n_vals, loops)
        elif choice == 3:
            ThreeD_plot(n_vals, loops)
        elif choice == 4:
            n_vals, loops = get_n_vals_and_loops()
        else:
            print("Invalid Choice \n")


if __name__ == "__main__":
    main()
