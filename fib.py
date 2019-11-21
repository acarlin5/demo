def fib():
    fibs = [0, 1]

    for i in range(1,99):
        i += 1
        fib = (fibs[i-1]) + (fibs[i-2])
        
        fibs.append(fib)

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
