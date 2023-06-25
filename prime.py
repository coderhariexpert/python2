def prime(n): 
    if n <= 0: 
        return "Not defined" 
    elif n == 1: 
        return "Not prime" 
    for i in range(2, n): 
        if n%i == 0: 
            return "not prime" 
    return "prime" 
 
 
 
def list_prime(lst): 
	prime_list =[ ] 
	for i in lst: 
		x = prime(i) 
		if x == "prime": 
			prime_list.append(i) 
	return prime_list 
	 
lst=[]
n=int(input("Enter No Of Elements: "))
for i in range(0,n):
    ele=int(input("Enter Element: "))
    lst.append(ele)
print(list_prime(lst))
