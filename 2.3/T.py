'''
Хайпанём немножечко!
'''

number_n = int(input())
prev_hash = 0

for i in range(number_n):
    block = int(input())
    m_n = block // 256 ** 2
    r_n = (block // 256) % 256
    h_n = block % 256
    computed_hash = (37 * (m_n + r_n + prev_hash)) % 256
    if h_n >= 100 or h_n != computed_hash:
        print(i)
        break
    prev_hash = h_n
else:
    print(-1)
