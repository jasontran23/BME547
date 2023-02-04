def coordinate_input():
    x1 = input("Enter x1: ")
    y1 = input("Enter y1: ")
    x2 = input("Enter x2: ")
    y2 = input("Enter y2: ")
    x3 = input("Enter x3: ")
    return (x1, y1), (x2, y2), x3


def y_online(A, B, x3):
    x1 = float(A[0])
    y1 = float(A[1])
    x2 = float(B[0])
    y2 = float(B[1])
    y3 = ((y2-y1)*(float(x3)-x1)/(x2-x1))+y1
    return y3


def y_output(y3):
    print(y3)


def y_driver():
    A, B, x3 = coordinate_input()
    y3 = y_online(A, B, x3)
    y_output(y3)


if __name__ == "__main__":
    y_driver()
