import sys

def main():
    # read CLI for input data
    try:
        data_path = sys.argv[1]
    except:
        print("No data path supplied!")
        return
    
    # open and read the data.
    try:
        data=open(data_path).readlines()
    except:
        print(f"Could not open path: {data_path}. Enter a valid path.")
        return
    
    try:
    # process data
        left_list = []
        right_list = []
        for line in data:
            left,right=line.strip().split(" ", 1)
            left_list.append(int(left))
            right_list.append(int(right))
            pass
        
        # do da ting
        simularity = calculate_simularity(left_list, right_list)
        return simularity
        
    except Exception as ex:
        print(ex)
        return
    pass

def calculate_simularity(primary, secondary):
    secondary.sort()
    simularity = 0
    for current in primary:
        found = False
        count = 0
        for subject in secondary:
            if subject == current:
                found = True
                count+=1
                continue
            if(found):
                break
        simularity += current*count
    return simularity
                
if __name__ == "__main__":
    result = main()  
    print(result)  