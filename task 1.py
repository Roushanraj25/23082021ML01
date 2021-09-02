Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 5**9
1953125
>>> 3//2
1
>>> 7/3
2.3333333333333335
>>> 6==6
True
>>> a=20;a+=30;a%=3;
>>> print(a)
2
>>> True*False
0
>>> True&False
False
>>> True and False
False
>>> ((6>3)and(7<4)or(18==3))and (9>3)
False
>>> True is False
False
>>> False is 'False'
False
>>> ((True==False)or(False>True))and(False<=True)
False
>>> s1="Nice to have it"
>>> s2="here"
>>> s2=" here"
>>> print(s1 + s2)
Nice to have it here
>>> a=[1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
>>> a[3][1][2]
['hello']
>>> a.insert(0,s1)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7]
>>> a.insert(23,s2)
>>> print(a)
['Nice to have it', 1, 2, [3, 4], [5, [100, 200, ['hello']], 23, 11], 1, 7, ' here']
>>> c0l0r_list_1=(["White","Black","Red"])
>>> >>> c0l0r_list_1=set(["White","Black","Red"])
SyntaxError: invalid syntax
>>> color_list_1=set(["White","Black","Red"])
>>> colour_list_2=set(["Red","Green"])
>>> colour_list_1.difference(colour_list_2)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    colour_list_1.difference(colour_list_2)
NameError: name 'colour_list_1' is not defined
>>> 
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> >>> colour_list_1=set(["White","Black","Red"])
SyntaxError: invalid syntax
>>> color_list_1=(["White","Black","Red"])
>>> color_list_1=set(["White","Black","Red"])
>>> color_list_2=set(["Red","Green"])
>>> color_list_1.difference(color_list_2)
{'White', 'Black'}
>>> n=5
>>> nn=((n*10)+n)
>>> nnn=((n*100)+(n*10)+n)
>>> print(n+nn+nnn)
615
>>> phrase=input("input word:")
input word:without,hello,bag,world
>>> phrase_list=phrase.split(",")
>>> phrase_list.sort()
>>> print((',').join(phrase_list))
bag,hello,without,world
>>> 