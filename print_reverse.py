def print_reverse(ptyhon):
    print(ptyhon[::-1])

print_reverse("python")

def print_score(score_list):
    print(sum(score_list) / len(score_list))

print_score([1, 2, 3])

def print_even(one_list):
    for i in one_list:
        if i % 2 == 0:
            print(i)

print_even([1, 3, 2, 10, 12, 11, 15])

def print_keys(one_dict):
    for i in one_dict:
        print(i)
print_keys({"이름":"김말똥", "나이":30, "성별":0})

def print_value_by_key(my_dict, day):
    print(my_dict[day])

my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
print_value_by_key(my_dict, "10/26")

def print_5xn(string):
    chunk_num = int(len(string)/5)
    for x in range(chunk_num+1):
        print(string[x*5 : x*5+5])
print_5xn("아임어보이유어럴골")


def printmxn(string, num):
    for x in range(num+1):
        print(string[x * num :x * num + num ])

printmxn("아이엠어보이유알어걸걸거럭러", 3)

def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay
calc_monthly_salary(1201)