from module2 import *
from module3 import *
from module4 import *
from module5 import *
from user_auth import *

from datetime import datetime

now = datetime.now()   
print(f"{now}:  hello")

print_module2()
print_module3()
print_module4()
print_module5()
user_auth("user1", "87n9m9n96b^BJ")
