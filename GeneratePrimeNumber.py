# genrate prime Number upto 100
def generate_prime(x):
    f=[]
    for i in range(2,x+1):
        is_prime=True
        for j in range(2,int(x**0.5)+1):
            if i%j==0:
                is_prime=False
                break
        if is_prime:
            f.append(i)        
    return f

print(generate_prime(100))            