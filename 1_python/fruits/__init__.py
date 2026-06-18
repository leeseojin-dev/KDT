from .apple import info as apple_info, func1
from .banana import info as banana_info

__all__ = ["apple_info", "banana_info", "func1"]

# 같은 함수명을 사용할 때 apple 파일의 info 메서드를 apple._info로 사용하도록 
# from fruits import * 
# 위의 코드를 사용했을 때 원래 다 가져와야하는데 __all__을 설정하면 해당 함수나 클래스만 사용 가능