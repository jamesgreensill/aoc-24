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
        
        # sort data
        left_list.sort()
        right_list.sort()
        
        # calculate distance
        distance = 0
        for left, right in zip(left_list, right_list):
            distance += (max(left, right) - (min(left,right)))    
        return distance     
    except Exception as ex:
        print(f"Malformed Data: {ex}.")  
        return
    pass

# entry point      
if __name__ == "__main__":
    distance = main()
    print(distance)