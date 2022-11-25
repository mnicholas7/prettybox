# prettybox
Generate random snowflakes of ascii boxes around your shell output

## Here's a couple common use cases when working at the shell prompt:

![alt text](/Image_16.jpg)
```
 => ./prettybox.py << EOF
>
> Welcome to the home of pretty box!
>
> Your TUI's and CLI's look like they
>
> need a little bit of excitement!
>
> EOF

۷۷۷۷۷۷۷۷۷۷۷۷۷    ۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷     ۷۷۷۷۷۷۷۷۷۷۷۷۷
۷
                                                           ۷
۷    ∧∧∧∧∧∧∧∧∧∧        ∧∧∧∧∧∧∧∧∧∧        ∧∧∧∧∧∧∧∧∧∧        ∧ ۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧۲           ۲۲۲۲۲۲           ۲۲۲۲۲۲           ۲۲۲۲۲۲  ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲                                                     ∧۷
۷    ∧۲    řřřřřřřřřř  řřřřřřřřřřřřřřřřřřřř  řřřřřřřřřř    ۲∧۷
۷    ∧۲    Welcome to the home of pretty box!              ۲∧۷
۷    ∧۲    Your TUI's and CLI's look like they             ۲∧۷
۷    ∧۲    need a little bit of excitement!                ۲∧۷
۷    ∧۲    řřřřřřřřřř  řřřřřřřřřřřřřřřřřřřř  řřřřřřřřřř    ۲∧۷
۷    ∧۲۲۲۲۲۲           ۲۲۲۲۲۲           ۲۲۲۲۲۲           ۲  ∧۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧                                                       ۷
۷    ∧        ∧∧∧∧∧∧∧∧∧∧        ∧∧∧∧∧∧∧∧∧∧        ∧∧∧∧∧∧∧∧∧∧ ۷
۷۷۷۷۷۷۷۷۷۷۷۷۷    ۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷۷     ۷۷۷۷۷۷۷۷۷۷۷۷۷


 =>
```


![alt text](/Image_14.jpg)
![alt text](/Image_15.jpg)


```
 => echo $SHELL | ./prettybox.py

ŒŒŒ  ŒŒ  ŒŒŒŒ


/bin/bash
ŒŒŒŒ  ŒŒ  ŒŒŒ
```

```
 => echo $SHELL | ./prettybox.py

  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ
Ⅴ
                       Ⅴ
Ⅴ     □ □ □ □ □ □ □ □ □  Ⅴ
Ⅴ     □                  Ⅴ
Ⅴ     □                  Ⅴ
Ⅴ     □    /bin/bash□    Ⅴ
Ⅴ     □ □ □ □ □ □ □ □ □  Ⅴ
Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ  Ⅴ
```



![alt text](/Image_13.jpg)
```

 => cat > newfile.txt

Also easy to pass a file as an arg!

^C

 => ./prettybox.py newfile.txt

⅕⅕⅕⅕⅕⅕⅕⅕    ⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕     ⅕⅕⅕⅕⅕⅕⅕⅕
⅕  Also easy to pass a file as an arg!  ⅕
⅕
                                      ⅕
⅕⅕⅕⅕⅕⅕⅕⅕    ⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕⅕     ⅕⅕⅕⅕⅕⅕⅕⅕


 =>
 ```
 
 ## Here's how we usually call the function from inside a python script:

![alt text](/Image_12.jpg)
 ```
 Python 3.8.1 (v3.8.1:1b293b6006, Dec 18 2019, 14:08:53)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
>>> import prettybox
>>>
>>>
>>> MSG = f"""
...
... Some multi line string
...
... more text here
... """
>>>
>>> prettybox.NEW(MSG,9)

ﬀ          ﬀﬀﬀ          ﬀﬀﬀ          ﬀﬀﬀ
 ※     ※※※※※※※     ※※※※※※※     ※※※※※※※
 ξ  ξξξξξξξξξ  ξξξξξξξξξ  ξξξξξξξξξ
 ξ
 ξ
 ξ
 ξ
 ξâââââââââââââââââââââââââ       ξ
 ξâ  Some multi line string  â    ξ
 ξâ  more text here          â    ξ
 ξâ                               ξ
 ξâ                               ξ
 ξâââââââââââââââââââââââââ       ξ
 ξ
 ξ
 ξ
 ξ
 ξξξξξξξξξ  ξξξξξξξξξ  ξξξξξξξξξ  ξ
 ※※※※※※※     ※※※※※※※     ※※※※※※※     ※


ﬀﬀﬀ          ﬀﬀﬀ          ﬀﬀﬀ          ﬀ

>>>
 ```
 ![alt text](/Image_10.jpg)
 
 ### The NEW() function takes two mandatory arguments and one optional 'quiet' mode: 
 - The string 
 - an integer from 1-9 that controls the probability of chaos, with 1 being the most basic and 9 being the most dramatic.
 - **optional** A boolean for 'quiet' mode, where nothing is printed only the formatted string is returned
   
  


![alt text](/Image_11.jpg)

```
>>> BOXED_STRING = prettybox.NEW(MSG,1,1)  # quiet mode
>>>
>>> print(BOXED_STRING)

řř       řř       řř       ř
ř
                         ř
řSome multi line string    ř
řmore text here            ř
ř       řř       řř       řř

>>>

```
![alt text](/Image_9.jpg)
