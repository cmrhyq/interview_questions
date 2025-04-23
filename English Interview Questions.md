1. What was the biggest（challenge/diffeent）you encountered in the project? 你在项目里遇到的最大的 挑战/困难 是什么
```
In the China Mobile Payment project, some users could not see their orders. I checked this problem right away. First, I looked at system logs using the payment times users gave me, but found nothing. When I checked the database, I found the missing orders there. The problem was with writing data to Elasticsearch. Since the website searches Elasticsearch for orders, users couldn't see them.

To fix this, we did two things: First, we manually(ˈmanyə(wə)lē) added the missing(ˈmisiNG) orders on the same day to help users. Then, in our next update, I created a scheduled job using XXL-Job that regularly(ˈreɡ(yə)lərlē) checks both the database and Elasticsearch to keep them in sync(siNGk), which completely(kəmˈplētlē) solved(sälvd) the problem.

在中国移动收钱宝项目中，我们曾遇到部分用户反馈无法查询到订单的问题。针对这一"丢单"现象，我立即展开了系统化排查。首先，我根据用户提供的支付时间检索系统日志，但未发现相关记录。进一步排查后，我在数据库中成功找到了这些"丢失"的订单，最终确认问题根源在于数据写入Elasticsearch时出现异常。由于前端查询依赖Elasticsearch，这导致用户无法查看自己的订单信息。

为解决此问题，我们采取了两步走策略：首先在投产日通过手动补单方式快速恢复受影响的订单数据，保障用户体验；随后在下一迭代周期中，我实现了一个基于XXL-Job的定时任务，用于自动扫描比对数据库与Elasticsearch中的订单信息并进行同步，从根本上解决了数据不一致的问题。
```

2. What is your team（team structure/member/size）? 你们的 团队结构/成员/规模 是怎么样
```
In the China Mobile Payment Project, our company is divided（dəˈvīdəd） into two project teams in this large（lärj）project, one responsible（rəˈspänsəb(ə)l）for the mobile side and the other responsible for the web side. I am in the web side project team. My project team has 1 project portfolio(ˌpɔːtˈfəʊ.li.əʊ) manager, 1 project manager, 1 product manager, 1 architect(ˈɑː.kɪ.tekt), 8 developers, 8 testers, 2 test team leaders, and 2 operation and maintenance(ˈmānt(ə)nəns) personnel.

在中国移动支付项目中，我们公司的在这个大项目中分为两个项目组，一个负责移动端，一个负责web端，我是在web端项目组中，我的项目组共有1位项目集经理，1位项目经理，1位产品经理，1位架构师，8位开发，8位测试，2位测试组长，2位运维。
```

3. What is the testing（testing process/life circles）? 测试流程/生命周期 是怎么样的
```
The first step is to conduct a demand analysis. The second step is to make a test plan, the third step is to design test cases, and then apply for test resources, execute tests, track defects and manage them, write test reports, regression test the original functions, and finally acceptance test.

第一步是进行需求分析。第二步是做测试计划，第三步是做测试用例设计，接下来是申请测试资源、执行测试、跟踪缺陷和管理、编写测试报告、回归测试原有功能，最后是验收测试
```

4. How much do you know about the cloud? 你对 云 的了解有多少
```
I am familiar with Alibaba Cloud and Tencent Cloud, and am currently taking Amazon Cloud-related certifications.

我熟悉阿里云和腾讯云，并且正在考取亚马逊的云相关的证书
```

4. What are the technology skill you are most（familiar/good at/special in）? 你最 熟悉/擅长/最擅长 的技术技能是什么
```
I familiar automation and common testing technologies, be familiar with testing tools such as Apifox and Jmeter, be familiar in development technologies such as Java, Python, Vue, React, familiar SQL language and database knowledge, familiar Linux and Docker, and be familiar in using Git for version control.

我掌握自动化和常用测试技术，熟悉Apifox、Jmeter等测试工具，熟练掌握Java、Python、Vue，React等开发技术，掌握SQL语言和数据库知识，掌握Linux、Docker，熟练使用Git进行版本控制。
```