<div style="font-family: 'Kanit', sans-serif;text-align: center;border: 10px solid #fff;box-shadow: 1px 1px 2px #e6e6e6;background: linear-gradient(to left top, #11998e, #38ef7d); padding: 50px 0;">
<div style="color: #fff;">
    <h3 style="font-size: 25px;font-weight: 600;letter-spacing: 1px;text-transform: uppercase;margin: 0;">
       Database Interview Question
    </h3>
    <span style="font-size: 16px;text-transform: capitalize;">
    	数据库面试题
    </span>
</div>
</div>

[toc]



## 数据库基础

### 	数据库的三范式是什么

- 第一范式：列的原子性，即数据库表的每一列都是不可分割的原子数据项，比如用户表中的地址信息，把地址拆分成省、市这种明确的字段。

- 第二范式：实体的属性完全依赖于主关键字，且不存在对主键的部分依赖，用来消除表中冗余的列，比如订单表中的商品分类，详细信息这些，只需要由商品表存一份就够了。

- 第三范式：任何非主属性不依赖于其它非主属性，属性直接依赖于主键。具体的解释就是没有间接依赖于主键的列，意思就是对字段冗余性的约束，比如用户表中不需要存额外的所在城市的人口，城市特点的这些字段



### 左连接和右连接的区别

- 左连接（左外连接）：以左表作为基准进行查询，左表数据会全部显示出来，右表如果和左表匹配的 数据则显示相应字段的数据，如果不匹配则显示为 null。 

- 右连接（右外连接）：以右表作为基准进行查询，右表数据会全部显示出来，左表如果和右表匹配的 数据则显示相应字段的数据，如果不匹配则显示为 null。 

- 全连接：先以左表进行左外连接，再以右表进行右外连接。

- 内连接：显示表之间有连接匹配的所有行。



## SQL相关





## 调优相关

