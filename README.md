# create label from data


```
glabels-3 &
```

edit merge properties

![](2019-07-07-12-09-15.png)


get text from file, cancel

![](2019-07-07-12-10-40.png)


```
echo "Hello" > data_1.txt
echo "World" > data_2.txt
```


![](2019-07-07-12-13-15.png)

Print > Print Preview

label from file 1

![](2019-07-07-12-16-12.png)

![](2019-07-07-12-15-04.png)


label from file 2

![](2019-07-07-12-16-31.png)

![](2019-07-07-12-17-05.png)

```
echo -e 'day;month;year\r\n01;Jan;1970' > data.txt
```




create glabel file

```
${day} - ${month} - ${year}
```

![](2019-07-07-12-28-59.png)glab

![](2019-07-07-12-30-17.png)

![](2019-07-07-12-31-21.png)


extract data from command line

set location to None, save, close

![](2019-07-07-12-36-35.png)

```
echo -e 'day;month;year\r\n31;Dec;3000' > data.txt
glabels-3-batch -i data.txt -o date_label.pdf label.glabels
atril date_label.pdf

```
