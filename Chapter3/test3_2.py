# 从上到下顺序执行语句
name = 'Storm'
print('start')
print('Hello {}'.format(name))
print('end')

# 分支语句
today_weather = input("Please input the weather today:")
if today_weather == '下雨':
    print("打伞")
elif today_weather == '起雾':
    print("开雾灯")
else:
    print("省点事")

# 循环语句--for
for i in 'storm':
    print(i)

# 循环语句--while
sum = 0
n = 100
while n > 0:
    sum = sum + n
    n-=1

print(sum)

# continue跳过
for i in 'storm':
    if i == 'o':
        continue
    print(i)

# break终止
for i in 'storm':
    if i == 'o':
        break
    print(i)