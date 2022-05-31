def run():
    def maxim(nums):
        maximun = None
        for value in nums:
            if maximun is None or value > maximun:
                maximun = value
        return maximun
        
    def minim(nums):
        minimus = None
        for value in nums:
            if minimus is None or value < minimus:
                minimus = value
        return minimus
    
    nums = []
    
    while True:

        num = input('Write a number: ')
        try:
            numb = int(num)
            numb = nums.append(numb)
            
        except:
            if num == "exit":
                break
            print("Write a valid number")
    
    maximun = maxim(nums)
    minimus = minim(nums)
    print('The higher number is:', maximun, 'and the lower number is:',
          
          minimus)        

if __name__ == "__main__":
    run()


