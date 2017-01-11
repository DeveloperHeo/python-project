from collections import OrderedDict
import random

food_list = OrderedDict()
food_list["한식"] = ["김밥천국","장충동왕족발","엄마밥상"]
food_list["중식"] = ["복성각","차우차우","베이징덕"]
food_list["일식"] = ["갓덴스시","아비꼬","아리가또"]

selected_food_type = input("{} 중 한가지를 고르시오.\n".format(",".join(food_list.keys())))

while selected_food_type not in food_list.keys():
    print("{} 중에만 고르시오.".format(",".join(food_list.keys())))
    selected_food_type = input()

print(random.choice(food_list[selected_food_type]))
