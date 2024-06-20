import traceback  
import mylog 
logger = mylog.setup_logger('dump')

def my_function():  
    # 在这里编写您的代码  
    c = 1/0
    return c
  
try:  
    my_function()  
except Exception as e:  
    # 在这里处理异常  
    traceback.print_exc()
