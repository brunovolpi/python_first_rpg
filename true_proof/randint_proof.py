from random import randint

randint_counter = 0
list_0_25 = []
list_25_50 = []
list_50_75 = []
list_75_100 = []
while randint_counter <= 100:
    randint_obj = randint(0, 100)
    if randint_obj <= 25:
        list_0_25.append(randint_counter)
        pass
    elif randint_obj <= 50:
        list_25_50.append(randint_counter)
        pass
    elif randint_obj <= 75:
        list_50_75.append(randint_counter)
        pass
    else:
        list_75_100.append(randint_counter)
        pass
    randint_counter += 1

print(f'25%-: {list_0_25}'
      f'\n50%-: {list_25_50}'
      f'\n75%-: {list_50_75}'
      f'\n100%-: {list_75_100}')