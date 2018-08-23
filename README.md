# Regression
Regression is used to find a model for continuous variables. The model can be used to handle prediction, controling and causal link task. Before doing regression, we need to determine which regression function is good for the sample data e.g. linear, polynomial or parabolic.

## Skill
+ Variable transformation: use linear regression to solve non-linear model
+ Find regression parameter

## Example
<img width="400" src="https://github.com/ChienKangLu/Regression/blob/master/regression/img1.png" />

## Practice
In ML Lecture 1, I follow the tutorial and practice to use gradient descent to solve linear regression.
+ Not using the linear regression closed form
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

## Reference
+ [ML Lecture 1: Regression - Demo] (https://www.youtube.com/watch?v=1UqCjFQiiy0)
+ [Hung-yi Lee ML Course] (http://speech.ee.ntu.edu.tw/~tlkagk/courses_ML17_2.html)

