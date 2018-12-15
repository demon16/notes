## Linux内核编码风格

### 空格
  - 关键字`if`, `while`, `for`与其后面的控制表达式的`(`括号之间插入一个空格分隔, 但括号内的表达式应紧贴括号. 例如`while (1);`.
  - 双目运算符的两侧插入一个空格分隔, 单目运算符和操作数之间不加空格, 例如`i = i + 1`, `++i`, `!(i < 1)`, `-x`, `&a[1]`等.
  - 后缀运算符和操作数之间也不加空格, 例如取结构体成员`s.a`, 调用`foo(arg1)`, 取数组成员`a[i]`.
  - `,`号和`;`号之后要加空格, 这是英文的书写习惯, 例如`for (i = 1; i < 10; i ++)`, `foo(arg1, arg2)`.
  - 以上关于双目运算符和后缀运算符的规则不是严格要求, 有时候为了突出优先级也可以写得更紧凑一些, 例如`for (i=1; i<10; i++)`, `distance = sqrt(x*x + y*y)`等. 但是省略的空格一定不要误导了读代码的人, 例如`a||b && c`很容易让人理解成错误的优先级.
  - 由于标准的Linux终端是24行80列, 接近或大于80个字符的较长语句要折行写, 折行后用空格和上面的表达式或参数对齐, 例如
```c
if (sqrt(x*x + y*y)) > 5.0
	&& x < 0.0
	&& y > 0.0)

for (sqrt(x*x + y*y),
	a[i-1] + b[i-1] + c[i-1])
```
  - 较长的字符串可以断成多个字符串然后分行写, 例如
```c
printf("This is such a long sentence that "
	"it cannot be held within a line\n");
```
### 缩进
  - 要用缩进体现出句块的层次关系, 使用Tab字符缩进, 不能用空格代替Tab. 在标准Linux终端上, 一个Tab看起来是8个空格的宽度, 有些编辑器可以设置一下Tab看起来是几个空格的宽度, 建议设成8, 这样大的缩进使代码看起来非常清晰.规定不能用空格代替Tab主要是不希望空格和Tab混在一起做缩进, 如果混在一起用了, 在某些编辑器里面Tab的宽度改了就会看起来非常混乱.
  - `if/else`, `while`, `do/while`, `for`, `switch`这些带语句的语块, 语句块`{`和`}`应该和关键字写在一起, 用空格隔开, 而不是单独占一行. 例如应该这样写:
```c
if (...) {
	语句列表
} else if (...) {
	语句列表
}
```
  - 函数定义的`{`和`}`单独占一行, 这一点和语句块的规定不同, 例如
```c
int foo(int a, int b)
{
	语句列表
}
```
  - `switch`和语句块里的`case`, `default`对齐写, 也就是说语句块里的`case`, `default`相对于`switch`不往里缩进. 例如
```c
switch (C) {
case 'A':
	语句列表
case 'B':
	语句列表
default:
	语句列表
}
```
  - 自己命名的标号(用于`goto`)必须顶头写不缩进, 而不管标号下的语句缩进到第几层.
  - 代码中每个逻辑段落之间应该用一个空行分割开. 例如每个函数定义之间应该插入一个空行, 头文件, 全局变量定义和函数定义之间定义也应该插入空行, 例如:
```c
#include <stdio.h>
#include <stdlib.h>

int g;
double h;

int foo(void)
{
	语句列表
}

int bar(int a)
{
	语句列表
}

int main(void)
{
	语句列表
}
```
  - 一个函数的语句列表如果很长, 也可以根据相关性分成若干组, 用空行分隔, 这条规定不是严格要求, 一般变量定义语句组成一组, 后面要加空行, `return`之前要加空行, 例如:
```c
int main(void)
{
	int a, b;
	double c;
	
	语句组1

	语句组2

	return 0;
	
}
```
### 注释
  - 单行注释应采用`/* comment */的形式, 用空格把界定符和文字分开. 多行注释最常见的是这种形式
```c
/*
* Multi-line
* comment
*/
```
  - 整个源文件的顶部注释. 说明此模块的相关信息, 例如文件名, 作者和版本历史等, 顶头不缩进. 例如内核源代码*kernel/sched.c*的开头:
```c
/*
* kernel/sched.c
*
* Kernel scheduler and related syscalls
*
* Copyright (C) 1991-2002 Linus Torvalds
*
* 1996-12-23 Modified by Dave Grothe to fix bugs in semaphores and
* make semaphores SMP safe
* 1998-11-19 Implemented schedule_timeout() and related stuff
* by Andrea Arcangeli
* 2002-01-04 New ultra-scalable O(1) scheduler by Ingo Molnar:
* hybrid priority-list and round-robin design with
* an array-switch method of distributing timeslices
* and per-CPU runqueues. Cleanups and useful suggestions
* by Davide Libenzi, preemptible kernel bits by Robert Love.
* 2003-09-03 Interactivity tuning by Con Kolivas.
* 2004-04-02 Scheduler domains code by Nick Piggin
*/
```
  - 函数注释. 说明此函数的功能, 参数, 返回值, 错误码等, 写在函数定义上侧, 和此函数定义之间不留空行, 顶头写不缩进.
  - 相对独立的语句组注释. 对这一组语句作特别说明, 写在语句组上侧, 和此语句组之间不留空行, 与当前语句组的缩进一致. 注意, 说明语句组的注释一定要写在语句组上面, 不能写在语句组下面.
  - 代码行右侧的简短注释. 对当前代码行做特别说明, 一般为单行注释, 和代码之间至少用一个空格隔开, 一个源文件中所有的右侧注释最好能上下对齐.
  - 内核源代码*lib/radix-tree.c`中的一个函数包含了上述三种注释:
```c
/**
 * radix_tree_insert - insert into a radix tree
 * @root: radix tree root
 * @index: index key
 * @item: item to insert
 *
 * Insert an item into the radix tree at position @index.
 */
int radix_tree_insert(struct radix_tree_root *root, 
			unsigned long index, void *item) {
	struct radix_tree_node *node = NULL, *slot;
   	unsigned int height, shift;
   	int offset;
   	int error;
   	/* Make sure the tree is high enough. */
   	if ((!index && !root->rnode) ||
   			index > radix_tree_maxindex(root->height)) {
		error = radix_tree_extend(root, index);
		if (error)
		return error;
   	}
	slot = root->rnode;
	height = root->height;
	shift = (height-1) * RADIX_TREE_MAP_SHIFT;
	offset = 0; /* uninitialised var warning */
   	do {
		if (slot == NULL) {
			/* Have to add a child node. */
			if (!(slot = radix_tree_node_alloc(root)))
			return -ENOMEM;
		if (node) {
			node->slots[offset] = slot;
			node->count++;
		} else
			root->rnode = slot;
		}
		/* Go a level down */
		offset = (index >> shift) & RADIX_TREE_MAP_MASK;
		node = slot;
		slot = node->slots[offset];
		shift -= RADIX_TREE_MAP_SHIFT;
		height--;
	} while (height > 0);
	if (slot != NULL)
		return -EEXIST;
	BUG_ON(!node);
	node->count++;
	node->slots[offset] = item;
	BUG_ON(tag_get(node, 0, offset));
	BUG_ON(tag_get(node, 1, offset));

	return 0;
}
```
  - 复杂的结构提定义比函数更需要注释. 例如内核源代码*kernel/sched.c*中定义了这样一个结构体:
```c
/*
 * This is the main, per-CPU runqueue data structure.
 *
 * Locking rule: those places that want to lock multiple runqueues
 * (such as the load balancing or the thread migration code), lock
 * acquire operations must be ordered by ascending &runqueue.
 */
struct runqueue {
	spinlock_t lock;
	/*
 	 * nr_running and cpu_load should be in the same cacheline because
 	 * remote CPUs use both these fields when doing load calculation.
	 */
 	unsigned long nr_running;
	#ifdef CONFIG_SMP
 		unsigned long cpu_load[3];
	#endif
 	unsigned long long nr_switches;

 	/*
	 * This is part of a global counter where only the total sum
	 * over all CPUs matters. A task can increase this counter on
	 * one CPU and if it got migrated afterwards it may decrease
	 * it on another CPU. Always updated under the runqueue lock:
	 */
	unsigned long nr_uninterruptible;

	unsigned long expired_timestamp;
	unsigned long long timestamp_last_tick;
	task_t *curr, *idle;
	struct mm_struct *prev_mm;
	prio_array_t *active, *expired, arrays[2];
	int best_expired_prio;
	atomic_t nr_iowait;

#ifdef CONFIG_SMP
	struct sched_domain *sd;
	/* For active balancing */
	int active_balance;
	int push_cpu;
	task_t *migration_thread;
	struct list_head migration_queue;
	int cpu;
#endif

#ifdef CONFIG_SCHEDSTATS
	/* latency stats */
	struct sched_info rq_sched_info;
	
	/* sys sched yield() stats */
	unsigned long yld_exp_empty;
	unsigned long yld_act_empty;
	unsigned long yld_both_empty;
	unsigned long yld_cnt;
	
	/* schedule() stats */
	unsigned long sched_switch;
	unsigned long sched_cnt;
	unsigned long sched_goidle;
	
	/* try_to_wake_up() stats */
	unsigned long ttwu_cnt;
	unsigned long ttwu_local;
#endif
};
```
  - 复杂的宏定义和变量定义也需要注释. 例如内核源代码*include/linux/jiffies.h*中的定义:
```c
/* TICK_USEC_TO_NSEC is the time between ticks in nsec assuming real ACTHZ and */
/* a value TUSEC for TICK_USEC (can be set bij adjtimex) */
#define TICK_USEC_TO_NSEC(TUSEC) (SH_DIV (TUSEC * USER_HZ * 1000, ACTHZ, 8))

/* some arch's have a small-data section that can be accessed register-relative
 * but that can only take up to, say, 4-byte variables. jiffies being part of
 * an 8-byte variable may not be correctly accessed unless we force the issue
 */
#define __jiffy_data __attribute__((section(".data")))

/*
 * The 64-bit value is not volatile - you MUST NOT read it
 * without sampling the sequence number in xtime_lock.
 * get_jiffies_64() will do this for you as appropriate.
 */
extern u64 __jiffy_data jiffies_64;
extern unsigned long volatile __jiffy_data jiffies;
```

### 标识符命名
  - 短的单词可以通过取元音形成缩写, 较长的单词可以取单词的头几个字母形成缩写, 如`count`写成`cnt`, `block`写成`blk`, `length`写成`len`, `windows`写成`win`, `message`写成`msg`, `temporary`写成`temp`/`tmp`.
  - 内核风格规定变量, 函数和类型采用全小写加下划线的方式命名, 常量(宏定义和枚举常量)采用全大写加下划线的方式命名.