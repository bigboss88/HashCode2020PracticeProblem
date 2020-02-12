import sys

def rev(ls):
    return [ele for ele in reversed(ls)]
def main():
    file = sys.argv[1]
    max_slices = 0
    pizza_types = 0
    type_slices = []
    with open(file,"r") as f:
        max_slices,pizza_types = map(int,f.readline().split(" "))
        slices = f.readline().split(" ")
        if(len(slices) != pizza_types):
            print("Please enter correct slice types")
            return
        type_slices = list(filter(lambda x: x <= max_slices,map(int,slices))) # Can filter an pizza that has more slices than needed
    total = 0
    ids = []
    for t in reversed(type_slices):
        if(total + t <= max_slices and type_slices.index(t) not in ids):
            total+=t
            ids.append(type_slices.index(t))
    with open(file.split('.')[0]+'.out',"w") as f:
        f.write(str(len(ids))+'\n')
        for i in reversed(ids):
            f.write(str(i)+' ')
main()
