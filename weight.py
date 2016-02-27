weight = int(input())
calories = int(input())
while calories != -1:
    weight += (calories - 2500)/100
    calories = int(input())
print weight
