import time

t_s = time.time()

def check_11(n_list):              # 이 함수는 Num이 11의 배수인지를 확인해준다. sum을 계산 후 몫과 나머지값을 return한다.
    n_list = [1] + n_list
    sum = 0
    s = 1
    for j in range(len(n_list), 0, -1):
        sum += n_list[j-1]*s
        s *= -1

    return sum//11, sum%11


a = 45*10**5
b = -45*10**5

# for i in range(100000):
#     ma = a//11
#     ra = a%11
#     mb = b//11
#     rb = b%11
#     # print(ma, ra, a&1, mb, rb, b&1)
#     a += 1
#     b -= 1


Data = []
m_list =[]
Length =[]

for i in range(10000):
    N_list = [int(i) for i in list(str(a))]
    Data.append(N_list)
    length = len(N_list)
    Length.append(length)
    if length > 1:
        m_list.append(N_list[-2])  # 아래 식에서 b
    else:
        m_list.append(int(c))
    a += 1

count = len(m_list)
coef = [0, 1]
sign = -1
for k in range(2, max(Length) + 1):
    coef.append(coef[0] * 100 + 9 * sign * (-1))
    for j in range(count):
        if k < Length[j]:
            m_list[j] += coef[2] * Data[j][-k - 1]
        elif k == Length[j]:
            # m, r = check_11(Data[j])
            Data[j] = [1] + Data[j]
            sum = 0
            s = 1
            for i in range(Length[j]+1, 0, -1):
                sum += Data[j][i-1]*s
                s *= -1
            m = sum//11
            r = sum%11

            if r == 0:
                m_list[j] += coef[2] + m
            elif Length[j] & 1 == 1 and r != 10:
                m_list[j] += coef[2] * (r + 1) + m
            elif Length[j] & 1 == 0 and r != 1:
                m_list[j] += coef[2] * (12 - r) + m + 1
            else:
                m_list[j] = 'IMPOSSIBLE'
    del coef[0]
    sign *= -1

for l in range(count):
    if Length[l] == 2:
        if Data[l][-1] == 0:
            m_list[l] = Data[l][-2] * 10
        else:
            m_list[l] = 'IMPOSSIBLE'

for n in range(count):
    print(f'{n+1}. {m_list[n]}')

print()
print("Runtime: %0.6f seconds"%(time.time() - t_s))

print()
print("Runtime: %0.6f seconds"%(time.time() - t_s))