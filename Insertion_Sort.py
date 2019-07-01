#------Insertion Sort--------------------------------- ----#
#-- Enter your input as comma separated numbers          --#
#-- Browse through the unsorted array , then take one    --#
#-- element from start and find its position in the      --#
#-- array, insert it where it belongs, do it till u      --#
#-- reach end of the array                               --#
#----------------------------------------------------------#

def insertion_sort(arr):
    arr_len=len(arr)
    for i in range(arr_len):
        for j in range(1,arr_len):
            if i == 0:
                if arr[j] < arr[i]:
                    arr[j],arr[i]=arr[i],arr[j]
            else:
                if arr[i] >= arr[j-1] and arr[i] <= arr[j]:
                    arr[i],arr[j]=arr[j],arr[i]
    print('Insertion Sort array')
    print(arr,end=' ')


def main():
    try:
        arr=list(map(int,input().split(',')))
    except:
        print('Enter Valid input')
    insertion_sort(arr)


if __name__ == "__main__":
    main()