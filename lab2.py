from collections import namedtuple
import datetime

Person = namedtuple("Person", "first_name, last_name, date_of_birth")


def person_from_line(line : str):
    entry = line.split(",")
    return Person(entry[0],entry[1], datetime.datetime.strptime(entry[2],
                        "%Y-%m-%d"))

def people_from_csv(path):
    file = open(path, 'r')
    people = []
    for line in file.readlines():
        people.append(person_from_line(line.strip()))
    return people

def solve_Josephus_(people, step, index):
    if len(people) == 1:
        return people[0]
    index=(index+step)%len(people)
    print("kill " + str(people.pop(index)))
    return solve_Josephus_(people, step, index)


def solve_Josephus(people, step):
    return solve_Josephus_(people.copy(), step, 0)


def sort_by_age(people):
    people.sort(key=lambda person:person.date_of_birth)

def merge_sort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        merge_sort(left)
        merge_sort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
                i+=1

            else:
                arr[k]=right[j]
                j+=1
            k+=1
        while i<len(left):
            arr[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1



def main():

    people = people_from_csv("lista")
    sort_by_age(people)
    for person in people:
        print(person)
    arr=[2, 7, 19, -5, -26]
    merge_sort(arr)
    print(arr)




    pass

if __name__ == "__main__":
     main()