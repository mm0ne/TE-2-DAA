import random


def main():
    gen(10000)
    gen(100000)
    gen(1000000)
    bnb_gen(10000)
    bnb_gen(100000)
    bnb_gen(1000000)


def gen(vertices: int) -> None:
    with open(f"nary_tree_{vertices}.txt", "w") as target:
        target.write(f"{vertices} {vertices - 1} 0\n")
        written = 2
        while vertices > 1:
            if vertices > 200:
                number_of_children = random.randrange(3, 11) % vertices
            else:
                number_of_children = random.randrange(1, 11) % vertices
            line = " ".join([str(written + j) for j in range(number_of_children)])
            written += number_of_children
            vertices -= number_of_children
            if len(line) >= 1 and vertices > 1:
                line += "\n"
            target.write(line)


def bnb_gen(vertices: int) -> None:
    with open(f"nary_tree_{vertices}.txt", "r") as src:
        if vertices == 10000:
            vertices = 100
        elif vertices == 100000:
            vertices = 300
        elif vertices == 1000000:
            vertices = 900

        lines = src.readlines()[1:]

        target = open(f"nary_tree_{vertices}.txt", "w")
        target.write(f"{vertices} {vertices - 1} 0\n")

        for line in lines:
            if str(vertices) in line:
                line = line[:line.find(str(vertices))] + str(vertices)
                target.write(line)
                break
            else:
                target.write(line)
        
        target.close()


if __name__ == "__main__":
    main()
