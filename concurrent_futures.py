from concurrent.futures import ThreadPoolExecutor

data = [10, 20, 30, 40, 50]

def square(number):
    return number * number

if __name__ == "__main__":
    
    with ThreadPoolExecutor(max_workers=4) as executor:
        
        result = list(executor.map(square, data))
    
        print("input data = "+str(data))
        print("output data = "+str(result))