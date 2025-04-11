from django.template.defaultfilters import first


def case1(str_list: list):
    prefix = str_list[0]
    for i in range(1, len(str_list)):
        while str_list[i].find(prefix) != 0:
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


def case2(num_list: list):
    count = 0
    for left_pointer in range(len(num_list)):
        for right_pointer in range(left_pointer + 1, len(num_list)):
            current = num_list[left_pointer]
            compare = num_list[right_pointer]

            if current + compare == 100:
                print(f" {current}(第{left_pointer + 1}个) + {compare}(第{right_pointer + 1}个) = 100")
                count += 1
    return count


def case3(num_list: list):
    result = set()
    for first in num_list:
        if first == 0:
            continue

        for second in num_list:
            if second == first:
                 continue

            for third in num_list:
                if third == first or third == second:
                    continue

                number = str(first) + str(second) + str(third)
                result.add(number)

    return result


if __name__ == '__main__':
    """
        编写一个函数来查找字符串数组中的最长公共前缀。如果不存在公共前缀，返回空字符串示例1:flower,flow,flight
        从左到右，竖着看，第一列全是f，第二列全是l。第三列就不全一样了，所以「最长公共前缀」是 fl。
    """
    case_list = ["flower", "flow", "flight"]
    print(case1(case_list))

    """
        7个数字[1 15 35 55 65 85 99]找出2个数相加等于100，有几组。
    """
    case_list = [1,15,35,55,65,85,99]
    print(case2(case_list))

    """
        不重复的使用四个数字:1、8、0、3，能组成多少个互不相同的三位数
    """
    case_list = [1,8,0,3]
    print(case3(case_list))
    print(f"共{len(case3(case_list))}种组合")