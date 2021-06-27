# Least Square Monte Carlo for American Option
   
[![Followers](https://img.shields.io/github/followers/AlbertLin0327?style=social)](https://github.com/AlbertLin0327)
[![Stars](https://img.shields.io/github/stars/AlbertLin0327?style=social)](https://github.com/AlbertLin0327)
![Issue](https://img.shields.io/github/issues/AlbertLin0327/Least-Square-Monte-Carlo)
![Commit](https://img.shields.io/github/last-commit/AlbertLin0327/Least-Square-Monte-Carlo)
   
## Program Description   
This program is to stimulate the price of an American option with given market informations (interest rate, volatility rate, ...). It uses Least Square Monte Carlo to estimate the price. Also,extra informations such as delta and RMSER is calculated. More features will be added in the near future. For futher discription and explanation, please refer to this [document](https://www.csie.ntu.edu.tw/~b08902127/Least_Square_Monte_Carlo.pdf).

## Basic Information  
- Author: Albert Lin    
- School: National Taiwna University    
- Version: Python3   
- Library: random math Numpy matplotlib   
    
## Usage    
#### Prerequisites
- Python 3.6 or up  
- git  
  
#### Installation  
1. Cloning the repository  
```
git clone https://github.com/AlbertLin0327/Least-Square-Monte-Carlo.git
cd Least-Square-Monte-Carlo
```
  
2. Install Python dependencies  
```
pip3 install dependency
```
or  
```
python3 -m pip install -r dependency
```
  
#### Execution   

```

Enter the type of American Option, Put or Call
>>> Put
Enter: spot price, strike price, time interval, interest(%), dividend(%), volatility(%), period, stimulations
>>> 100 110 2.5 0.05 0.01 0.02 500 100000

-----------------------------
Price of Put: 97.65491215553891
Stdandard deviation: 0.00979123231158338
Root Mean Sqaure Error Rate: 0.03170613184836371
-----------------------------

Enter the dS (porportion) to shift the Random Path to estimate delta. Better to have 0 < dS <= 0.1
>>> 0.08

-----------------------------
Price of p after 0.08 shift: 93.09784165073779
Stdandard deviation after 0.08 shift: 0.00933432405179502
Root Mean Sqaure Error Rate after 0.08 shift: 0.0317061318483637
Estimated Delta of p: -0.5696338131001397
-----------------------------

```
  
## Result
#### Distribution of the Monte Carlo sampled path  
<img src="/images/Distribution.png" height="500">   
  
#### Random Seleceted Monte Carlo sampled path  
<img src="/images/Path.png" height="500">  
  
## Additional Information  
Explanation: https://www.csie.ntu.edu.tw/~b08902127/Least_Square_Monte_Carlo.pdf  


## Links to Me!
[![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:linhsinkai@gmail.com)
[![Medium](https://img.shields.io/badge/Medium-12100E?style=for-the-badge&logo=medium&logoColor=white)](https://medium.com/@linhsinkai)
[![Facebook](https://img.shields.io/badge/Facebook-1877F2?style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/hsinkai.lin.327)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/albert-hk-lin)