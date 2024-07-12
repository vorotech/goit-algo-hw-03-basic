"""Module for solving the Tower of Hanoi puzzle recursively."""

def hanoi(n, source, aux, target, state):
    """
    Solves the Tower of Hanoi puzzle recursively.

    Parameters:
    - n (int): The number of disks to be moved.
    - source (str): The source peg from which to move the disks.
    - aux (str): The auxilary peg to use for moving the disks.
    - target (str): The target peg to which the disks should be moved.
    - state (dict): The current state of the pegs and disks.
    """
    if n > 0:
        hanoi(n-1, source, target, aux, state)
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        hanoi(n-1, aux, source, target, state)

def main():
    """Main function."""
    n = int(input("Вкажіть кількість дисків: "))

    state = {
        'A': list(range(n, 0, -1)),
        'B': [],
        'C': []
    }
    print(f"Початковий стан: {state}")
    hanoi(n, 'A', 'B', 'C', state)
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
