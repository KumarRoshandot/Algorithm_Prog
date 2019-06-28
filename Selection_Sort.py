#------Selecttion Sort-------------------------------------#
#-- Enter your input as comma separated numbers          --#
#-- Split into 2 arr, one with default sorted  and one   --#
#-- list will be unsorted array which again u split      --#
#-- till u reach a point where the 1st sorted arr will   --#
#-- contain all the elements in sorted and               --#
#-- other list will be empty                             --#
#----------------------------------------------------------#

def selection_sort(arr):
    arr_len = len(arr)
    
    for i in range(arr_len):
        min_val = i
        
        for j in range(i+1,arr_len):
            if arr[j] < arr[min_val]:
                min_val = j
        
        arr[min_val],arr[i]=arr[i],arr[min_val]
    
    print('Selection Sort Array')
    print(arr,end=' ')


def main():
    try:
        arr = list(map(int,input().split(',')))
    except:
        print('Enter Valid Numbers')
    selection_sort(arr)
    

if __name__ == "__main__":
    main()