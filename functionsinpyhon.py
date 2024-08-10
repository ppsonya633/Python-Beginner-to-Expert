def print_table(rows, columns):
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            print(i * j, end="\t")
        print()


# syndex def(functionname)(parameters):
#     function body

def addition(a,b):
    return a+b;

print(addition(2,3))