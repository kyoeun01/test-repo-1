print('이름: 김경식', '학번: 201900543','학과: 컴퓨터전자시스템공학부')
print('오픈소스SW및실습')

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
