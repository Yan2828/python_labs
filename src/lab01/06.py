N = int(input('in_1: '))
Tru, Fals = 0, 0
for i in range(N):
    a, b, c, d = map(str, input('in_'+str(i+2)+': '). split())
    if d == 'True':
        Tru += 1
    else:
        Fals += 1

print('out: ', Tru, Fals)