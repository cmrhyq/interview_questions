<div style="font-family: 'Kanit', sans-serif;text-align: center;border: 10px solid #fff;box-shadow: 1px 1px 2px #e6e6e6;background: linear-gradient(to left top, #11998e, #38ef7d); padding: 50px 0;">
<div style="color: #fff;">
    <h3 style="font-size: 25px;font-weight: 600;letter-spacing: 1px;text-transform: uppercase;margin: 0;">
       LeetCode Question
    </h3>
    <span style="font-size: 16px;text-transform: capitalize;">
    	LeetCode题目
    </span>
</div>
</div>

[toc]

## Java

### 最长特殊序列

给你两个字符串 `a` 和 `b`，请返回 *这两个字符串中 **最长的特殊序列*** 的长度。如果不存在，则返回 `-1` 。

**「最长特殊序列」** 定义如下：该序列为 **某字符串独有的最长**

**子序列**

**（即不能是其它字符串的子序列）** 。

字符串 `s` 的子序列是在从 `s` 中删除任意数量的字符后可以获得的字符串。

- 例如，`"abc"` 是 `"aebdc"` 的子序列，因为删除 `"aebdc"` 中的`ed`字符可以得到 `"abc"` 。 `"aebdc"` 的子序列还包括 `"aebdc"` 、 `"aeb"` 和 `""` (空字符串)。

**示例 1：**

```
输入: a = "aba", b = "cdc"
输出: 3
解释: 最长特殊序列可为 "aba" (或 "cdc")，两者均为自身的子序列且不是对方的子序列。
```

**示例 2：**

```
输入：a = "aaa", b = "bbb"
输出：3
解释: 最长特殊序列是 "aaa" 和 "bbb" 。
```

**示例 3：**

```
输入：a = "aaa", b = "aaa"
输出：-1
解释: 字符串 a 的每个子序列也是字符串 b 的每个子序列。同样，字符串 b 的每个子序列也是字符串 a 的子序列。
```

**提示：**

- `1 <= a.length, b.length <= 100`
- `a` 和 `b` 由小写英文字母组成

**解析**

1. 字符串的子序列的长度不会超过该字符串的长度。
2. 如果子序列的长度等于该字符串的长度，那么子序列就是该字符串
3. 字符串不相同长度也不相同时，可以选择较长的字符串当作最长特殊序列，因为它不会是较短字符串的子序列
4. 字符串不相同但是长度相同时，仍然可以选择一个字符串作为最长特殊字符串，它不会是另一个字符串的子序列
5. 字符串相同长度也相同时，那么任意一个子序列就会出现在两个字符串中，那么就是 -1

```java
class Solution {
    public int findLUSlength(String a, String b) {
        // Math.max方法：max() 方法用于返回两个参数中的最大值。
        return a.equals(b) ? -1 : Math.max(a.length(), b.length());
    }
}
```



### 最长特殊序列Ⅱ

给定字符串列表 `strs` ，返回其中 **最长的特殊序列** 的长度。如果最长特殊序列不存在，返回 `-1` 。

**特殊序列** 定义如下：该序列为某字符串 **独有的子序列（即不能是其他字符串的子序列）**。

 `s` 的 **子序列**可以通过删去字符串 `s` 中的某些字符实现。

- 例如，`"abc"` 是 `"aebdc"` 的子序列，因为您可以删除`"aebdc"`中的下划线字符来得到 `"abc"` 。`"aebdc"`的子序列还包括`"aebdc"`、 `"aeb"` 和 "" (空字符串)。

**示例 1：**

```
输入: strs = ["aba","cdc","eae"]
输出: 3
```

**示例 2:**

```
输入: strs = ["aaa","aaa","aa"]
输出: -1
```

**提示:**

- `2 <= strs.length <= 50`
- `1 <= strs[i].length <= 10`
- `strs[i]` 只包含小写英文字母

**解析**

```java
class Solution {
    public int findLUSlength(String[] strs) {
        int n = strs.length;
        int ans = -1;
        // 使用一个双重循环，外层枚举每一个字符串 str[i] 作为特殊序列，内层枚举每一个字符串 str[j]，判断 str[i] 是否不为 str[j] 的子序列即可。
        for (int i = 0; i < n; ++i) {
            boolean check = true;
            for (int j = 0; j < n; ++j) {
                if (i != j && isSubseq(strs[i], strs[j])) {
                    check = false;
                    break;
                }
            }
            if (check) {
                // 在所有满足isSubSeq方法的strs[i]中选择最长的一个作为答案，如果不满足，则返回-1
                ans = Math.max(ans, strs[i].length());
            }
        }
        return ans;
    }

    public boolean isSubseq(String s, String t) {
        // 定义两个指针
        int ptS = 0, ptT = 0;
        // 两个指针指向的位置要小于两个字符串的长度
        while (ptS < s.length() && ptT < t.length()) {
            // 两个指针对s、t两个字符串一位接一位的比对
            // 如果两个比对的字符当前位都相同则都往右移动一位
            // 如果ptT指针向右移动则表示匹配失败
            if (s.charAt(ptS) == t.charAt(ptT)) {
                ++ptS;
            }
            ++ptT;
        }
        // 判断ptS指针是否遍历了整个字符串，如果是则代表字符串s是字符串t的子序列
        return ptS == s.length();
    }
}
```





## 算法







## 数据库

### 组合两个表

表: `Person`

```
+-------------+---------+
| 列名         | 类型     |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+
personId 是该表的主键（具有唯一值的列）。
该表包含一些人的 ID 和它们的姓和名的信息。
```

表: `Address`

```
+-------------+---------+
| 列名         | 类型    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+
addressId 是该表的主键（具有唯一值的列）。
该表的每一行都包含一个 ID = PersonId 的人的城市和州的信息。
```

编写解决方案，报告 `Person` 表中每个人的姓、名、城市和州。如果 `personId` 的地址不在 `Address` 表中，则报告为 `null` 。

以 **任意顺序** 返回结果表。

**解析**

本题关键点在于“如果 `personId` 的地址不在 `Address` 表中，则显示`null`”，由此可以想到 **left join 左外连接**去查询，把person表当左表，address当右表，左表的数据全部显示，右表显示符合搜索条件的记录。

```mysql
select p.firstName,
       p.lastName,
       a.city,
       a.state
from person p left join address a on p.personId = a.personId
```



### 第二高的薪水

`Employee` 表：

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是这个表的主键。
表的每一行包含员工的工资信息。
```

查询并返回 `Employee` 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 `null(Pandas 则返回 None)` 。

**解析**

1. 首先考虑重复问题，则需要使用 `distinct` 来去除重复
2. 第二高可以使用 `limit 1 offset 1` 来实现返回第二高的数据
3. 最重要的是要考虑到如果数据只有一条的时候，就应该使用 `ifnull` 来处理查不到第二高的时候来返回null

```mysql
select ifnull(
    (select distinct salary
     from employee
     order by salary desc
     limit 1,1)
    ,null) as SecondHighestSalary
```



### 第N高的薪水

表: `Employee`

```
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
在 SQL 中，id 是该表的主键。
该表的每一行都包含有关员工工资的信息。
```

查询 `Employee` 表中第 `n` 高的工资。如果没有第 `n` 个最高工资，查询结果应该为 `null` 。

**解析**

```mysql
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
  # mysql索引从0开始，所以减一
  SET M = N - 1;
  RETURN (
    select distinct salary
     from Employee
     order by salary desc
     limit M,1
  );
END
```

