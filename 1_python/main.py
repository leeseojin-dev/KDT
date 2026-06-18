# main.py

import fruit        # fruit 파일에 있는 것을 가져다가 사용이 가능
# main.py 파일을 실행 했을 때 👉 if __name__ == "__main__": 블록은 실행되지 않음
# from fruits import apple_info, banana_info, func1
# from fruits.apple import func1      # 패키지(fruits 폴더) 안의 모듈인 apple
from fruits import *

fruit.print_fruit("사과")

result = fruit.add_quantity(10, 5)
print(result)
# print(fruit.add_quantity(10, 5))

apple = fruit.Fruit("사과", 10)
apple.print_info()

print("=" * 30)
print(apple_info())
print(banana_info())
print(func1())