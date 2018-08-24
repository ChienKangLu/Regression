# Regression
Regression is used to find a model for continuous variables. The model can be used to handle prediction, controling and causal link task. Before doing regression, we need to determine which regression function is good for the sample data e.g. linear, polynomial or parabolic.

## Skill
+ Variable transformation: use linear regression to solve non-linear model
+ Find regression parameter

## Example
<img width="400" src="https://github.com/ChienKangLu/Regression/blob/master/regression/img1.png" />

## Practice
In ML Lecture 1, I follow the tutorial and practice to use gradient descent to solve linear regression.
+ Without using the linear regression closed form
+ If using the pure gradient descent, it will take too much time to find the optimal parameter. Therefore, we need to give different learning rates to b and w, and update them in each iteration. The cool method is called **Adagrad**.
+ **Adagrad**: I remeber my professor tell us that it can **normalize** the gradient at each iteration by **gradient sd**

<Table>
   <tr>
      <td><img width="400" src="https://github.com/ChienKangLu/Regression/blob/master/ML_Lecture/gradient.png" /></td>
      <td><img width="400" src="https://github.com/ChienKangLu/Regression/blob/master/ML_Lecture/gradient%20with%20adagrad.png" /></td>
   </tr>
   <tr>
      <td align="center">Pure gradient descent</td>
      <td align="center">Gradient descent with Adagrad</td>
   </tr>
</Table>

## Regression closed form for multiple dimensional vector
<p> We have <i>m</i> data tuples which contain vector <i><b>x</b></i> and scalar <i>y</i>,</p>
<p align="center">
<img src="https://latex.codecogs.com/svg.latex?data%20%3D%20%5C%7B%28%5Ctextbf%7B%5Ctextit%7Bx%7D%7D_%5Ctextbf%7B%5Ctextit%7Bi%7D%7D%2Cy_i%29%5C%7D%2Ci%3D1%5Ccdots%20m" />
</p>

<p><i><b>x</b></i> is a n-dimensional vector,</p>
<p align="center">
<img src="http://latex.codecogs.com/svg.latex?%5Ctextbf%7B%5Ctextit%7Bx%7D%7D_%5Ctextbf%7B%5Ctextit%7Bi%7D%7D%3D%5Cbegin%7Bbmatrix%7Dx_i_1%20%5C%5Cx_i_2%5C%5C%5Cvdots%5C%5C%20x_i_n%5Cend%7Bbmatrix%7D_%7Bn*1%7D" />
</p>

<p>Now, Assume <i>y</i> has linear relationship with <i><b>x</b></i>,</p>
<p align="center">
<img src="http://latex.codecogs.com/svg.latex?y_i=\alpha&plus;\beta&space;_1x_i_1&plus;\beta&space;_2x_i_2&plus;\cdots&plus;\beta_nx_i_n" />
</p>

<p>For simplifying the notation, we combine <i>&alpha;</i> and all <i>&beta;</i> into a vector <i><b>&beta;</b></i>, all <i>y</i> into vector <i><b>y</b></i>. We create a maxtrix <i><b>X</b></i> whose row vector ia vector <i><b>x</b></i> and added 1 at first column.</p>

<p align="center">
<img src="http://latex.codecogs.com/svg.latex?%24%5Cmathit%20%7B%5Cboldmath%20%24%5Cbeta%24%7D%20%24%3D%5Cbegin%7Bbmatrix%7D%5Calpha%5C%5C%5Cbeta_1%5C%5C%5Cbeta_2%5C%5C%5Cvdots%5C%5C%5Cbeta_n%5Cend%7Bbmatrix%7D_%7B%28n&plus;1%29*1%7D" />
<img src="https://latex.codecogs.com/svg.latex?%5Ctextbf%7B%5Ctextit%7By%7D%7D%20%3D%20%5Cbegin%7Bbmatrix%7Dy_1%5C%5Cy_2%5C%5Cy_3%5C%5C%5Cvdots%5C%5Cy_m%5Cend%7Bbmatrix%7D_%7Bm&plus;1%7D" />
<img src="https://latex.codecogs.com/svg.latex?%5Ctextbf%7B%5Ctextit%7BX%7D%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%201%26%20x_i_1%20%26%20x_i_1%20%26%20%5Ccdots%20%26%20x_i_n%20%5C%5C%20%26%20%26%20%5Cvdots%20%26%20%26%5C%5C%201%26%20x_m_1%20%26%20x_m_1%20%26%20%5Ccdots%20%26%20x_m_n%20%5Cend%7Bbmatrix%7D_%7Bm*%28n&plus;1%29%7D" />
</p>

<p>We assume the linear regression model is</p>
<p align="center">
<img src="https://latex.codecogs.com/svg.latex?%5Ctextbf%7B%5Ctextit%7By%7D%7D%20%3D%20%5Ctextbf%7B%5Ctextit%7BX%7D%7D%20%24%5Cmathit%7B%5Cboldmath%20%24%5Cbeta%24%7D%24%20&plus;%20%5Ctextbf%7B%5Ctextit%7Berror%7D%7D" />
</p>

<p>To minimize error, the loss function is</p>
<p align="center">
<img src="https://latex.codecogs.com/svg.latex?L%28%24%5Cmathit%7B%5Cboldmath%20%24%5Cbeta%24%7D%24%29%3D%28%5Ctextbf%7B%5Ctextit%7By%7D%7D-%5Ctextbf%7B%5Ctextit%7BX%7D%7D%20%24%5Cmathit%7B%5Cboldmath%20%24%5Cbeta%24%7D%24%29%5E%7B%27%7D%28%5Ctextbf%7B%5Ctextit%7By%7D%7D-%5Ctextbf%7B%5Ctextit%7BX%7D%7D%20%24%5Cmathit%7B%5Cboldmath%20%24%5Cbeta%24%7D%24%29" />
</p>


## Reference
+ [ML Lecture 1: Regression - Demo] (https://www.youtube.com/watch?v=1UqCjFQiiy0)
+ [Hung-yi Lee ML Course] (http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML17_2.html)

