# AppDesign
Application design homework for me.

## 它是什么
这是我在大三时的“软件设计”实习周的一份作业，一共七道题目，两个星期内完成。应该说时间还是非常宽裕的，题目本身也并不是很难。至于为什么想要开源，主要是想着，将这段时间的经历分享出来，毕竟是自己用心做的，也可以给他人作为一个参考吧。

**注意：本项目已上交作业，不得抄袭！！如需引用，需显著注明该仓库地址及作者。项目遵循[Mozilla Public License 2.0](https://github.com/Pragmatism0220/AppDesign/blob/master/LICENSE)协议开源，请认真阅读遵守。**

### 环境依赖
* Python 3.7.2环境开发
* Windows 10操作系统

之所以选用Python开发，一方面是因为我对Python比较熟悉，另一方面是因为Python开发的高效。我需要在有限的时间内完成优秀的软件，那么繁茂的Python社区决定了Python一定是我的第一选择。

对于其他版本的Python我并没有做测试；所有的图形化界面均采用[PyQt5](https://pypi.org/project/PyQt5/)开发。为了保证代码的一致性，代码风格均采用[PEP8](https://www.python.org/dev/peps/pep-0008/)标准（除了base64的图片编码部分）。

此外，对于我所引用的其他第三方开源类库，我表示衷心的感谢。非常感谢你们伟大的工作！！非常感谢！！

## 如何使用
### 方法一、使用release版
在项目的[release](https://github.com/Pragmatism0220/AppDesign/releases)界面下载最新的release版本，然后直接双击运行即可。

### 方法二、源码运行
首先利用git克隆该项目到本地：
```shell
git clone https://github.com/Pragmatism0220/AppDesign.git
```
克隆之后，所对应的每个文件夹都是一个项目；先进入你想运行的项目，之后在确保已经安装Python3的情况下，安装相应的依赖，使用命令：
```shell
pip install -r requirements.txt
```
如果你的默认Python版本不是3的话，你应该使用`pip3`代替`pip`。

然后使用命令：
```shell
python app.py
```
同样地，如果你的默认Python版本不是3的话，你应该使用`python3`代替`python`。

具体的使用方法我在每个子项目的**自述文件**里有详细说明，请查看。

之后，尽情享受吧！

## 一些细节
基本上每个项目都分为两个文件：`app.py`和`UI.py`，个别的项目会有`images.py`，这表示那里面嵌入了一些图片信息。

`app.py`是主控脚本，负责调用`UI.py`，本身不涉及任何实现；`UI.py`是前端和后端的集成，由类和类方法实现。对于更详细的踩坑过程，可以访问[我的博客](https://pragmatism0220.cf/)~~（随缘更新）~~。~~由于一些特殊的原因国内访问可能会比较慢。~~

哦对了，由于我将图标文件以字节的形式硬编码到了源代码中，因此源代码中的个别行可能会非常长。在Pycharm中进行开发时，Pycharm会强制进行换行：
```
This document contains very long lines. Soft wraps were forcibly enabled to improve editor performance.
```
~~对没错，这是个feature。~~

附上解决方法：

在Pycharm上方工具栏中点击`Help`，然后点击`Edit Custom Properties...`，打开（没有则创建）`idea.properties`文件，强行修改自动换行的阈值。在文件中键入：
```
editor.soft.wrap.force.limit=500000
```
也就是指定一个较大的数字。保存后，重启Pycharm即可。请注意，编辑器可能会因此变得很慢。默认限制值为10000。

## 已知问题
暂时未发现新的问题。欢迎提issue。

## 作者
一个学生，一个宅男。

* **联系方式**
  * 博客： https://pragmatism0220.cf/
  * 电子邮件: pragmatism0220@gmail.com
  * 微博: [@保護者_Pragmatism0220](https://weibo.com/u/7341561133)
  * 推特: [@Pragmatism_0220](https://twitter.com/Pragmatism_0220)

## 开源许可证
[Mozilla Public License 2.0](https://github.com/Pragmatism0220/AppDesign/blob/master/LICENSE)
