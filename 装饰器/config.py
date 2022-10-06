import logging

# 第一步，创建一个logger
logger = logging.getLogger()# 定义对应的程序模块名name，默认是root
logger.setLevel(logging.INFO)  # 指定最低的日志级别 critical > error > warning > info > debug

# 第二步，创建一个handler，用于写入日志文件
#logfile = './log2.txt'
#fh = logging.FileHandler(logfile, mode='a',encoding="utf-8")
#fh.setLevel(logging.DEBUG)  # 用于写到file的等级开关

# 第三步，再创建一个handler,用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.WARNING)    # 输出到console的log等级的开关

# 第四步，定义handler的输出格式
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
#fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 第五步，将logger添加到handler里面
#logger.addHandler(fh)
logger.addHandler(ch)