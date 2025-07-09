# 哈希表（散列表

要想突破基于关键字比较查找的时间性能下界，就不能仅依赖于基于比较来进行查找
*Q: 能否不用比较，通过关键字的取值直接确定存储位置？*
在关键字值和存储位置之间建立一个确定的对应关系

*Q: 哈希（散列）技术仅仅是一种查找技术吗？*
哈希既是一种查找技术，也是一种存储技术。

*Q: 哈希是一种完整的存储结构吗？
哈希只是通过记录的关键字的值定位该记录，没有表达记录之间的逻辑关系，所以哈希主要是面向查找的存储结构。

Q: 哈希技术适用于何种场合？* 
通常用于实际出现的关键字的数目远小于关键字所有可能取值的数量。 

*Q: 哈希技术适合于哪种类型的查找?*
不适用于允许多个记录有同样关键字值的情况。
也不适用于范围查找，如在哈希表中，找最大或最小关键值的记录，也不可能找到在某一范围内的记录。



#### 哈希函数的构造方法：

- 若是非数字关键字，则需先对其进行数字化处理

1.直接定址法（仅适合于：地址集合的大小==关键字集合的大小）

    取关键字或关键字的某个线性函数值为哈希地址

2.数字分析法（仅适合于：能预先估计出全体关键字的每一位上各种数字出现的频度）

    假设关键字集合中的每个关键字都是由 s 位数字组成 (u1, u2, …, us)，分析关键字集合的全体， 并从中提取分布均匀的若干位或它们的组合作为地址。

3.平方取中法（适合于：关键字中的每一位都有某些数字重复出现频度很高的现象）

    以关键字的平方值的中间几位作为存储地址。求“关键字的平方值” 的目的是“扩大差别” ，同时平方值的中间各位又能受到整个关键字中各位的影响。

4.折叠法（关键字的数字位数特别多）

    将关键字分割成位数相同的几段，最后一段可以不同。段的长度取决于散列表的地址位数，然后将各段的叠加和（舍去进位）作为散列地址

![07b344ea-fc01-4496-8b25-1a9dc008ad83](file:///D:/Users/asus/Pictures/Typedown/07b344ea-fc01-4496-8b25-1a9dc008ad83.png)

5.除留余数法(质数除余法)

设桶数B，取质数 m ≤ B，Hash ( key ) = key %  m 

最常用最简单的构造哈希函数的方法。
散列表中的每个存储单元可以称为桶。
一般情况下对m的选取很重要。如果选的不好，容易产生同义词，可以选m为质数或者不包含小于20的质因数的合数。

6.除随机数法（通常，此方法用于对长度不等的关键字构造哈希函数)

设定哈希函数为: H(key) = Random(key)
(其中，Random 为伪随机函数



- 构造Hash函数应注意以下几个问题：
  计算Hash函数所需时间
  关键字的长度
  散列表的大小
  关键字的分布情况
  记录的查找频率
  
  

### 处理冲突（为产生冲突的地址寻找下一个哈希地址）

1.开放定址法

<img src="file:///D:/Users/asus/Pictures/Typedown/0e76756d-0b8f-4f63-810a-b9eb82d9c4a1.png" title="" alt="0e76756d-0b8f-4f63-810a-b9eb82d9c4a1" style="zoom:50%;">

```c
int hashsize[]={997,...};//哈希表容量递增表，一个适合的素数序列
typedef struct{
    ElemType *elem;//数据元素存储基址，动态分配数组
    int count;//当前数据元素个数
    int sizeindex;//hashsize[sizeindex]为当前容量
}HashTable;
#define SUCCESS 1
#define UNSUCCESS 0
#define DUPLICATE -1

Status SearchHash(HashTable H, KeyType K, int &p, int &c){
    p = Hash(K);// 求得哈希地址
    while(H.elem[p].key != NULLKEY && !EQ(K, H.elem[p].key))//该地址含有记录且关键字不等 
        collision(p, ++c);// 求得下一探查地址 p
    if(EQ(K, H.elem[p].key)) return SUCCESS;                 
     //查找成功，返回待查数据元素位置 p
    else return UNSUCCESS;// 查找不成功
} // SearchHash

```

冲突时，按步长探测，找到空槽放入关键字



2.链地址法

<img src="file:///D:/Users/asus/Pictures/Typedown/3856cccf-ad80-434f-86d0-bf2df4dbb8ad.png" title="" alt="3856cccf-ad80-434f-86d0-bf2df4dbb8ad" style="zoom:50%;">



<img src="file:///D:/Users/asus/Pictures/Typedown/9dd0ef2a-75ff-430b-9e35-c6a5e3f206ea.png" title="" alt="9dd0ef2a-75ff-430b-9e35-c6a5e3f206ea" style="zoom:50%;">
