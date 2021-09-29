import concurrent.futures
import time

list = []
f0 = 0 #seed fibonacci3
f1 = 1 #seed fibonacci
list.extend([f0,f1])
def find_fibonacci(x: int) -> bool:
    """
    Menemukan bilangan bulat x di dalam suatu deret fibonacci.
    Apabila x ada di dalam suatu deret fibonacci, maka kembalikan True.
    Jika tidak ada, maka kembalikan False
    """
    # write your code here
    
    for idx, value in enumerate(list):
        if (list[len(list)-1] < x):
            fibo = list[len(list)-1] + list[len(list)-2]
            list.append(fibo)
      
    if (x in list):
        print("{} - True".format(x))
        print("End Function")
        return True
        
    else:
        print("{} - False".format(x))
        print("End Function")
        return False
    
    

#Synchronous
if __name__ == "__main__":
    """Jalankan beberapa test-case di bawah sini
    """
    start = time.perf_counter()
    for i in range(1,101):
        find_fibonacci(i) 

    finish = time.perf_counter()
    executed_time = round(finish - start, 2)
    print(f"Finished in {executed_time} second(s)")
