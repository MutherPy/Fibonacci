
def fibon(num_of_members :int) -> list:
    def recurs(num_of_members, fib_row = []):
        if num_of_members == 0:
            return fib_row
        if len(fib_row) < 2:
            fib_row.append(1)
            return recurs(num_of_members-1, fib_row)
        else:
            fib_row.append((fib_row[-1]+fib_row[-2]))
            return recurs(num_of_members-1, fib_row)
    a = recurs(num_of_members)

    return a


print(fibon(5))
