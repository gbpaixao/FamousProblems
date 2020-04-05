def sieveOfEratosthenes (n):
  
  # Create a list with n+1 (from 0 to n) elements 
  array = [True] * (n+1)
  # Define 0 and 1 as not prime
  array[0] = array[1] = False
  
  # For each element of array
  for i in range(2,n+1): 
    
    if array[i]: # If it is prime
      # For each element of array starting at i^2 and finishing at n+1, with i as intervals
      for j in range(i**2, n+1, i):
        if j % i == 0:
          array[j] = False
  
  return array