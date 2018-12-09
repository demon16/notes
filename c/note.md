> gcc是linux平台的C编译器, 编译后再当前目录下生成可执行文件a.out, 直接在命令行输入这个可执行文件的路径就可以执行它.

gcc 参数
  - -E  Preprocess only; do not compile, assemble or link.
  - -S  Compile only; do not assemble or link.
  - -c  Compile and assemble, but do not link.
  - -o \<file\> Place the output into \<file\>.
  - -Wall 提示所有警告信息.
  - -lm 告诉编译器, 我们的程序中要用到的一些函数需要到`/lib/libm.so`库中找.

> 局部变量可以用任意类型相符的表达式来初始化, 而全局变量只能用常量表达式初始化. 全局变量的初始之要求保存在编译生成的目标代码中, 所以必须在编译时就能计算出来.

> 如果全局变量在定义时不初始化, 则初始值是0, 也就是说, 整型的就是0, 字符型的就是'\0', 浮点型的就是0.0.

> 如果局部变量在定义时不初始化, 则初始值是不确定(每次调用这个函数时局部变量的初值可能不一样, 运行环境不同, 函数的调用次序不同, 都会影响到局部变量的初值.)的.

> `switch`分支的`case`后面跟的必须是常量表达式, 因为这个值必须在编译时计算出来. `case`后面跟的常量表达式的值必须是可以精确比较的整型或字符型.
