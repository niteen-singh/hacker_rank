You are given a function f(X) = X^2. You are also given K lists. The ith list consists of
N(i) elements.

You have to pick one element from each list so that the value from the equation below is maximized:

S=(f(X1) + F(X2) +... + F(Xk))%M

Xi denotes the element picked from the  list ith. Find the maximized value Smax obtained.

% denotes the modulo operator.

Note that you need to take exactly one element from each list, not necessarily the largest element. You add the squares of the chosen elements and perform the modulo operation. The maximum value that you can obtain, will be the answer to the problem.

Input Format

The first line contains 2 space separated integers k and m.
The next k lines each contains an integer Ni, denoting the number of elements in the ith list, followed by Ni space separated integers denoting the elements in the list.

Constraints

1 <= K <= 7
1 <= M <= 1000 
1 <= Ni <= 7 
1 <= Magnitude of elements in list <= 10^9 

Output Format

Output a single integer denoting the value Smax.

Sample Input

3 1000
2 5 4
3 7 8 9 
5 5 7 8 9 10 

Sample Output

206

Explanation

Picking 5 from the 1st list, 9 from the 2nd list and 10 from the 3rd list gives the maximum
S value equal to (5^2 + 9^2 + 10^2)%1000 = 206.