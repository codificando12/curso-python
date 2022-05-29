def run():
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
        
        
    print(sum(nums), len(nums), float(sum(nums) / len(nums)))
    
    
if __name__ == "__main__":
    run()