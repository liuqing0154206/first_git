
# import os, shutil
#
# filepath0 = 'data/bat/IMG_000001.jpg'
# filepath1 = 'data/bat/IMG_000000.jpg'
#
# # 修改文件名
# os.system('mv {} {}'.format(filepath0, filepath1))
# # os.rename(filepath0, filepath1)
#
#
# # 创建文件夹
# dirname = 'data_samples'
# os.system('mkdir -p {}'.format(dirname))
# # if not os.path.exists(dirname):
# #    os.mkdir(dirname)
#
# # 拷贝文件
# os.system('cp {} {}'.format(filepath1, dirname))
# shutil.copy(filepath1, dirname)
# import os#文件处理
#
# # 定义文件夹名称和标签的对应关系
# label_map = {
#     'cat': 0,
#     'dog': 1,
#     'bat': 2
# }
#
# with open('data.txt', 'w') as f:
#     # 遍历所有文件，root为当前文件夹，dirs是所有子文件夹名，files是所有文件名
#     for root, dirs, files in os.walk('data'):
#         for filename in files:
#             filepath = os.sep.join([root, filename])  # 获得文件完整路径
#             dirname = root.split(os.sep)[-1]  # 获取当前文件夹名称
#             label = label_map[dirname]  # 得到标签
#             line = '{},{}\n'.format(filepath, label)
#             f.write(line)
#进程并发
# from multiprocessing import Process  , freeze_support
#
#
# def process_data(filelist):
#     for filepath in filelist:
#         print('Processing {} ...'.format(filepath))
#         # 处理数据
#         ...
#
#
# if __name__ == '__main__':
#     # 如果是在Windows下，还需要加上freeze_support()
#     freeze_support()
#
#     # full_list包含了要处理的全部文件列表
#     ...
#     full_list=[1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#     n_total = len(full_list)  # 一个远大于32的数
#     n_processes = 32
#
#     # 每段子列表的平均长度
#     length = float(n_total) / float(n_processes)
#
#     # 计算下标，尽可能均匀地划分输入文件列表
#     indices = [int(round((i + 1) * length)) for i in range(-1, n_processes)]
#
#     # 生成每个进程要处理的子文件列表
#     sublists = [full_list[indices[i]:indices[i + 1]] for i in range(n_processes)]
#
#     # 生成进程
#     processes = [Process(target=process_data, args=(x,)) for x in sublists]
#
#     # 并行处理
#     for p in processes:
#         p.start()
#
#     for p in processes:
#         p.join()