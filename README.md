# -
智能科学与技术
[分数.py](https://github.com/user-attachments/files/22597214/default.py)
# 提示用户输入分数
score = input("请输入分数（0-100）：")

# 检查输入是否为数字并在有效范围内
if score.isdigit():
    score = int(score)
    if 0 <= score <= 100:
        if score == 100:
            print("满分")
        if score >= 90:
            print("优秀")
        elif score >= 75:
            print("良好")
        elif score >= 60:
            print("及格")
        else:
            print("不及格")
    else:
        print("分数超出范围，请输入0到100之间的数字！")
else:
    print("无效输入，请输入一个数字！")
