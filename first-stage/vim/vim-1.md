# vim快速入门
+ Vim中的六种基本模式
+ Vim中的基本操作

## vim模式介绍
vim有六种基本模式和五种派生模式

1. 普通模式
在普通模式中，用的编辑器命令，比如移动光标，删除文本等等。这也是Vim启动后的默认模式。这正好和许多新用户期待的操作方式相反（大多数编辑器默认模式为插入模式）。
在普通模式中，有很多方法可以进入插入模式。比较普通的方式是按a（append／追加）键或者i（insert／插入）键。

2. 插入模式
在这个模式中，大多数按键都会向文本缓冲中插入文本。大多数新用户希望文本编辑器编辑过程中一直保持这个模式。这个模式下按ESC可以回到普通模式。

3. 可视模式
这个模式与普通模式比较相似。但是移动命令会扩大高亮的文本区域。高亮区域可以是字符、行或者是一块文本。当执行一个非移动命令时，命令会被执行到这块高亮的区域上。Vim的"文本对象"也能和移动命令一样用在这个模式中。

4. 选择模式
这个模式和无模式编辑器的行为比较相似（Windows标准文本控件的方式）。这个模式中，可以用鼠标或者光标键高亮选择文本，不过输入任何字符的话，Vim会用这个字符替换选择的高亮文本块，并且自动进入插入模式。

5. 命令行模式
在命令行模式中可以输入会被解释成并执行的文本。例如执行命令（:键），搜索（/和?键）或者过滤命令（!键）。在命令执行之后，Vim返回到命令行模式之前的模式，通常是普通模式。

6.Ex模式
这和命令行模式比较相似，在使用:visual命令离开Ex模式前，可以一次执行多条命令。**这其中我们常用到就是普通模式、插入模式和命令行模式，本课程也只涉及这三个常用模式的内容**

## 三种常用模式的切换
vim启动进入普通模式，处于插入模式或命令行模式时只需要按Esc或者Ctrl+[(这在vim课程环境中不管用)即可进入普通模式。普通模式中按i（插入）或a（附加）键都可以进入插入模式，普通模式中按:进入命令行模式。命令行模式中输入wq回车后保存并退出vim。

1. 进入vim
```
vim filename
```
2. 游标移动
在进入vim后，按下i键进入插入模式，按Esc进入普通模式，在该模式下使用方向键或者h,j,k,l键可以移动游标。
3. 进入插入模式
i在当前光标处进行编辑
I在行首插入
A在行末插入
a在光标后插入编辑
o在当前行后插入一个新行
O在当前行前插入一个新行
cw替换从光标所在位置后到一个单词结尾的字符

4. 命令模式下保存文档
从普通模式输入:进入命令行模式，输入w回车，保存文档。输入:w 文件名可以将文档另存为其他文件名或存到其它路径下

5. 退出vim
从普通模式输入:进入命令行模式，输入wq回车，保存并退出编辑
普通模式下输入Shift+zz即可保存退出vim
