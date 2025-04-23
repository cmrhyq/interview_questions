1. What was the biggest（challenge/diffeent）you encountered in the project? 你在项目里遇到的最大的 挑战/困难 是什么
```
In the China Mobile Payment project, some users could not see their orders. I checked this problem right away. First, I looked at system logs using the payment times users gave me, but found nothing. When I checked the database, I found the missing orders there. The problem was with writing data to Elasticsearch. Since the website searches Elasticsearch for orders, users couldn't see them.

To fix this, we did two things: First, we manually added the missing orders on the same day to help users. Then, in our next update, I created a scheduled job using XXL-Job that regularly checks both the database and Elasticsearch to keep them in sync, which completely solved the problem.

在中国移动收钱宝项目中，我们曾遇到部分用户反馈无法查询到订单的问题。针对这一"丢单"现象，我立即展开了系统化排查。首先，我根据用户提供的支付时间检索系统日志，但未发现相关记录。进一步排查后，我在数据库中成功找到了这些"丢失"的订单，最终确认问题根源在于数据写入Elasticsearch时出现异常。由于前端查询依赖Elasticsearch，这导致用户无法查看自己的订单信息。

为解决此问题，我们采取了两步走策略：首先在投产日通过手动补单方式快速恢复受影响的订单数据，保障用户体验；随后在下一迭代周期中，我实现了一个基于XXL-Job的定时任务，用于自动扫描比对数据库与Elasticsearch中的订单信息并进行同步，从根本上解决了数据不一致的问题。
```

2. What is your team（team structure/member/size）? 你们的 团队结构/成员/规模 是怎么样
```

```

3. What is the testing（testing process/life circles）? 测试流程/生命周期 是怎么样的
```

```

4. How much do you know about the cloud? 你对 云 的了解有多少
```
I am familiar with Alibaba Cloud and Tencent Cloud, and am currently taking Amazon Cloud-related certifications.

我熟悉阿里云和腾讯云，并且正在考取亚马逊的云相关的证书
```

4. What are the technology skill you are most（familiar/good at/special in）? 你最 熟悉/擅长/最擅长 的技术技能是什么
```
I familiar automation and common testing techniques, be familiar with testing tools such as Apifox and Jmeter, be familiar in development technologies such as Java, Python, Vue, React, familiar SQL language and database knowledge, familiar Linux and Docker, and be familiar in using Git for version control.

我掌握自动化和常用测试技术，熟悉Apifox、Jmeter等测试工具，熟练掌握Java、Python、Vue，React等开发技术，掌握SQL语言和数据库知识，掌握Linux、Docker，熟练使用Git进行版本控制。
```