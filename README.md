# iOS-Interview-for-Toplogis

面試題目分為兩部分: 第一部分是簡答題，會以考iOS的基本觀念的方式來進行。每一題請在三句話以內回答。第二部分是coding題，會請你用我們為這次面試寫的迷你API來做一個小Project。

There are two parts of interview. The first part is short answer. You will be tested on basic concepts in iOS development. Answer under three sentences for each question. The second part is coding challenge. You will be asked to finish a small project using the API we provide. Good luck!

## 簡答題
1. 什麼是AutoLayout? 為什麼要用AutoLayout？
2. 你有連過API的經驗嗎？你用什麼工具/Library? 例: NSURLRequest, NSURLSession, AFNetworking
3. 舉出三種在iOS上儲存資料的方法
4. 簡述Singleton pattern與使用的時機
5. 簡述Key Value Observing和使用的時機
6. 舉出兩種multi-threading的方法

## Short Answer
1. What's AutoLayout? Why AutoLayout?
2. Do you have experience with API? What framework do you use to connect? Ex: NSURLRequest, NSURLSession, AFNetworking
3. Write down three ways to persistently store data in iOS
4. What's Singleton pattern? When to use it?
5. What's Key Value Observing? When to use it?
6. Write down two ways to do multi-threading

## Coding 挑戰
### Setup 
打開Terminal並navigate到API資料夾裡，輸入`./run.py`
來開啟API server. 你可以在http://127.0.0.1:5000 做API的Request

### API範例
在對http://127.0.0.1:5000 POST以下Parameters
Parameters:
```
{
  startNum = 0,
  endNum = 3
}
```
我們會有下列Response:
```
{
    result =     (
                {
            item = 0;
            left = 38218;
            middle = 93355;
            right = 60552;
        },
                {
            item = 1;
            left = 27153;
            middle = 92004;
            right = 254;
        },
                {
            item = 2;
            left = 95128;
            middle = 99026;
            right = 55553;
        },
                {
            item = 3;
            left = 32785;
            middle = 7183;
            right = 31975;
        }
    );
}
```
### API Example
After you post following parameters to http://127.0.0.1:5000
```
{
  startNum = 0,
  endNum = 3
}
```
you will see response similar to the following
```
{
    result =     (
                {
            item = 0;
            left = 38218;
            middle = 93355;
            right = 60552;
        },
                {
            item = 1;
            left = 27153;
            middle = 92004;
            right = 254;
        },
                {
            item = 2;
            left = 95128;
            middle = 99026;
            right = 55553;
        },
                {
            item = 3;
            left = 32785;
            middle = 7183;
            right = 31975;
        }
    );
}
```

### 挑戰
你的目標是做出一個UITableView，其中第nth個UITableViewCell裡包含API第n個item的資料。左上角寫著"Left: 待填"，中間是"Middle: 待填"，右下是"Right: 待填"。你的UITableView要能做到無限滑動

完成後應如下圖所示:

![Result](/Result.gif)

### Challenge
Your goal is to create a UITableView in which the nth UITableViewCell contains the data of nth item in API. At the upper left corner of cell, you should display "Left: data from API". At the center, you should display "Middle: data from API". At the bottom right corner, you should display "Right: data from API". Your UITableView should be able to infinitely scrolling.

After you finish, you should see following:

![Result](/Result.gif)




