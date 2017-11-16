# Author:ZYM

data = {
    "北京":{
        "昌平":{
            "沙河":["oldboy","test"],
            "天通苑":["链家地产","我爱我家"]
        },
        "朝阳":{
            "望京":["奔驰","陌陌"],
            "国贸":{"CICC","HP"},
            "东直门":{"Advent","飞信"}
        },
        "海淀":{
        }
    },
    "山东":{
        "德州":{},
        "青岛":{},
        "济南":{}
    },
    "广东":{
        "东莞":{},
        "常熟":{},
        "佛山":{}
    },
}


exit_flag = True
while exit_flag:
    for i1  in data:
        print(i1)
    choice1 = input("选择进入1,q退出整个系统，b返回上一级>>:")
    if choice1 in data:
        while exit_flag:
            for i2 in data[choice1]:
                print("\t",i2)
            choice2 = input("选择进入2,q退出整个系统，b返回上一级>>:")
            if choice2 in data[choice1]:
                while exit_flag:
                    for i3 in data[choice1][choice2]:
                        print("\t\t",i3)
                    choice3 = input("请选择进入3,q退出整个系统，b返回上一级>>:")
                    if choice3 in data[choice1][choice2]:
                        for i4 in data[choice1][choice2][choice3]:
                            print("\t\t\t",i4)
                        choice4 = input("目录查询完成，q退出整个系统，按b返回>>")
                        if choice4 == 'b':
                            pass
                        elif choice3 == 'q':
                            exit_flag = False
                    elif choice3 == 'b':
                        break
                    elif choice3 == 'q':
                        exit_flag = False
                    else:
                        exit("没有在三级目录中")
            elif choice2 == 'b':
                break
            elif choice2 == 'q':
                exit_flag = False
            else:
                exit("没有在二级目录中")
    elif choice1 == 'b':
        break
    elif choice1 == 'q':
        exit_flag = False
    else:
        exit("没有在一级目录中")

        # gitbug test again