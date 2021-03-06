# 环境变量

## 变量
shell中创建一个变量：
```
declare variable
```
`=`跟变量赋值：
```
variable=ximolang
```
`echo`显示出来,$引用变量
```
echo $variable
```

## 环境变量
在所有的 UNIX 和类 UNIX 系统中，每个进程都有其各自的环境变量设置，且默认情况下，当一个进程被创建时，处理创建过程中明确指定的话，它将继承其父进程的绝大部分环境设置。Shell 程序也作为一个进程运行在操作系统之上，而我们在 Shell 中运行的大部分命令都将以 Shell 的子进程的方式运行。

**相关命令**
`set` 显示当前 Shell 所有变量，包括其内建环境变量（与 Shell 外观等相关），用户自定义变量及导出的环境变量

`env` 显示与当前用户相关的环境变量，还可以让命令在指定环境中运行。

`export` 显示从 Shell 中导出成环境变量的变量，也能通过它将自定义变量导出为环境变量。

/etc/bashrc（有的 Linux 没有这个文件） 和 /etc/profile ，它们分别存放的是 shell 变量和环境变量。还有要注意区别的是每个用户目录下的一个隐藏文件：.profile
这个 .profile 只对当前用户永久生效。而写在 /etc/profile 里面的是对所有用户永久生效，所以如果想要添加一个永久生效的环境变量，只需要打开 /etc/profile，在最后加上自己想添加的环境变量就好啦。

## 命令的查找路径与顺序
`echo $PATH`查看环境变量内容

## 添加环境变量
```
$ PATH=$PATH:/home/shiyanlou/mybin
```
## 删除环境变量
可以使用 unset 命令删除一个环境变量

# 文件查找

## 搜索文件
whereis 只能搜索二进制文件(-b)，man 帮助文件(-m)和源代码文件(-s)。如果想要获得更全面的搜索结果可以使用 locate 命令

通过locate查找 /usr/share/ 下所有 jpg 文件：
```
$ locate /usr/share/\*.jpg
```
如果想只统计数目可以加上 -c 参数，-i 参数可以忽略大小写进行查找，whereis 的 -b、-m、-s 同样可以使用。

which 本身是 Shell 内建的一个命令，我们通常使用 which 来确定是否安装了某个指定的软件，因为它只从 PATH 环境变量指定的路径中去搜索命令：

find 应该是这几个命令中最强大的了，它不但可以通过文件类型、文件名进行查找而且可以根据文件的属性（如文件的时间戳，文件的权限等）进行搜索.

    注意 find 命令的路径是作为第一个参数的， 基本命令格式为 find [path] [option] [action] 。

