# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    # See PyCharm help at https://www.jetbrains.com/help/pycharm/
def multiply(a, b):
    return a * b

def duck_duck_goose(players, goose):
    c = goose % len(players)
    print(players[c-1])
    return players[c-1]

def count_bits(n):
    #binn = bin(n)
    binn=''
    result = 0
    while n>0:
        binn = str(n%2) + binn
        if (n%2) > 0:
            result = result+1
        n = n // 2
    print(binn)
    print(result)
    return result

def up_array(arr):

    result = []
    l = len(arr)
    oldnum = 0
    for i in range(len(arr)):
        inx = l-i-1
        if arr[inx] < 0:
            return None
        oldnum = oldnum + arr[inx] * (10 ** i)
    newnum = oldnum + 1

    lnew = len(str(newnum))
    if lnew < l:
        result.append(0)
    for i in range(lnew):
        pw = lnew - i - 1
        num = newnum // (10**pw)
        result.append(num)
        newnum = newnum - num * (10 ** pw)
    print(result)
    return result



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    up_array([1,5,4])

