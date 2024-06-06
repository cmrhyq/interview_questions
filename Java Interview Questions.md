<div style="font-family: 'Kanit', sans-serif;text-align: center;border: 10px solid #fff;box-shadow: 1px 1px 2px #e6e6e6;background: linear-gradient(to left top, #11998e, #38ef7d); padding: 50px 0;">
<div style="color: #fff;">
    <h3 style="font-size: 25px;font-weight: 600;letter-spacing: 1px;text-transform: uppercase;margin: 0;">
       Java Interview Question
    </h3>
    <span style="font-size: 16px;text-transform: capitalize;">
    	Java面试题
    </span>
</div>
</div>

[toc]

## 一、Java基础

### java中的基本数据类型

​		byte、short、int、long、float、double、char、boolean



### 	面向对象的三个基本特征

- **继承**：继承是从已有类得到继承信息创建新类的过程。例如子类继承父类，
- 封装：通常认为封装是把数据和操作数据的方法绑定起来，对数据的访问只能通过已定义的接口。例如常说的把这段方法封装一下

- **多态性**：多态性是指允许不同子类型的对象对同一消息作出不同的响应。**实现多态，就有覆盖、重载两种方法**。
  - **覆盖**它是覆盖了一个方法并且对方法重写，以求达到不同的作用，例如最熟悉的覆盖就是对接口方法的实现
  - **重载**是指允许存在多个同名函数，但是函数的参数不同，



### 	float f=3.4;是否正确

​		不正确。3.4是双精度数，需要强制类型转换float f =(float)3.4,或者写成float f =3.4F。



### 原始类型和包装类型

- 原始类型：boolean, char, byte, short, int, long, float, double

- 包装类型：Boolean, Character, Byte, Short, Integer, Long, Float, Double



### 	&和&&的区别

- 当&运算符两边的表达式的结果都为true时，整个运算结果才为true。
- &&运算符第一个表达式为false时，则结果为false，不再计算第二个表达式。

- &还可以用作位运算符，当&操作符两边的表达式不是boolean类型时，&表示按位与操作



### 	数组有没有length()方法？String有没有length()方法

​		数组没有length()方法，有length 的属性。String 有length()方法



### String、StringBuffer和StringBuilder之间的区别

​		String长度不可变，StringBuffer和StringBuilder都是长度可变的。
​		StringBuilder的效率要比StringBuffer高。但是String的效率是最低的



### 	构造器（constructor）是否可被重写（override）

​		构造器不能被继承，因此不能被重写，但可以被重载



### 	抽象类（abstract class）和接口（interface）有什么异同

- 实现：抽象类的子类使用 extends 来继承；接口必须使用 implements 来实现接口。

- 构造函数：抽象类可以有构造函数；接口不能有。

- main 方法：抽象类可以有 main 方法，并且我们能运行它；接口不能有 main 方法。

- 实现数量：类可以实现很多个接口；但是只能继承一个抽象类。

- 访问修饰符：接口中的方法默认使用 public 修饰；抽象类中的方法可以是任意访问修饰符。 



### 作用域public, private, protected以及不写时的区别

不能用protected和和private修饰类

| 作用域           | 当前类 | 同一package | 子孙类 | 其他package |
| ---------------- | ------ | ----------- | ------ | ----------- |
| public           | √      | √           | √      | √           |
| protected        | √      | √           | √      |             |
| 不写（friendly） | √      | √           |        |             |
| private          | √      |             |        |             |



### 	常见的异常类有哪些？

- NullPointerException 空指针异常

- ClassNotFoundException 指定类不存在

- NumberFormatException 字符串转换为数字异常

- IndexOutOfBoundsException 数组下标越界异常

- ClassCastException 数据类型转换异常

- FileNotFoundException 文件未找到异常

- NoSuchMethodException 方法不存在异常

- IOException IO 异常

- SocketException Socket 异常



### HashMap和Hashtable的区别

- HashMap允许空（null）键值（key），HashMap允许将null作为一个entry的key或者value，而Hashtable不允许
- 由于非线程安全，HashMap效率上可能高于Hashtable。
- Hashtable的方法是Synchronize的，而HashMap不是，在多个线程访问Hashtable时，不需要自己为它的方法实现同步，而HashMap 就必须为之提供外同步。 



### 排序都有哪几种方法？请列举

- 插入排序（直接插入排序、希尔排序）
- 交换排序（冒泡排序、快速排序）
- 选择排序（直接选择排序、堆排序）



## 二、Java框架





## 三、线程相关

### 	创建线程有哪几种方式

​		继承Thread类创建线程类

​		通过Runnable接口创建线程类

​		通过Callable和Future创建线程 

### 	线程有哪些状态？

​		线程通常都有五种状态，创建、就绪、运行、阻塞和死亡。



## 四、JVM相关

### 描述一下JVM加载class文件的原理机制?

JVM中类的装载是由 ClassLoader 和它的子类来实现的, Java ClassLoader 是一个重要的Java运行时系统组件。它负责在运行时查找和装入类文件的类。



## 五、中间件相关

### 什么是缓存

缓存是一种临时存储数据的技术，目的是为了提高数据访问速度和系统性能。在软件开发中，缓存通常用于存储频繁访问的数据副本，以便将来能够更快地获取这些数据而不必每次都从原始数据源中获取。缓存可以存在于各种形式，包括内存、硬盘、数据库等。

**答**：在Java开发中，缓存通常通过使用缓存库或者框架来实现，比如常用的Redis。将经常使用的数据存储在内存中，程序可以减少对数据库或其他外部数据源的频繁访问，从而提高系统的性能和响应速度。



### 为什么需要缓存

缓存的存在有几个重要的原因：

1. **提高性能**：缓存能够存储频繁访问的数据，减少了从数据库或其他数据源获取数据的次数。由于内存访问速度通常比硬盘或网络访问速度更快，因此通过缓存可以大大提高数据访问的速度，提升应用程序的性能。

2. **降低系统负载**：频繁的数据库或其他外部数据源访问会增加系统的负载，尤其是在高并发环境下。通过使用缓存，可以减轻数据源的压力，降低系统负载，提高系统的可伸缩性和稳定性。

3. **减少网络延迟**：如果数据存储在远程服务器上，每次访问都需要经过网络传输，会导致较高的延迟。通过使用缓存，在应用程序本地存储数据副本，可以减少网络传输的次数，从而降低访问数据的延迟。

4. **提高数据可用性**：缓存可以在某些情况下提高数据的可用性。例如，如果数据库发生故障或者网络连接中断，应用程序仍然可以从缓存中获取数据，确保系统的正常运行。

5. **降低成本**：通过减少对数据库或其他外部数据源的频繁访问，可以降低系统的运行成本，尤其是在云计算环境下，减少数据传输和存储的成本。
