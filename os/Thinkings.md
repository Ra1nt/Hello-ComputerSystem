<!--
 * @Author: rain l0802_69@qq.com
 * @Date: 2025-09-15 11:16:30
 * @LastEditors: rain l0802_69@qq.com
 * @LastEditTime: 2025-09-15 11:26:08
 * @FilePath: /Hello-ComputerSystem/os/Thinkings.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
## Lab1
使用简单的 for 获取第一个没有结束的进程
在了解了整个系统是如何运行的之后，这里是编写 Lab1，引入 os, process 类，运行 test，test 中调用 os, process中的类，使用编写的lab方式，最后验证输出，从编写 lab1 下手，发现没有思路，于是回到测试代码和 process, myos 类。阅读源码之后发现在 os 中已经执行了一些部分，例如系统的退出 exit(); 在 lab1 中就不需要再次使用 exit();
于是 lab1 的编写变得简单，只需要找到第一次未完成的进程即可

## Lab2
在 Lab1 的基础上添加优先级，实现比较简单，找到最高级，然后赋值即可。

## Lab3 Lab4
模仿提供的代码，编写对应的 run 函数

## Lab5
---

## Summary
了解系统的运行之后，rtfsc, 形式变得明朗。