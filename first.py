
name = "yang heng"  
age = 20     
height = 175.67  
examscores = [85, 90, 78]
height = 1.75 
weight = 65.5  

print(f"姓名: {name} ") 
print(f"年龄: {age} ")
print(f"身高: {height}")
print(f"考试成绩: {examscores} ")

averagescore = sum(examscores) / len(examscores)
print(f"考试平均分: {averagescore:.1f}")

bmi = weight / (height **2)
bmirounded = round(bmi, 2)
print(f"BMI指数: {bmirounded}")

totalscore = sum(examscores)
averagescore = totalscore / len(examscores)
maxscore = max(examscores)
minscore = min(examscores)
print(f"总分: {totalscore}")
print(f"平均分: {averagescore:.1f}")
print(f"最高分: {maxscore}")
print(f"最低分: {minscore}")

namecapitalized = name.title()
print(f" 姓名首字母大写: {namecapitalized}")

nameparts = namecapitalized.split()
if len(nameparts) == 1:
    for i, char in enumerate(namecapitalized[1:], 1):
        if char.isupper():
            nameparts = [namecapitalized[:i], namecapitalized[i:]]
            break

print(f"分割后的姓名: {nameparts}")

if len(nameparts) >= 2:
    modifiedname = f"Wu {nameparts[1]}"
else:
    modifiedname = "Wu"  
print(f"修改后的姓名: {modifiedname}")


reversedname = modifiedname[::-1]
print(f"反转后的姓名: {reversedname}")

