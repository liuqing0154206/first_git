
# import os, shutil
#
# filepath0 = 'data/bat/IMG_000001.jpg'
# filepath1 = 'data/bat/IMG_000000.jpg'
#
# # �޸��ļ���
# os.system('mv {} {}'.format(filepath0, filepath1))
# # os.rename(filepath0, filepath1)
#
#
# # �����ļ���
# dirname = 'data_samples'
# os.system('mkdir -p {}'.format(dirname))
# # if not os.path.exists(dirname):
# #    os.mkdir(dirname)
#
# # �����ļ�
# os.system('cp {} {}'.format(filepath1, dirname))
# shutil.copy(filepath1, dirname)
# import os#�ļ�����
#
# # �����ļ������ƺͱ�ǩ�Ķ�Ӧ��ϵ
# label_map = {
#     'cat': 0,
#     'dog': 1,
#     'bat': 2
# }
#
# with open('data.txt', 'w') as f:
#     # ���������ļ���rootΪ��ǰ�ļ��У�dirs���������ļ�������files�������ļ���
#     for root, dirs, files in os.walk('data'):
#         for filename in files:
#             filepath = os.sep.join([root, filename])  # ����ļ�����·��
#             dirname = root.split(os.sep)[-1]  # ��ȡ��ǰ�ļ�������
#             label = label_map[dirname]  # �õ���ǩ
#             line = '{},{}\n'.format(filepath, label)
#             f.write(line)
#���̲���
# from multiprocessing import Process  , freeze_support
#
#
# def process_data(filelist):
#     for filepath in filelist:
#         print('Processing {} ...'.format(filepath))
#         # ��������
#         ...
#
#
# if __name__ == '__main__':
#     # �������Windows�£�����Ҫ����freeze_support()
#     freeze_support()
#
#     # full_list������Ҫ�����ȫ���ļ��б�
#     ...
#     full_list=[1,2,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,11,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
#     n_total = len(full_list)  # һ��Զ����32����
#     n_processes = 32
#
#     # ÿ�����б��ƽ������
#     length = float(n_total) / float(n_processes)
#
#     # �����±꣬�����ܾ��ȵػ��������ļ��б�
#     indices = [int(round((i + 1) * length)) for i in range(-1, n_processes)]
#
#     # ����ÿ������Ҫ��������ļ��б�
#     sublists = [full_list[indices[i]:indices[i + 1]] for i in range(n_processes)]
#
#     # ���ɽ���
#     processes = [Process(target=process_data, args=(x,)) for x in sublists]
#
#     # ���д���
#     for p in processes:
#         p.start()
#
#     for p in processes:
#         p.join()