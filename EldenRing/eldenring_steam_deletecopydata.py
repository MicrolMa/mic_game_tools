''' 删除备份数据 '''
from config import datacopy_remember_dir,auto_datacopy_remember_dir
from common_util import del_files

# 为 API 提供的功能函数
def deletecopydata_action_forapi(filename):
    gamecopydata_dir = f'{datacopy_remember_dir}/{filename}'
    # 删除备份记录文件夹
    for i in range(2):
        del_files(gamecopydata_dir)

def deletecopydata_fromauto_action_forapi(filename):
    gamecopydata_dir = f'{auto_datacopy_remember_dir}/{filename}'
    # 删除备份记录文件夹
    for i in range(2):
        del_files(gamecopydata_dir)


