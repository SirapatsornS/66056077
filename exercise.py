def calculateSum(list_data):
    if list_data .__len__()==0:
        return 0
    else:
        total=0
        for i in list_data:
            total = total + i

        return total
def caculateProduct(list_data):
    if list_data.__len__()==0:
        return 0
    else:
        total=1
        for i in list_data:
            total = total*i

        return total


def caculateAverage(list_data):
    if list_data.__len__() == 0:
        return 0
    else :
        list_count = list_data.__len__()
        sum_total = 0
        for i in list_data:
            sum_total = sum_total + i

        cal_avg = sum_total/list_count
        return cal_avg


if __name__ == '__main__':
    print(calculateSum([])==0)
    print(calculateSum([2,4,6,8,10])==30)
    print(caculateProduct([])==0)
    print(caculateProduct([2,4,6,8,10])==3840)
    print(caculateAverage([1,2,3])==2)
    print(caculateAverage([1,2,3,1,2,3,1,2,3])==2)
    print(caculateAverage([12,20,37])==23)
    print(caculateAverage([0,0,0,0,0])==0)