def print_info(name, title="开发", gender=True):
    """
    :param title:职位
    :param name:姓名
    :param gender:True=男生/False=女生
    :return:
    """
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("[%s]%s 是 %s" % (title, name, gender_text))


# 假设班上的同学男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值!
# 缺省参数必须在参数列表末尾
print_info("小明")
print_info("老王")
print_info("小美", gender=False)
