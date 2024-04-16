'''
Something with a lot of functions that take some time (for profiling)
'''

# to create a code profile
# python -m cProfile -o sl.prof slow_prog.py

# to run snakevis to visually explore this profile
# snakevis: https://jiffyclub.github.io/snakeviz/
# snakeviz sl.prof

import time

def main():
    N = 5000
    M = 1000

    answer = do_it_several_times(N,M)
    print(answer)

def slow_cumsum(N):
    ans = 0
    for n in range(N):
        ans += n
    return ans

def do_it_several_times(N,M):
    ans = 0
    for n in range(N):
        print(f'Iternation number {n}')
        cum_sum = slow_cumsum(M+n)
        # do some other computations
        ans += cum_sum - n
    return ans

if __name__ == "__main__":
    tic = time.time()
    main()
    timediff = time.time() - tic
    print('Elapsed time: {}'.format(timediff))