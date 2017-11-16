# Author:ZYM



goods_list = [["iphone",8000],["macpro",12000],["book",300],["coffee",30],["bike",600]]#商品列表
bought_list = []#购物车列表

salary = input("请输入您的工资：")

if salary.isdigit():#判断工资是否为数字
    salary = int(salary)#强制转换为int类型
    while True:#执行死循环
        for i in goods_list:
            print(goods_list.index(i),i)
        user_choice = input("请输入你想要买的商品编号：")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice < len(goods_list) and user_choice >= 0:#判断选择商品ID是否超限
                p_item = goods_list[user_choice]
                if salary >= p_item[1]:#买得起
                    bought_list.append(p_item)
                    salary -= p_item[1]
                    print("恭喜您购买成功，您的账户余额为：",salary)
                else:#买不起
                    print("您的账户余额不足")
            else:#商品ID超限
                print("您所选择的商品不存在")
        elif user_choice == 'q':#如果输入的是‘q’执行退出并打印购物车清单和余额
            print("-------您的购物清单------")
            for i in bought_list:
                print(i)
            print("您的账户余额为：",salary)
            exit()
        else:#输入了其他非法的字符
            print("错误的选择")
else:
    print("请输入整数的工资")

