def same(a):
    a=list(a.lower())
    if a==reversed(a):
        return True
    else:
        print(a)
        return False
def main():
    a=input()
    if same(a)==True:
        print('yes')
    else:
        print('no')
main()