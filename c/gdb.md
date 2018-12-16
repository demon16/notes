## gdb调试

在编译时要加上`-g`选项, 生成的目标文件才能用gdb进行调试.

### 单步执行和跟踪函数调用
```bash
gcc -g main.c -o main
gdb main
```
  - `list`/`l` 列出源代码, 接着上次的位置往下列, 每次列10行 `list 2` / `list function_name`.
  - `next`/`n` next line.
  - `step`/`s` step into.
  - `backtrace`/`bt` 查看函数调用的栈帧.
  - `info`/`i` 查看函数局部变量的值, `i locals`.
  - `frame`/`f` 选择指定的栈帧的局部变量.
  - `print`/`p` 打印出变量的值, `p sum`.
  - `finish` 让程序一直运行到从当前函数返回为止.
  - `set var` 指定一个变量的值 `set var sum=0` / `p sum=0`.

### 断点 程序访问某一代码行时中断
  - `display` 使得每次停下来的时候都系爱你时当前变量值 `display sum`.
  - `undisplay` 与`display`相反.
  - `break`/`b` 设置断点. `b 9` 在9行设置一个断点. `break`命令的参数也可以是函数名, 表示在某一个函数开头设置断点.
  - `continue`/`c` 连续运行而非单步运行, 程序到达断点回自动停下来.
  - `i breakpoints` 查看断点信息.
  - `delete breakpoints 2` 删除指定断点.
  - `disable breakpoints 3` 暂时禁用断点.
  - `enable breakpoints 3` 恢复断点.
  - `break 9 if sum != 0` 如果`sum`值不为0， 则中断.
  - `run`/`r` 重新从程序开头连续执行.

### 观察点 程序访问某一存储单元时中断
  - `x/7b input` 打印存储器中的内容. `7b`是打印格式, `b`表示每个字节一组, `7`表示打印7组.
  - `watch` 设置观察点. `watch input[5]`.

### 段错误(Segmentation fault)
  - `bt` 查看栈帧.