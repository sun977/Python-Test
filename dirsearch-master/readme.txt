 目录搜索

=========


当前版本：v0.3.8（2017.07.25）



概述

———

DirSearch是一个简单的命令行工具，用于强制执行网站中的目录和文件。



安装和使用

—————


```

Git克隆https://github.com/maurosoria/dirsearch.git

CD目录搜索

python3 dirsearch.py-u<url>-e<extension>

```


也可以使用此别名直接发送到代理

` python3/path/to/dirsearch/dirsearch.py--http proxy=localhost:8080`



选项

———---



```

选项：

-h，帮助显示此帮助消息并退出


强制性的：

-u url，--url=url url目标

-l urlList，--url list=urlList

URL列表目标

-E延伸，--延伸=延伸

用逗号分隔的扩展列表（例如：php、asp）


词典设置：

-W字列表，--WordList=WordList

-L，--小写

-F，--力扩展

强制扩展每个wordlist条目（如

德布斯特）


常规设置：

-S延迟，--延迟=延迟

请求之间的延迟（浮点数）

-r，--递归bruteforce

--抑制空，--抑制空

--扫描细分曲面=扫描细分曲面，--扫描细分曲面=扫描细分曲面

扫描给定-u--url的子目录（分隔

以逗号表示）

--exclude subdir=excludesubirs，--exclude subdirs=excludesubirs

在递归过程中排除以下子目录

扫描（用逗号分隔）

--排除文本“未找到”，“错误”

按响应文本排除结果

--排除regexps='not foun[a-z]{1}'，'^error$'

根据响应中的文本regexp排除结果

-T螺纹孔，--螺纹=螺纹孔

线程数

-x excludeStatuscodes，--excludeStatus=excludeStatuscodes

排除状态代码，用逗号分隔（例如：301，

500英镑）

-C cookie，--cookie=cookie

--ua=用户代理，--用户代理=用户代理

-F，--遵循重定向

-H头，--头=头

要添加的标题（示例：--header“referer:

example.com--header“用户代理：ie”

--随机代理，--随机用户代理


连接设置：

--timeout=超时连接超时

--IP=IP解析名称到IP地址

--proxy=httpproxy，--http proxy=httpproxy

http代理（示例：localhost:8080

--max retries=最大重试次数

-B，--按主机名请求

默认情况下，DirSearch将通过IP请求速度。

这将按主机名强制请求


报告：

--简单报告=SimpleOutputFile

只找到路径

--纯文本报告=纯文本输出文件

找到状态代码为的路径

--json report=jsonOutputFile


```



支持的操作系统

———————————————————————————-

-Windows XP/7/8/10版

-GNU/Linux系统

-马科斯


特征

———

-多线程

-保持连接

-支持多个扩展（-e--extensions asp，php）

-报告（纯文本，json）

-启发式检测无效网页

-递归强制

-HTTP代理支持

-用户代理随机化

-批处理

-请求延迟


关于单词列表

———————————————————---

词典必须是文本文件。每一行都将按原样进行处理，除了使用特殊单词%ext%外，它将为作为参数传递的每个扩展名（-e--extension）生成一个条目。


例子：

-示例/

-示例%ext%


传递扩展名“asp”和“aspx”将生成以下词典：

-示例/

-示例.asp

-示例.aspx


还可以使用-f--force extensions开关将扩展附加到单词列表中的每个单词（如dirbuster）。


许可证

———---

版权所有（c）mauro soria（maurosoria at gmail dot com）


许可证：GNU通用公共许可证，第2版



