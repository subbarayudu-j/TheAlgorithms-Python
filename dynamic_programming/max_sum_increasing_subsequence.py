# Python solution for Maximum Sum 
# Increasing Subsequence problem 
# using Dynamic Programming

def maxSumIncreasingSubsqence(a, n): 
	maxSum = 0
	dp = [0 for x in range(n)] 

	for i in range(n): 
		dp[i] = a[i] 

	for i in range(1, n): 
		for j in range(i): 
			if(a[i] > a[j] and dp[i] < dp[j] + a[i]): 
				dp[i] = dp[j] + a[i] 

	for i in range(n): 
		if maxSum < dp[i]: 
			maxSum = dp[i] 

	return maxSum


a = [7, 5, 2, 10, 9 ,8, 9] 
n = len(a) 
print("Sum of maximum sum increasing subsequence is " + str(maxSumIncreasingSubsqence(a, n))) 